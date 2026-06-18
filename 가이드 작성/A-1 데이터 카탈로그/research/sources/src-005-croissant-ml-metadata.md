# src-005: Croissant — ML-Ready Dataset Metadata Format

- URL: https://arxiv.org/html/2403.19546v1
- 제목: Croissant: A Metadata Format for ML-Ready Datasets (MLCommons, 2024)
- 접속일: 2026-06-18

## 개요

Croissant는 ML-ready 데이터셋을 위한 메타데이터 형식. schema.org/Dataset를 확장하며
MLCommons가 2024년 3월 공개. PyTorch·TensorFlow·JAX 등 ML 프레임워크와 직접 연동 가능.

## 4계층 아키텍처

### 1. Dataset Metadata Layer (데이터셋 메타데이터)
schema.org/Dataset 기반 필드:
- **name** — 데이터셋 식별자
- **description** — 데이터셋 개요
- **license** — 사용 권리
- **url** — 데이터셋 위치
- **citeAs** — 인용 정보
- **dct:conformsTo** — 표준 규격 준수 선언

책임 있는 AI(Responsible AI) 문서화 지원:
- 데이터 라이프사이클, 라벨링, 안전성, 공정성, 추적성, 규제 컴플라이언스, 포용성

### 2. Resources Layer (리소스)
- **FileObject** — 개별 파일
  - contentUrl, sha256(체크섬), encodingFormat
- **FileSet** — 파일 그룹
  - containedIn, includes/excludes 패턴, encodingFormat

### 3. Structure Layer (구조)
- **RecordSet** — 개념적 데이터 뷰
  - key (기본 식별자)
  - field 배열 (구조 정의)
- **Field** 속성
  - dataType (예: sc:ImageObject, sc:Text)
  - source (데이터 원천)
  - extract (내용 추출)
  - transform (정규식·조작)
  - references (조인 명세)
  - subField (중첩 구조)

### 4. Semantic Layer (의미론)
- dataType — schema.org 어휘 매핑
- equivalentProperty — 명시적 의미 연결
- ML 특화 메타데이터: 학습/테스트 분할, 레이블 정보

## AI-Ready 관점 의의

Croissant의 데이터셋 메타데이터는 AI 엔지니어가 "학습 중 데이터 동작 방식이나 전처리(preprocessing) 요건을 빠르게 파악"하게 돕는 기술 매뉴얼 역할.
