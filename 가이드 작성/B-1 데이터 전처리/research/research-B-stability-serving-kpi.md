# B-1 데이터 전처리 — 리서치 노트: 안정성·적재·KPI·로드맵

> 작성 목적: B-1 가이드의 How(안정성·운영), 적재 대상, 구축 절차, KPI·고도화 로드맵 섹션 작성을 위한 웹 리서치 원자료.  
> 관점 고정: "AI가 쓸 데이터를 준비·구조화하는 법" — AI 구축법 X  
> 작성일: 2026-06-18

---

## 1. 원천 양식 변경에 대한 안정성

### 1-1. 문제 정의

보고서·엑셀 양식·표 레이아웃이 바뀌면 규칙 기반 파서가 즉시 깨진다. 예:
- 열 순서 변경 → 필드명 오매핑
- 표 머리글 병합 → 셀 추출 오류
- 페이지 여백/폰트 변경 → PDF 레이아웃 파서 좌표 불일치

**두산 계열사 현업 예시:**  
분기마다 조금씩 바뀌는 품질 보고서(QC Report) — 사업부마다 열 순서가 다르거나, 반기 말에 항목이 추가됨 → 파서가 "A열=불량율"로 하드코딩되어 있으면 다음 분기 적재 시 전체 수치가 뒤섞임.  
설비별로 다른 점검 엑셀 양식 — 설비 A는 7열, 설비 B는 9열 → 단일 파서로 처리하면 설비 B의 추가 열이 묵시적으로 드랍.

### 1-2. 골든 문서셋(Golden Test Set)을 통한 회귀 테스트

**개념:**  
골든 테스트셋은 "현재 파서 출력을 저장된 '골든' 기준선과 비교하여 파이프라인 회귀(regression)를 감지하는 방법"이다.  
알려진 정상 상태(known-good state)의 파서 출력을 스냅샷으로 저장해 두고, 양식 변경 또는 파서 코드 변경 후에도 의도치 않은 동작이 생겼는지를 자동 검증한다.

**구성 요소:**

| 구성 | 설명 |
|------|------|
| 골든 문서 샘플 | 대표 양식·엣지케이스·이전 버전 양식을 포함한 고정 테스트 문서 세트 |
| 기대 출력(golden output) | 해당 문서를 처리했을 때 나와야 하는 정규화된 JSON/표 스냅샷 |
| 허용 오차(tolerance) | 예: 핵심 필드 100% 일치, 부가 필드 90% 이상 일치 |
| CI/CD 통합 | 파서 코드 변경 시 자동 실행 → 회귀 발생 시 파이프라인 중단 |

**베스트 프랙티스:**
- 버전 관리: 골든 파일을 불변 스냅샷으로 버전화하고, 추가·삭제·재라벨링 이력(change log)을 남긴다.
- 메타데이터 포함: 파서 버전·설정·타임스탬프를 함께 저장해 진단을 빠르게 한다.
- 정기 갱신: 양식이 공식 변경되면 골든 파일을 업데이트하고 "이전 버전 양식"도 하위 호환 테스트용으로 보관.
- 출력 차이(diff) 검토: 변경된 출력이 개선인지 회귀인지 담당자가 판단하는 검토 프로세스.

