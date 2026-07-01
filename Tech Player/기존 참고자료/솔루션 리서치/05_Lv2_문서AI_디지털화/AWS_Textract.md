# AWS Textract

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | Amazon Web Services (AWS) |
| 라이선스 | 상용 (AWS 종량제·엔터프라이즈) |
| 배포 형태 | AWS 클라우드 API (완전 관리형, 온프레미스 미지원) |
| 최신 동향 | 2026년 회전 텍스트·저해상도 팩스 인식 정확도 개선; Layout 기능 추가(단락·헤더·제목 그룹핑); Analyze Lending API 강화 |

---

## 한 줄 포지셔닝

> **AWS 생태계에 최적화된 Document AI — 5가지 특화 API로 텍스트 추출부터 대출 서류 처리까지**

---

## 주요 기능

### API 구성 (5종)

| API | 용도 |
|---|---|
| Detect Document Text | 기본 텍스트 OCR 추출 |
| Analyze Document | 폼(KV 쌍), 표, 서명, 레이아웃 분석 |
| Analyze Expense | 인보이스·영수증 특화 필드 추출 |
| Analyze ID | 신분증(여권·운전면허 등) 특화 |
| Analyze Lending | 대출 서류(모기지, 소득 증명) 특화 |

### Layout 기능 (신규)
- 단어를 단락·헤더·제목·목록으로 자동 그룹핑 (읽기 순서 재정렬)
- 기존에는 사용자 정의 후처리가 필요했던 작업을 자동화

### 수기·회전 텍스트 개선 (2026)
- 회전된 텍스트, 저해상도 팩스 문서 인식 정확도 개선
- 폼 필드 KV(Key-Value) 쌍 추출

### 비동기 처리
- 대용량 문서 비동기 분석 지원 (SNS 알림 연계)
- S3 직접 참조 — 대용량 배치 파이프라인 구성 용이

### AWS 생태계 통합
- S3 → Textract → Lambda → DynamoDB/RDS 파이프라인
- Amazon Comprehend(NLP), Amazon A2I(Human Review)와 연계
- AWS Step Functions로 워크플로 오케스트레이션

---

## AI-Ready Data 주제 매핑

| AI-Ready Data 주제 | 관련도 | 비고 |
|---|:---:|---|
| B-1 비정형 문서 파싱/전처리 | ★★☆ | 표·폼 추출, 레이아웃 그룹핑 |
| F-3 종이·수기 OCR 디지털화 | ★★★ | 수기 인식, 폼 필드, 서명 감지 |
| 데이터 파이프라인 | ★★★ | S3/Lambda/Step Functions 완전 통합 |
| Human-in-the-loop | ★★☆ | Amazon A2I 연계로 저신뢰도 항목 인간 검토 |

---

## 강점

- **AWS 생태계 완전 통합**: S3, Lambda, Step Functions, Comprehend, A2I — 기존 AWS 인프라 활용
- **특화 API**: 대출·인보이스·신분증 등 도메인 특화 처리 즉시 사용 가능
- **운영 부담 없음**: 완전 관리형 서비스, 인프라 관리 불필요
- **볼륨 할인**: 대용량(100만+ 페이지) 처리 시 단가 급감
- **서명 감지**: 서명 존재 여부 탐지(법적 문서 처리 유용)

---

## 약점·주의점

- **온프레미스 미지원**: 완전 AWS 클라우드 전용, 에어갭 환경 불가
- **한국어 성능**: 한국어·CJK 특화 처리 부족 (Upstage·NAVER 대비)
- **HWP 미지원**: 국내 한글 문서 형식 처리 불가
- **복잡 레이아웃**: 다단·복잡 레이아웃에서 텍스트 순서 오류 발생 가능
- **청킹 미내장**: RAG 파이프라인 구성 시 별도 청킹 처리 필요
- **가격 예측성**: API 조합 시 가격 계산이 복잡

---

## 가격 모델

| API | 가격 (1~100만 페이지) | 볼륨 할인 |
|---|---|---|
| Detect Document Text | $1.50 / 1,000페이지 | 100만+ : $0.60 |
| Analyze Document (Forms) | $50 / 1,000페이지 | 문의 |
| Analyze Document (Tables) | $15 / 1,000페이지 추가 | 문의 |
| Analyze Expense | $8~10 / 1,000페이지 | 문의 |
| Analyze ID | $8 / 1,000페이지 (1~1만) → $0.50 | 단계별 |

**무료 티어**: 신규 고객 3개월간 Detect Document Text 1,000페이지/월 무료

---

## 연동 생태계

```
AWS: S3, Lambda, Step Functions, EventBridge, SNS/SQS
Amazon AI: Comprehend (NLP), A2I (Human Review), Rekognition
LangChain: AmazonTextractPDFLoader
LlamaIndex: AmazonTextractReader
API: Python (boto3), Java, .NET, Go SDK
CDK/SAM: 인프라 코드로 파이프라인 구성
```

---

## 최신 동향 (2025~2026)

- **2026**: 회전 텍스트·저해상도 팩스 인식 정확도 개선 (기존 사용자 불만 대응)
- **2025~2026**: Layout 기능 — 단락·헤더·제목 자동 그룹핑, 읽기 순서 재정렬
- **지속**: Analyze Lending API 강화 — 모기지·소득증명 등 미국 금융 문서 특화
- **지속**: Amazon A2I 통합으로 저신뢰도 결과 인간 검토 워크플로 자동화
- **AWS Bedrock 연계**: Textract 추출 결과를 Bedrock LLM에 투입하는 RAG 패턴 지원

---

## 출처

- https://aws.amazon.com/textract/pricing/
- https://www.signisys.com/blog/amazon-textract-the-complete-guide-to-aws-document-processing/
- https://aiproductivity.ai/tools/aws-textract/
- https://www.braincuber.com/blog/what-is-amazon-textract-document-ai-aws
- https://cloudchipr.com/blog/aws-textract
