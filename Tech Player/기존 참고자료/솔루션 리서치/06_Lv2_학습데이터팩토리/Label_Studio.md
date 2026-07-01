# Label Studio (HumanSignal)

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | HumanSignal Inc. (미국) |
| 라이선스 | Apache 2.0 (OSS Community) / 상용 Enterprise |
| 배포 형태 | 오픈소스 자체 호스팅, HumanSignal Cloud(SaaS), 엔터프라이즈 온프레미스 |
| 최신 동향 | 2025 전체 기능 정리 Webinar 발표; GenAI 벤치마크 평가·에이전틱 트레이스 지원; PDF·스펙트로그램·대화형 데이터 신규 지원; 2025.11 멀티모달 데이터 서비스 부문(HumanSignal Services) 신설 |

---

## 한 줄 포지셔닝

> **오픈소스 멀티타입 라벨링 플랫폼 — 텍스트·이미지·오디오·비디오·GenAI 평가까지 단일 도구로, 대규모 HITL 워크플로 지원**

---

## 주요 기능

### 지원 데이터 모달리티
- **이미지**: 바운딩 박스, 폴리곤, 폴리라인, 키포인트, 비트마스크(픽셀 수준 브러시)
- **텍스트**: NER, 분류, 관계 추출, 문장 분류
- **오디오**: 전사(ASR), 세그먼트, 감정 분류
- **비디오**: 객체 추적(프레임별), 분류
- **PDF**: PDF 내 박스 드로잉 + 텍스트 추출 (2025 신규)
- **스펙트로그램**: 음성·진동 데이터 어노테이션 (2025 신규)
- **대화형(Conversational)**: 채팅 데이터, RLHF 평가 (2025 신규)

### AI-Assisted Labeling
- 사전 라벨 예측 모델 연결 → 작업자 검토·수정 방식
- Confidence-aware 라우팅: 저신뢰도 예측 자동 인간 검토 전달
- 대규모 배치 예측 (수만 태스크 자동 처리)

### GenAI 평가 (2025 신규)
- 커스텀 벤치마크로 GenAI 모델 평가
- 인터랙티브 챗봇 평가 UI
- 에이전틱(Agentic) 트레이스 평가
- A/B 테스트 프롬프트 비교

### HITL 워크플로 (Enterprise)
- 어노테이터 → 리뷰어 → 리드 파이프라인 구조
- **Inter-annotator Agreement**: Cohen's Kappa, Agreement Matrix, Consensus Tooling
- 글로벌 단축키 설정 (작업자 생산성 향상)

### 새 어노테이션 태그 (2025)
- **BitMask**: 픽셀 수준 세그멘테이션 (브러시 기반, 단일 픽셀 세밀도)
- **Vector/VectorLabels**: 폴리라인·폴리곤·스켈레톤 포인트 기반 벡터 어노테이션

---

## AI-Ready Data 주제 매핑

| AI-Ready Data 주제 | 관련도 | 비고 |
|---|:---:|---|
| B-2 라벨링·어노테이션 | ★★★ | 핵심 기능, 멀티모달 |
| Human-in-the-Loop (HITL) | ★★★ | 리뷰 워크플로 내장 |
| 데이터 품질 | ★★★ | IAA 스코어링, 품질 관리 |
| GenAI/LLM 모델 평가 | ★★★ | 챗봇 평가, 에이전틱 트레이스 |
| 학습 데이터 파이프라인 | ★★☆ | 모델 연동, 예측 피드백 루프 |

---

## 강점

- **오픈소스 Apache 2.0**: 무료 자체 호스팅, 완전 커스터마이징 가능
- **멀티모달 단일 도구**: 이미지·텍스트·오디오·비디오·PDF·GenAI 평가를 하나의 플랫폼에서
- **GenAI 평가 선도**: 2025 RLHF·챗봇 평가·에이전틱 트레이스 지원으로 LLM 시대 대응
- **활발한 커뮤니티**: GitHub 20k+ 스타, 다양한 통합 플러그인
- **HITL 내장**: 엔터프라이즈에서 구조화된 품질 관리 워크플로

---

## 약점·주의점

- **LiDAR/3D 지원 제한**: 포인트클라우드·3D 큐보이드는 Encord·CVAT 대비 제한
- **의료 DICOM**: DICOM 볼륨 처리에서 Encord 대비 기능 부족
- **대규모 팀 관리**: 엔터프라이즈 거버넌스·접근 제어는 유료 버전 필요
- **스케일 아웃**: 자체 호스팅 시 대용량 처리를 위한 인프라 직접 관리 필요
- **외주 라벨러 풀**: Labelbox Alignerr 같은 자체 전문가 풀 없음 (HumanSignal Services 신설로 보완 중)

---

## 가격 모델

| 플랜 | 가격 | 주요 내용 |
|---|---|---|
| Community (OSS) | 무료 | 자체 호스팅, 기본 기능 전부 |
| HumanSignal Cloud | 사용량 기반 | 클라우드 관리형, 팀 협업 |
| Enterprise | 연간 계약 (문의) | HITL 워크플로, IAA, SSO, SLA, 전용 지원 |

---

## 연동 생태계

```
ML 프레임워크: TensorFlow, PyTorch, Hugging Face (예측 서버 연결)
LangChain: 라벨 데이터 → LangChain 파이프라인 투입
API: REST API, Python SDK (label-studio-sdk)
클라우드 스토리지: S3, GCS, Azure Blob
데이터 포맷: COCO, Pascal VOC, YOLO, CSV, JSON, CONLL
```

---

## 최신 동향 (2025~2026)

- **2025**: PDF, 스펙트로그램, 대화형 데이터 신규 모달리티 지원
- **2025**: GenAI 평가 기능 — 커스텀 벤치마크, 인터랙티브 챗봇, 에이전틱 트레이스
- **2025**: BitMask(픽셀 수준 브러시), Vector/VectorLabels(포인트 기반 벡터) 신규 태그
- **2025**: 사용자 계정별 글로벌 단축키 설정
- **2025.11**: **HumanSignal Services** 출범 — 멀티모달 데이터 생성·전문 어노테이션 외주 서비스 부문 신설 (Erud AI 인수 기반)
- **Enterprise**: Confidence-aware 라우팅, A/B 프롬프트 테스트, 대규모 배치 예측 배포

---

## 출처

- https://humansignal.com/platform/
- https://labelstud.io/
- https://github.com/HumanSignal/label-studio
- https://humansignal.com/webinars/label-studio-wrapped-2025/
- https://finance.yahoo.com/news/humansignal-launches-multimodal-data-services-165700567.html
- https://docs.humansignal.com/guide/release_notes.html
- https://humansignal.com/blog/automating-quality-control-with-label-studio/