출처: [Golden Tests in AI: Ensuring Reliability Without Slowing Innovation | Shaped](https://www.shaped.ai/blog/golden-tests-in-ai), [What Is a Golden Dataset in AI and Why Does It Matter? | DAC.digital](https://dac.digital/what-is-a-golden-dataset/)

### 1-3. 파싱 결과 스키마 검증(Output Schema Validation)

파서 출력이 구조적으로 올바른지 매 실행마다 검증한다. JSON Schema를 사용하면 데이터 타입·필수 필드·값 범위를 선언적으로 정의할 수 있다.

**파이프라인 내 검증 적용 지점 4단계:**

1. **수집(Ingestion)**: 들어오는 문서 메타데이터가 미리 정의된 스키마와 일치하는지 확인
2. **변환(Transformation)**: 추출된 표·필드가 여전히 예상 형식인지 검증
3. **보강(Enrichment)**: 추가 데이터 병합 시 구조 유지 여부 확인
4. **적재(Storage)**: 최종 저장 전 품질 표준 충족 확인

"Quality gates stop the pipeline when inputs violate contracts" — 계약(스키마) 위반 입력을 초기 격리.

출처: [Ensuring Data Quality with JSON Schema Validation | DataHen](https://www.datahen.com/blog/ensuring-data-quality-with-json-schema-validation-in-data-processing-pipelines/)

---

## 2. 전처리 결과 적재(서빙) 대상

전처리 산출물을 어디에 제공하느냐는 **다운스트림 활용 목적**에 따라 달라진다.

### 2-1. 적재 대상 비교

| 적재 대상 | 언제 쓰나 | 특징 |
|-----------|-----------|------|
| **벡터 DB(Vector DB)** | AI가 의미 유사도 검색(RAG)으로 문서를 찾아야 할 때 | 임베딩(embedding) 벡터로 변환 후 저장. 키워드가 달라도 의미가 유사하면 검색됨 |
| **검색 인덱스(Search Index)** | 키워드 기반 전문 검색, 하이브리드 검색(키워드+벡터)이 필요할 때 | 역인덱스(inverted index) 구조. BM25 등 키워드 매칭 강함 |
| **데이터레이크(Data Lake)** | 원시(raw) 전처리 결과를 장기 보관하거나 다양한 다운스트림에 공급할 때 | 비정형·정형 데이터 모두 수용. 배치 분석·재처리에 적합 |
| **분석 테이블(Analytics Table)** | BI·대시보드·집계 쿼리에서 수치 데이터를 바로 쓸 때 | DW(데이터 웨어하우스)/데이터레이크하우스의 정형화된 테이블. SQL 쿼리 대상 |

### 2-2. 벡터 DB 대표 제품 (공식 URL)

> 벡터 DB는 임베딩(embedding)으로 변환된 텍스트를 저장해 의미 기반 유사도 검색을 가능하게 한다. 임베딩 모델 자체를 만드는 도구가 아니라, 임베딩 결과를 받아 저장·검색하는 데이터 저장소다.

| 제품 | 유형 | 언제 적합 | 공식 URL |
|------|------|-----------|----------|
| **pgvector** | PostgreSQL 확장 | 기존 PostgreSQL 인프라가 있는 조직, 관계형+벡터 검색 통합 | [github.com/pgvector/pgvector](https://github.com/pgvector/pgvector) |
| **Pinecone** | 완전 관리형(SaaS) | 대규모 프로덕션, 별도 인프라 관리 없이 수십억 벡터 처리 | [pinecone.io](https://www.pinecone.io/) / [docs.pinecone.io](https://docs.pinecone.io/guides/get-started/overview) |
| **Milvus** | 오픈소스(자체 호스팅) | 대규모 자체 호스팅, 수억 벡터 이상 고성능 검색 | [milvus.io/docs](https://milvus.io/docs) / [github.com/milvus-io/milvus](https://github.com/milvus-io/milvus) |
| **Chroma** | 오픈소스 | PoC·소규모 프로토타이핑, 빠른 설정 | [trychroma.com](https://www.trychroma.com/) / [docs.trychroma.com](https://docs.trychroma.com/docs/overview/introduction) |
| **Elasticsearch** | 오픈소스(엔터프라이즈 옵션) | 전문 검색+벡터 하이브리드, 기존 Elastic 스택 활용 | [elastic.co/docs/solutions/search/vector](https://www.elastic.co/docs/solutions/search/vector) |
| **OpenSearch** | 오픈소스(AWS 관리형 옵션) | Elastic 대안, AWS 기반 인프라, k-NN+하이브리드 검색 | [docs.opensearch.org/latest/vector-search](https://docs.opensearch.org/latest/vector-search/) |

**PoC·규모별 선택 가이드 (확인 필요 — 공식 벤치마크 참조):**
- 소규모 프로토타입: Chroma (간단한 설정)
- 기존 Postgres 환경: pgvector
- 엔터프라이즈 프로덕션(SaaS): Pinecone
- 자체 호스팅 대규모: Milvus

출처: [Best Vector Databases 2026 | DataCamp](https://www.datacamp.com/blog/the-top-5-vector-databases), [Pinecone vs pgvector vs Chroma vs Weaviate 2026 | GroovyWeb](https://www.groovyweb.co/blog/vector-database-comparison-2026), [OpenSearch Vector Search](https://docs.opensearch.org/latest/vector-search/), [Elasticsearch Vector Search](https://www.elastic.co/docs/solutions/search/vector)

---

## 3. 전처리 파이프라인 구축 절차

### 3-1. 표준 단계별 흐름

```
[1] 대상 문서 선정
     ↓ 
[2] 원문 추출 (PDF/Excel/HTML → 텍스트·표·이미지)
     ↓
[3] 구조화 (문서 요소 분류: 제목/본문/표/수식/각주)
     ↓
[4] 위치 정보 보존 (페이지 번호·섹션 경로·바이트 오프셋)
     ↓
[5] 청킹 (Chunking: 의미 단위로 분할)
     ↓
[6] 적재 (Search Index / Vector DB / Data Lake / Analytics Table)
```

**각 단계 세부:**

| 단계 | 내용 | 도구/방법 예시 |
|------|------|----------------|
| 대상 선정 | AI 활용 우선순위 높은 문서부터 선정 (품질보고서, 설비점검표, 매뉴얼 등) | 문서 유형·접근빈도·구조 복잡도 기준 |
| 원문 추출 | PDF→텍스트, Excel→JSON, HTML→Markdown | PyMuPDF, Apache Tika, Unstructured |
| 구조화 | 요소 분류 (제목/단락/표/이미지 캡션) | computer vision + NLP 기반 레이아웃 감지 |
| 위치 정보 보존 | 각 청크에 소스 문서 ID·페이지·섹션 경로 저장 | 메타데이터 필드로 관리 |
| 청킹 | 고정 크기(512 토큰, 50 토큰 overlap) 또는 의미 기반(semantic chunking) | LangChain, LlamaIndex, Unstructured |
| 적재 | 임베딩 변환 후 Vector DB 저장, 또는 검색 인덱스에 색인 | pgvector, Pinecone, Elasticsearch |

출처: [The Role of Data Preprocessing in RAG | deepset](https://www.deepset.ai/blog/preprocessing-rag), [RAG Chunking Strategy | Unstructured](https://unstructured.io/blog/unstructured-s-preprocessing-pipelines-enable-enhanced-rag-performance), [Develop a RAG Solution - Chunking Phase | Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-chunking-phase)

### 3-2. 배치(Batch) vs 증분(Incremental) 처리

| 방식 | 설명 | 언제 적합 |
|------|------|-----------|
| **배치(Batch)** | 일정 주기(일별·주별)로 전체 또는 대량 문서를 한꺼번에 처리 | 원천 시스템이 지속 읽기 부담을 못 견딜 때, 지연 허용 가능 |
| **증분(Incremental)** | 마지막 처리 시점 이후 변경된 문서만 처리 | 데이터 최신성이 중요할 때, 처리 비용 절감 필요 시 |
| **마이크로 배치** | 짧은 주기로 소량씩 배치 실행 | 실시간에 가까운 갱신 + 배치의 안정성 병행 |

**증분 처리 메커니즘:**  
- 타임스탬프 기반: 최종 처리 시각 이후 수정된 파일만 선택
- CDC(Change Data Capture): 소스 변경 로그에서 신규/수정 문서를 캡처
- 해시 비교: 문서 내용 해시로 변경 여부 판단

출처: [Incremental and Continuous Data Ingestion Strategies | Unstructured](https://unstructured.io/insights/incremental-data-ingestion-strategies-for-continuous-pipelines), [Incremental Load in ETL | Airbyte](https://airbyte.com/data-engineering-resources/etl-incremental-loading)

### 3-3. 사람 검수가 필요한 지점

deepset에 따르면 "전처리는 RAG 프로젝트의 약 50%를 차지"한다. 특히 사람 검수가 필요한 포인트:

- **복잡한 표 구조**: 병합 셀·다단계 헤더·중첩 표 → 자동 추출 오류율 높음
- **스캔 품질 낮은 문서**: 기울기·노이즈·손상된 OCR 결과 → 수동 보정
- **양식 변경 감지**: 스키마 검증 실패 → 원인 파악·골든 파일 업데이트
- **이미지·도면 내 수치**: 비정형 이미지 안의 텍스트(도면 치수 등) → 특수 처리
- **도메인 전문 표기**: 두산 설비코드·내부 약어 → 용어 사전 기반 후처리

---

## 4. 성과 지표(KPI)

### 4-1. 핵심 KPI 목록

| KPI | 정의 | 방향 | 측정 방법 |
|-----|------|------|-----------|
| **전처리 완료율** | 대상 문서 중 오류 없이 처리 완료된 비율 | ↑ 높을수록 좋음 | (완료 건수 / 전체 대상 건수) × 100 |
| **표 추출 정확도** (Table Extraction Accuracy) | 추출된 표 셀이 원문과 일치하는 비율 (F1 Score 기준) | ↑ 높을수록 좋음 | 정밀도(Precision)·재현율(Recall)로 F1 계산; TEDS·GriTS 지표 활용 가능 |
| **파서 안정성율** (양식 변경 후 무중단율) | 양식 변경 이벤트 발생 후 파이프라인이 중단 없이 처리한 비율 | ↑ 높을수록 좋음 | (양식 변경 후 정상 처리 건수 / 전체 양식 변경 이벤트) × 100 |
| **STP(직통 처리율)** (Straight-Through Processing) | 사람 개입 없이 완전 자동 처리된 문서 비율 | ↑ 높을수록 좋음 | (자동 처리 완료 건수 / 전체 처리 건수) × 100 |
| **처리량(Throughput)** | 단위 시간당 처리 문서 수 또는 페이지 수 | ↑ 높을수록 좋음 | 건/시간 또는 페이지/분 |
| **건당 비용** | 문서 1건 처리에 드는 비용 (CPU·API·인건비 포함) | ↓ 낮을수록 좋음 | 총 운영 비용 / 처리 건수 |
| **파이프라인 에러율** | 전체 처리 건 대비 오류 건수 비율 | ↓ 낮을수록 좋음 | (오류 건수 / 전체 건수) × 100 |
| **다운스트림 검색 기여** | 전처리 품질이 AI 검색 정확도에 기여하는 정도 | ↑ 높을수록 좋음 | RAG 검색 정밀도(Retrieval Precision@K) 변화 추적 |

### 4-2. 표 추출 정확도 측정 지표 상세

**기본 지표:**
- **F1 Score**: 정밀도(Precision)와 재현율(Recall)의 조화 평균. F1 = 2PR/(P+R)
- **TEDS (Tree Edit Distance-based Similarity)**: 표를 HTML 트리로 표현 후 편집 거리로 유사도 계산. 구조·내용 동시 평가.
- **GriTS (Grid Table Similarity)**: 표를 2D 배열로 처리, 행과 열을 균등하게 평가. 내용(edit distance)·구조(rowspan/colspan)·위치(공간 IoU) 3가지 기준 제공.
- **IOU (Intersection over Union)**: 레이아웃 감지에서 예측 영역과 실제 영역의 겹침 비율

출처: [The Ultimate Guide to Assessing Table Extraction | Nanonets](https://nanonets.com/blog/the-ultimate-guide-to-assessing-table-extraction/), [Data Pipeline Monitoring | Atlan](https://atlan.com/data-pipeline-monitoring/)

---

## 5. 고도화 로드맵

### 5-1. 성숙도 4단계 서사

문서 처리 자동화는 단계별로 성숙한다. 제조 현업에서의 현실적 경로:

#### 1단계: 수작업(Manual)
- 담당자가 PDF·Excel을 열어 복사·붙여넣기로 데이터 추출
- 양식마다 다른 방법 → 일관성 없음
- 확장 불가, 오류율 높음

#### 2단계: 도구 보조(Tool-Assisted)
- 표준 파서(PyMuPDF, Apache POI, Camelot 등)로 자동 추출 시도
- 규칙 기반 → 양식이 조금만 바뀌어도 수동 재작업 필요
- "규칙 변경 필요 시 취약성 발생"
- 골든 테스트셋·스키마 검증을 도입해 파이프라인 안정성 확보

#### 3단계: 지능형 반자동(Intelligent Semi-Auto, IDP)
- 머신러닝+NLP 기반 지능형 문서 처리(IDP, Intelligent Document Processing)
- 다양한 양식을 학습으로 처리 → 양식 변경 내성 향상
- 어려운 양식(병합 표, 도면)만 사람이 검수
- IDP 도입 시 "52% 오류 감소, 약 99% 필드 수준 정확도" 보고 사례
- 12개월 내 3~5배 ROI 보고 사례 (공식 문서·PoC 수치 확인 필요)

#### 4단계: 자동화+사람 최소화(Automated)
- LLM 보강 처리(레이아웃 이해, 맥락 기반 추출)
- 사람은 예외·신규 양식 유형 검수만 담당
- 완전 자동화 파이프라인 + CI/CD 통합 회귀 테스트

**두산 계열사 현실 경로 제언:**  
현재 대부분이 1~2단계. 3단계 진입 시 우선 "품질 보고서, 설비 점검표" 같은 반복 문서부터 골든셋 기반 안정화 → STP 목표 지표 설정 → 3단계로 단계적 이행.

출처: [The Complete Guide to Document Processing | Nanonets](https://nanonets.com/blog/document-processing/), [Intelligent Document Processing (IDP) Guide | BizData360](https://www.bizdata360.com/intelligent-document-processing-idp-ultimate-guide-2025/), [Data Maturity in Manufacturing | Ansoim](https://www.ansoim.com/data-maturity-manufacturing-strategic-roadmap-for-transformation)

---

## 6. 두산 계열사 현업 적용 맥락

### 6-1. 품질 보고서 양식 변경 문제
- 분기마다 조금씩 바뀌는 QC Report → 파서 설정이 분기마다 수동 수정 필요
- 파이프라인 회귀 테스트(골든셋) 미도입 시: 양식 변경 사실을 AI 검색 정확도 저하로 뒤늦게 발견
- 적재 대상: 품질 트렌드 분석 → 분석 테이블, AI 근거 제시 → 벡터 DB

### 6-2. 설비별 다른 점검 엑셀 양식
- 설비 A~Z마다 열 구성이 다름 → 통일된 파서 불가, 설비별 파서 N개 유지
- 증분 처리: 점검 완료 즉시 신규 파일을 자동 처리 → 검색 인덱스에 반영
- 적재 대상: 키워드 검색(설비명, 날짜) → 검색 인덱스; AI 이상 감지 → 벡터 DB + 분석 테이블

---

## 참고자료 (전체 출처 목록)

| 주제 | 출처 | URL |
|------|------|-----|
| 골든 테스트셋 | Shaped AI Blog | https://www.shaped.ai/blog/golden-tests-in-ai |
| 골든 데이터셋 개념 | DAC.digital | https://dac.digital/what-is-a-golden-dataset/ |
| 골든 파일 업데이트 | johal.in (pytest-regressions 2025) | https://johal.in/pytest-regressions-data-golden-file-updates-2025/ |
| JSON 스키마 검증 | DataHen Blog | https://www.datahen.com/blog/ensuring-data-quality-with-json-schema-validation-in-data-processing-pipelines/ |
| RAG 전처리 역할 | deepset Blog | https://www.deepset.ai/blog/preprocessing-rag |
| 청킹 전략 RAG | Unstructured Blog | https://unstructured.io/blog/unstructured-s-preprocessing-pipelines-enable-enhanced-rag-performance |
| 청킹 전략 가이드 | DataCamp | https://www.datacamp.com/blog/chunking-strategies |
| RAG 청킹 단계 | Microsoft Learn Azure | https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-chunking-phase |
| 증분 수집 전략 | Unstructured Insights | https://unstructured.io/insights/incremental-data-ingestion-strategies-for-continuous-pipelines |
| ETL 증분 로딩 | Airbyte | https://airbyte.com/data-engineering-resources/etl-incremental-loading |
| 표 추출 평가 | Nanonets Blog | https://nanonets.com/blog/the-ultimate-guide-to-assessing-table-extraction/ |
| 문서 파싱 벤치마크 | Unstructured SCORE-Bench | https://unstructured.io/blog/introducing-score-bench-an-open-benchmark-for-document-parsing |
| 데이터 파이프라인 모니터링 KPI | Atlan | https://atlan.com/data-pipeline-monitoring/ |
| 벡터 DB 비교 2026 | DataCamp | https://www.datacamp.com/blog/the-top-5-vector-databases |
| 벡터 DB 비교 상세 | GroovyWeb | https://www.groovyweb.co/blog/vector-database-comparison-2026 |
| pgvector 공식 | GitHub | https://github.com/pgvector/pgvector |
| Pinecone 공식 | Pinecone | https://www.pinecone.io/ |
| Pinecone Docs | Pinecone Docs | https://docs.pinecone.io/guides/get-started/overview |
| Milvus 공식 | Milvus | https://milvus.io/docs |
| Milvus GitHub | GitHub | https://github.com/milvus-io/milvus |
| Chroma 공식 | Chroma | https://www.trychroma.com/ |
| Chroma Docs | Chroma Docs | https://docs.trychroma.com/docs/overview/introduction |
| Elasticsearch 벡터 검색 | Elastic Docs | https://www.elastic.co/docs/solutions/search/vector |
| OpenSearch 벡터 검색 | OpenSearch Docs | https://docs.opensearch.org/latest/vector-search/ |
| 문서 처리 자동화 로드맵 | Nanonets | https://nanonets.com/blog/document-processing/ |
| IDP 가이드 | BizData360 | https://www.bizdata360.com/intelligent-document-processing-idp-ultimate-guide-2025/ |
| 제조 데이터 성숙도 | Ansoim | https://www.ansoim.com/data-maturity-manufacturing-strategic-roadmap-for-transformation |
