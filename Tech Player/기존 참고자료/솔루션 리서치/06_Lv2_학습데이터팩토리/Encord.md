# Encord

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | Encord (영국·미국) |
| 라이선스 | 상용 SaaS (SOC2 Type II, HIPAA, GDPR 인증) |
| 배포 형태 | SaaS 클라우드, 엔터프라이즈 온프레미스(문의) |
| 최신 동향 | SAM 3 통합(Early Access 2026); Cloud-synced Folder 지원; DICOM 볼륨 MPR에 SAM 적용; 수치형 온톨로지 속성 추가; 코멘트·이슈 어노테이션 태스크 기능(Beta) |

---

## 한 줄 포지셔닝

> **컴퓨터 비전 특화 엔드-투-엔드 플랫폼 — SAM3 AI 자동 라벨링·네이티브 비디오·LiDAR·의료 DICOM까지 단일 워크스페이스**

---

## 주요 기능

### 지원 데이터 모달리티
- **이미지**: 바운딩 박스, 폴리곤, 폴리라인, 키포인트, 비트마스크, 세그멘테이션
- **비디오**: 네이티브 렌더링(다운샘플링 없음), 객체 추적, 프레임별 분석
- **LiDAR/포인트클라우드**: 3D 큐보이드 어노테이션
- **센서 퓨전**: 이미지·LiDAR·오디오·텍스트 동일 워크플로
- **의료 DICOM**: DICOM 볼륨 MPR(다평면 재구성) 지원 + SAM AI 자동 라벨
- **오디오·텍스트**: 기본 지원

### SAM 통합 (Segment Anything Model)
- **SAM 3 Early Access (2026)**: 최신 버전 통합 — 텍스트 프롬프트 또는 원클릭으로 모든 인스턴스 동시 라벨링
- 클래스 이름에서 바로 세그멘테이션 마스크 생성
- **DICOM MPR 볼륨에 SAM 적용**: 의료·산업 3D 이미지 자동 세그멘테이션

### 어노테이션 유형
- 바운딩 박스, 폴리곤, 폴리라인, 키포인트, 비트마스크
- 3D 큐보이드 (포인트클라우드)
- 객체 추적 (비디오 프레임 간 연속 추적)
- **수치형 온톨로지 속성 (2026 신규)**: 슬라이더·수치 입력으로 속성값 정밀 지정

### HITL 워크플로
- 어노테이터 → 리뷰어 파이프라인
- 태스크별 코멘트·이슈 기록 (Beta 2026)
- Inter-annotator Agreement 스코어링

### 데이터 관리
- **Cloud-synced Folder 지원 (2026)**: 클라우드 스토리지 폴더 실시간 동기화
- 버전 관리, 데이터셋 분할(Train/Val/Test)

---

## AI-Ready Data 주제 매핑

| AI-Ready Data 주제 | 관련도 | 비고 |
|---|:---:|---|
| B-2 라벨링·어노테이션 | ★★★ | 컴퓨터 비전 특화, SAM3 |
| Human-in-the-Loop (HITL) | ★★★ | 리뷰 워크플로, 코멘트 기능 |
| 물리 AI·자율주행 | ★★★ | LiDAR·센서 퓨전·비디오 추적 |
| 의료·산업 특수 데이터 | ★★★ | DICOM MPR, 3D 볼륨 |
| 데이터 품질 관리 | ★★☆ | IAA, 이슈 트래킹 |

---

## 강점

- **SAM 3 최신 통합**: 원클릭·텍스트 프롬프트 자동 세그멘테이션으로 라벨링 속도 10배 이상 향상 가능
- **네이티브 비디오**: 다운샘플링 없는 원본 품질 렌더링, 프레임 간 객체 추적
- **DICOM 전문 지원**: 의료·산업 CT/MRI MPR 볼륨에 AI 자동 세그멘테이션
- **LiDAR·센서 퓨전**: 자율주행·로봇·물류 자동화용 포인트클라우드 어노테이션
- **보안 인증**: SOC2 Type II, HIPAA, GDPR — 의료·금융·엔터프라이즈 컴플라이언스

---

## 약점·주의점

- **텍스트/NLP 라벨링**: 순수 텍스트 NLP 어노테이션 기능은 Label Studio 대비 제한
- **오픈소스 아님**: CVAT·Label Studio 대비 오픈소스 옵션 없음
- **GenAI 평가**: RLHF·챗봇 평가 기능 Label Studio·Labelbox 대비 제한
- **가격**: 고급 기능 엔터프라이즈 플랜은 고가
- **온프레미스**: 표준 SaaS 전용, 온프레미스는 별도 협의

---

## 가격 모델

| 플랜 | 가격 | 주요 내용 |
|---|---|---|
| Starter | 무료(제한) | 소규모 팀, 기본 어노테이션 |
| Team | 월 구독 (문의) | 팀 협업, AI 지원, 추적 |
| Enterprise | 연간 계약 (문의) | 무제한·SLA·온프레미스·전용 지원 |

---

## 연동 생태계

```
ML 프레임워크: PyTorch, TensorFlow, Ultralytics (YOLO)
데이터 저장소: AWS S3, GCS, Azure Blob (Cloud-synced Folder)
AI 모델: SAM (Segment Anything Model), SAM 3
데이터 포맷: COCO, YOLO, Pascal VOC, JSON
API: Python SDK (encord 패키지), REST API
보안: SOC2 Type II, HIPAA, GDPR
```

---

## 최신 동향 (2025~2026)

- **2025**: 다양한 어노테이션 기능 릴리즈 — 비트마스크·폴리라인·3D 큐보이드 강화
- **2025.12~2026.01**: SAM 3 Early Access 통합 — 최신 Segment Anything Model 탑재
- **2026**: 수치형 온톨로지 속성 추가 (슬라이더·수치 입력)
- **2026**: Cloud-synced Folder 지원 — S3/GCS/Azure 폴더 실시간 동기화
- **2026**: 어노테이션 태스크 코멘트·이슈 기능 Beta 출시
- **2026**: DICOM MPR 볼륨에 SAM 적용 — 의료 3D 이미지 자동 세그멘테이션 확장

---

## 제조업 관점 코멘트

- **비전 검사(Visual Inspection)**: 제조 결함 탐지 모델용 이미지 라벨링에 SAM3 자동 세그멘테이션으로 속도·정확도 동시 향상
- **로봇·물류 자동화**: LiDAR·포인트클라우드 어노테이션으로 피킹 로봇·AGV 학습 데이터 구축
- **품질 이미지 아카이브**: 기존 검사 이미지를 폴더별 Cloud-synced로 자동 수집·라벨링 연동 가능

---

## 출처

- https://encord.com/
- https://docs.encord.com/release-notes/releasenotes-2025
- https://encord.com/blog/best-data-labeling-platform-2026/
- https://encord.com/blog/data-annotation-companies-for-computer-vision/
- https://encord.com/blog/best-data-annotation-tools-for-physical-ai/
