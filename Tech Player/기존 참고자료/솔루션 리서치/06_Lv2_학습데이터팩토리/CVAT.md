# CVAT (Computer Vision Annotation Tool)

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | CVAT.ai (前 Intel 사내 프로젝트, 2022년 독립 법인화) |
| 라이선스 | MIT (오픈소스) / 상용 CVAT.ai Cloud |
| 배포 형태 | 오픈소스 자체 호스팅, CVAT.ai Cloud(SaaS) |
| 최신 동향 | SAM (Segment Anything) 통합 — 자동 세그멘테이션 마스크/박스 생성; OpenVINO Toolkit 기반 AI 지원 강화; Intel로부터 독립 후 CVAT.ai 브랜드로 성장 |

---

## 한 줄 포지셔닝

> **Intel이 만들고 CVAT.ai가 키운 오픈소스 CV 어노테이션 표준 — SAM·OpenVINO AI 지원과 광범위한 포맷 내보내기**

---

## 주요 기능

### 어노테이션 유형
- **이미지**: 바운딩 박스, 폴리곤, 폴리라인, 키포인트, 비트마스크
- **3D 포인트클라우드**: 3D 큐보이드 어노테이션 (LiDAR)
- **비디오**: 객체 추적(인터폴레이션), 프레임별 어노테이션
- **멀티 레이블**: 이미지·세그먼트 분류

### AI-Assisted Labeling
- **SAM(Segment Anything Model)**: 세그멘테이션 마스크 또는 바운딩 박스 자동 생성 → 인간 수정
- **Mask R-CNN**: 자동 인스턴스 세그멘테이션 제안
- **YOLO**: 객체 탐지 사전 라벨
- **Intel OpenVINO 기반 AI 모델**: CPU 최적화로 엣지·온프레미스에서도 AI 지원
- Semi-automatic 모드: 자동 생성 → 인간 정제 방식

### 비디오 특화
- **객체 추적 인터폴레이션**: 키프레임 지정 → 중간 프레임 자동 보간
- 프레임 단위 세밀한 어노테이션

### 데이터 관리
- **데이터셋 내보내기**: COCO, Pascal VOC, YOLO, ImageNet, Cityscapes, TFRecord 등
- 멀티유저 협업: 역할 기반 접근 제어
- 클라우드 스토리지: AWS S3, Azure Blob Storage 직접 연동

### 배포 옵션
- Docker 기반 자체 호스팅 (docker-compose)
- Kubernetes 클러스터 배포
- CVAT.ai Cloud (관리형 서비스)

---

## AI-Ready Data 주제 매핑

| AI-Ready Data 주제 | 관련도 | 비고 |
|---|:---:|---|
| B-2 라벨링·어노테이션 | ★★★ | 핵심 기능, CV 특화 |
| 물리 AI·자율주행 | ★★★ | LiDAR 3D 큐보이드 지원 |
| 데이터 파이프라인 | ★★☆ | 다양한 포맷 내보내기 |
| 온프레미스 데이터 관리 | ★★★ | 완전 자체 호스팅 가능 |

---

## 강점

- **완전 오픈소스 MIT**: 상업적 사용 포함 무제한 자유 — 라이선스 비용 없음
- **업계 표준**: GitHub 최다 스타 CV 어노테이션 도구 중 하나, 광범위한 커뮤니티
- **SAM 통합**: 최신 파운데이션 모델로 수동 작업 대폭 감소
- **온프레미스 완전 지원**: Docker/Kubernetes로 보안 구역·사내망 배포
- **다양한 포맷 내보내기**: COCO·YOLO·VOC 등 주요 ML 프레임워크 포맷 지원
- **Intel OpenVINO**: CPU 최적화 AI 추론 — GPU 없는 엣지 환경에서도 AI 지원

---

## 약점·주의점

- **텍스트/NLP 라벨링**: 텍스트 어노테이션(NER 등) 기능 미흡
- **오디오 미지원**: 오디오 데이터 어노테이션 불가
- **PDF 미지원**: 문서 라벨링 불가
- **GenAI 평가**: RLHF·챗봇 평가 기능 없음
- **자체 호스팅 부담**: 대규모 배포 시 인프라 관리 필요
- **HITL 워크플로**: 구조화된 리뷰·IAA 스코어링 기능 제한 (Enterprise급 Label Studio 대비)

---

## 가격 모델

| 플랜 | 가격 | 주요 내용 |
|---|---|---|
| OSS (자체 호스팅) | 무료 | Docker 배포, 모든 기본 기능 |
| CVAT.ai Cloud (Free) | 무료 (제한) | 소규모 프로젝트 |
| CVAT.ai Cloud (Team) | 월 구독 (문의) | 팀 협업, 클라우드 저장 |
| CVAT.ai Cloud (Enterprise) | 연간 계약 (문의) | 무제한·SLA·전용 지원 |

---

## 연동 생태계

```
AI 모델: SAM (Segment Anything), Mask R-CNN, YOLO, OpenVINO 모델 서버
클라우드 스토리지: AWS S3, Azure Blob Storage
데이터 포맷: COCO, Pascal VOC, YOLO, ImageNet, Cityscapes, TFRecord, MOT
배포: Docker Compose, Kubernetes
API: REST API, Python SDK
ML 프레임워크: PyTorch, TensorFlow (데이터 내보내기 연계)
```

---

## 최신 동향 (2025~2026)

- **2022**: Intel에서 독립, CVAT.ai 법인화 — 독자적 상용 서비스 전개
- **2023~2025**: SAM(Segment Anything Model) 통합 — 자동 마스크/박스 생성, 수동 정제 워크플로
- **지속**: OpenVINO 기반 AI 모델 최적화 업데이트 — CPU 환경 AI 추론 성능 향상
- **지속**: 다양한 포맷 내보내기 확장 — 자율주행·로봇 도메인 포맷 추가
- **CVAT.ai Cloud**: 관리형 서비스 기능 지속 강화 (팀 협업, 대시보드)

---

## 제조업 관점 코멘트

- **비전 검사 내재화**: 오픈소스 MIT 라이선스로 라이선스 비용 없이 사내 배포 — 결함 이미지 라벨링 팀 구성 용이
- **엣지/공장 내 배포**: Intel OpenVINO로 GPU 없는 생산 현장 PC에서도 AI-assisted 라벨링 가능
- **LiDAR 물류**: 창고 자동화·AGV용 포인트클라우드 어노테이션에 CVAT 3D 큐보이드 활용

---

## 출처

- https://www.cvat.ai/
- https://docs.cvat.ai/
- https://viso.ai/computer-vision/cvat-computer-vision-annotation-tool/
- https://opencv.org/blog/opencv-and-cvat-computer-vision-annotation-tool-intel/
- https://www.cvat.ai/resources/blog/best-open-source-data-annotation-tools
- https://www.cvat.ai/resources/blog/home
