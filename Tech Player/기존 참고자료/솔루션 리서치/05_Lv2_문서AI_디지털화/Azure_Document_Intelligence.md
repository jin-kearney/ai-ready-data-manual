# Azure Document Intelligence

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | Microsoft (Azure AI 서비스) |
| 라이선스 | 상용 (Azure 종량제·엔터프라이즈) |
| 배포 형태 | Azure 클라우드 API, 컨테이너(온프레미스/에지 배포) |
| 최신 동향 | v4.0 GA (2024.11.30 REST API 기준); Azure Content Understanding으로 통합(2025.11 GA); Layout model 그림 다운로드 기능; 배치 분석 지원; 세금 폼 2025년 버전 대응 |

---

## 한 줄 포지셔닝

> **Azure 생태계 중심의 엔터프라이즈 IDP — v4.0 + Content Understanding으로 문서·이미지·오디오·비디오 통합 처리**

---

## 주요 기능

### 레이아웃 및 OCR (Layout Model)
- 스캔 텍스트 OCR 개선: 단일 문자, 박스 내 텍스트, 밀집 텍스트 문서 정확도 향상
- **그림(Figure) 감지 강화**: 문서 내 그림을 이미지 파일로 다운로드 — 별도 시각 이해 워크플로 가능
- Searchable PDF 생성 (v4.0 Read 컨테이너)
- 읽기 순서(Reading Order) 재정렬

### 사전 구축 모델 (Prebuilt Models)
- Invoice(인보이스), Receipt(영수증), ID Document(신분증)
- W-2, 1099, 세금 폼 (2025년 양식 업데이트, 멀티 폼 일괄 추출)
- Business Card, Marriage Certificate, Mortgage 등
- **수기 인식**: 사전 모델 전반에 걸쳐 강력한 수기체 지원

### 커스텀 모델
- Custom Template: 고정 레이아웃 폼 훈련
- Custom Neural: 다양한 레이아웃 적응형 학습
- Custom Classifier: 문서 종류 분류

### 배치 처리
- 배치 분석 오퍼레이션 지원 — 다수 문서 일괄 처리로 처리 효율 향상

### Azure Content Understanding 통합 (GA 2025.11)
- OCR + 생성형 AI(GPT)를 결합한 상위 레이어
- 문서·이미지·오디오·비디오 멀티모달 처리
- Azure AI Foundry Tools 내에서 통합 관리

### 컨테이너 배포 (온프레미스)
- v4.0 Read 컨테이너 GA — 완전 로컬 또는 에지 배포 가능
- Disconnected(인터넷 차단) 환경 컨테이너 제공(별도 라이선스)

---

## AI-Ready Data 주제 매핑

| AI-Ready Data 주제 | 관련도 | 비고 |
|---|:---:|---|
| B-1 비정형 문서 파싱/전처리 | ★★★ | 레이아웃·표 추출, 사전 모델 |
| F-3 종이·수기 OCR 디지털화 | ★★★ | 수기 인식 최강급, 폼 필드 추출 |
| 데이터 파이프라인 | ★★★ | Azure Data Factory, Logic Apps 연계 |
| 벡터 임베딩/RAG | ★★☆ | Azure AI Search와 통합 |
| 데이터 거버넌스 | ★★☆ | Azure Purview 연계, 규정 준수 |

---

## 강점

- **수기 인식**: 폼 필드·서명·수기 텍스트 인식에서 업계 최상위
- **엔터프라이즈 생태계**: Azure AD, Azure Data Factory, Power Automate, M365 완벽 연계
- **컨테이너 배포**: 온프레미스·에지 배포로 보안 구역 적용 가능
- **다국어**: 100+ 언어 지원
- **멀티모달 확장**: Content Understanding으로 오디오·비디오까지 확장
- **다양한 사전 모델**: 인보이스·영수증·신분증·세금 폼 등 즉시 사용 가능

---

## 약점·주의점

- **한국어 특화 부족**: 영어·라틴 문자 대비 한국어(특히 HWP) 처리 열세
- **청킹 미내장**: RAG 청킹은 Azure AI Search 또는 별도 처리 필요
- **완전 오프라인 비용**: Disconnected 컨테이너는 별도 라이선스 필요
- **가격 복잡성**: API 종류(Layout, Prebuilt, Custom)별 다른 가격 체계
- **GCP/오픈소스 연계**: AWS·GCP와의 멀티클라우드 연계는 추가 구성 필요

---

## 가격 모델

| 모델 종류 | 가격(기준) |
|---|---|
| Read (기본 OCR) | $1.50 / 1,000페이지 |
| Layout | $10 / 1,000페이지 |
| Prebuilt (Invoice, Receipt 등) | $10 / 1,000페이지 |
| Custom (Template/Neural) | $10 / 1,000페이지 훈련 + $10 / 1,000페이지 추론 |
| 무료 티어 | 500페이지/월 (F0) |

> 가격은 Azure 지역·플랜별 변동, 엔터프라이즈 계약 시 협의 가능

---

## 연동 생태계

```
Azure: Azure Data Factory, Azure AI Search, Azure Logic Apps, Power Automate, M365
LangChain: AzureAIDocumentIntelligenceLoader
LlamaIndex: AzureAIDocumentIntelligenceReader
API: REST API, Python/C#/Java/JavaScript SDK
Azure Content Understanding: 문서+이미지+오디오+비디오 통합
```

---

## 최신 동향 (2025~2026)

- **2024.11.30**: v4.0 REST API GA — 배치 분석, Searchable PDF, 그림 이미지 다운로드
- **2025.01**: v4.0 Read 컨테이너 GA (온프레미스 배포)
- **2025.08**: 세금 폼 2025년 버전 대응, 멀티 W-2/1099 일괄 추출
- **2025.11**: Azure Content Understanding GA — OCR + 생성형 AI 통합, 멀티모달
- **2026.01**: OCR 모델 개선(단일 문자, 박스 텍스트, 밀집 텍스트 정확도 향상)
- 레거시 프로세서 2026.06.30 종료 예정 → 신규 모델 마이그레이션 권고

---

## 출처

- https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/whats-new?view=doc-intel-4.0.0
- https://azure.microsoft.com/en-us/products/ai-foundry/tools/document-intelligence
- https://azure.microsoft.com/en-us/pricing/details/document-intelligence/
- https://jannikreinhard.com/2026/01/12/master-the-paper-chaos-comparing-azures-ocr-and-document-intelligence-powerhouses/
- https://www.signisys.com/blog/azure-ai-document-intelligence/
- https://www.ocrvendors.com/vendors/azure-document-intelligence
