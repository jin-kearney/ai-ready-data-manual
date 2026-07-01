# Labelbox

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | Labelbox Inc. (미국) |
| 라이선스 | 상용 (SaaS, 엔터프라이즈 계약) |
| 배포 형태 | SaaS 클라우드, 엔터프라이즈 온프레미스(문의) |
| 최신 동향 | 멀티모달 추론 리더보드 론칭(Q1 2025); Labelbox Applied Research 3대 축 발표(Evals·Agents·Robotics); Alignerr Connect(전문가 AI 트레이너 직접 채용) 출시; PDF 박스→텍스트 자동 추출; 오디오 자동 전사 기능 |

---

## 한 줄 포지셔닝

> **엔터프라이즈 AI 데이터 팩토리 — 멀티모달 라벨링에서 모델 평가·로보틱스 데이터까지 AI 개발 전 생명주기 지원**

---

## 주요 기능

### 멀티모달 라벨링
- **이미지**: 바운딩 박스(텍스트 자동 추출 포함), 세그멘테이션, 키포인트, 폴리곤
- **비디오**: 프레임별 어노테이션, 객체 추적
- **텍스트**: NER, 분류, 관계 추출
- **오디오**: 자동 전사(STT) → 라벨링 에디터 내 자동 텍스트 변환 (2025 신규)
- **PDF**: 박스 드로잉 → 내부 텍스트 자동 추출 (2025 신규)
- **멀티모달 채팅**: 인터랙티브 채팅 데이터 라벨링, 단계별 추론 분류(Step-by-step Reasoning)

### Model-Assisted Labeling
- 커스텀 ML 모델 연동 → 사전 라벨 예측 부트스트랩
- AI 기반 문법·워딩 제안 (In-editor Suggestions, 멀티모달 채팅 에디터)
- 예측 신뢰도 기반 인간 검토 라우팅

### Labelbox Applied Research (2025 신규)
세 가지 축:
1. **Labelbox Evals**: 통합 모델 평가 — 인간 선호도·정확도·일관성 평가
2. **Labelbox Agents**: 신뢰성 있는 AI 에이전트 구축용 데이터 파이프라인
3. **Labelbox Robotics (LBRx)**: 로봇 조작 학습용 고품질 훈련 데이터 생성

### 전문가 인력 연계 (Alignerr Connect)
- Alignerr: 철저히 검증된 AI 트레이너·전문 라벨러 풀
- 직접 채용 가능한 AI 트레이너 마켓플레이스
- 논리적 스토리텔링, 시각적 차이 탐지, 공간 추론 등 전문 능력 검증

### Multimodal Reasoning Leaderboard
- 이미지 캡셔닝, 공간 추론, 논리적 스토리텔링, 시각적 차이 탐지 등 종합 평가
- 최첨단 LLM의 멀티모달 이해 능력 비교

---

## AI-Ready Data 주제 매핑

| AI-Ready Data 주제 | 관련도 | 비고 |
|---|:---:|---|
| B-2 라벨링·어노테이션 | ★★★ | 핵심 기능, 멀티모달 |
| Human-in-the-Loop (HITL) | ★★★ | 전문가 라벨러 연계, 리뷰 워크플로 |
| GenAI/LLM 모델 평가 | ★★★ | Evals, RLHF, 멀티모달 리더보드 |
| 로봇·물리 AI | ★★★ | LBRx 로보틱스 전문 데이터 |
| 학습 데이터 품질 | ★★★ | IAA, 전문가 검토 품질 보증 |

---

## 강점

- **멀티모달 에디터 통합**: PDF·오디오 자동 텍스트 추출, 채팅 단계별 추론 분류
- **전문가 라벨러 직접 연결**: Alignerr Connect로 특화 AI 트레이너 즉시 조달
- **로보틱스 데이터 특화**: LBRx 축으로 물리 AI/로봇 조작 학습 데이터 구축
- **모델 평가 통합**: 라벨링 → 모델 학습 → 평가 단일 플랫폼
- **엔터프라이즈 API**: 개발자 친화적 API, 커스텀 ML 모델 연동 간편

---

## 약점·주의점

- **비용**: 엔터프라이즈 가격 정책으로 소규모 팀에는 높은 비용
- **오픈소스 아님**: Label Studio·CVAT 대비 오픈소스 옵션 없음
- **온프레미스**: 완전 온프레미스 배포는 별도 계약 필요
- **LiDAR**: 포인트클라우드 3D 어노테이션은 Encord·CVAT 대비 제한
- **의료 DICOM**: DICOM 전문 지원 제한

---

## 가격 모델

| 플랜 | 가격 | 주요 내용 |
|---|---|---|
| Starter | 무료(제한) / 소액 | 팀 소규모, 기본 라벨링 |
| Business | 월 구독 (문의) | 팀 협업, AI 지원 |
| Enterprise | 연간 계약 (문의) | 무제한·SLA·온프레미스·전용 지원 |

> 상세 가격은 팀 크기·처리량·기능 세트에 따라 문의

---

## 연동 생태계

```
ML 프레임워크: PyTorch, TensorFlow, Hugging Face
데이터 저장소: S3, GCS, Azure Blob, 로컬 스토리지
데이터 포맷: COCO, Pascal VOC, YOLO, JSON, CSV
API: REST API, GraphQL API, Python SDK
기타: Webhooks, 커스텀 ML 백엔드 연결
```

---

## 최신 동향 (2025~2026)

- **Q1 2025**: 멀티모달 추론 리더보드 공개 — LLM 멀티모달 이해 평가 표준화
- **2025**: PDF 에디터 박스→텍스트 자동 추출, 오디오 자동 전사 기능 추가
- **2025**: 멀티모달 채팅 에디터 AI 제안(문법·워딩 자동 교정)
- **2025**: Step-by-step Reasoning 태스크 — LLM 추론 단계별 correct/incorrect 분류
- **2025**: **Labelbox Applied Research** 론칭 — Evals·Agents·Robotics 3대 축
- **2025**: **Alignerr Connect** 출시 — 전문 AI 트레이너 직접 채용 마켓플레이스

---

## 출처

- https://labelbox.com/
- https://labelbox.com/blog/q1-2025-labelbox-spotlight-new-products-and-services/
- https://docs.labelbox.com/changelog
- https://techdailyshot.com/blog/comparing-data-labeling-platforms-2026
- https://www.techno-pulse.com/2026/05/best-ai-data-labeling-tools-in-2026.html
