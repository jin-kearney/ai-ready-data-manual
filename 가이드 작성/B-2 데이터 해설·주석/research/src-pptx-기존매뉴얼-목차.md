# B-2. Understandable — 데이터 해설·주석 (기존 매뉴얼 목차)

> 출처: `기존 매뉴얼 작성본/Kearney_두산지주_AI-ready Data 체계_데이터 주제별 가이드 B-2. 데이터 해설 주석.pptx` (총 35장)
> 아래는 기존 PPTX 장표의 **실제 구성을 그대로 목차화**한 것이다 (현업판 재구성 전 원본 구조 파악용).

---

## 0. 표지·목차
- 표지 — AI-Ready Data 체계 데이터 주제별 가이드 / B-2. Understandable 데이터 해설·주석 (DE Center)
- 목차 — Why / What / How / KPI(案) / Roadmap

## 1. Why — 데이터 해설·주석 필요성
1.1 데이터 해설·주석 필요성 (1/2)
   - Key Objectives: ① 데이터 의미·판단 기준 표준화 ② 신뢰 가능한 AI 학습 환경 구축 ③ 라벨링 품질·추적 관리 체계 구축
   - AI Data Pain Points: 표준 정의 부재 / 라벨링·주석 기준 부재로 품질 편차 / 주석 이력·품질 관리 미흡
1.2 데이터 해설·주석 필요성 (2/2) — 3대 기대효과
   - ① 기계 가독형 신호로의 전환 (Raw → 라벨링·해설 → AI-Ready Data)
   - ② 모델 훈련 최적화와 비용 절감 (전처리 비용↓·재학습↓·신뢰도↑)
   - ③ 지능형 자산화 및 재사용성 보장 (표준 스키마 → 여러 AI 과제 재사용)

## 2. What — 데이터 해설·주석의 정의
2.1 정의 (1/2) — 일반 데이터/Raw vs 라벨·주석·해석
   - Raw Data + 일반 메타데이터(파일명·촬영일시·설비·공정·자재 등)
   - 주석 종류·라벨 값·라벨 형태(분류/다중클래스/수치/조치 라벨)·해설 예시
2.2 정의 (2/2) — 라벨링·주석·해설 3계층 구조
   - ① 데이터 라벨링(Macro) — 표준 범주 정의, Ground Truth 기반
   - ② 데이터 주석(Micro) — 라벨 상세 설명(위치·원인·조치·부품·심각도·시간)
   - ③ 데이터 해설(Free Form) — 사람의 판단·경험·배경 자유 기록
2.3 Annotation 4대 유형 개관 (Text / Image / Video / Audio)
   - 유형별 정의·제조업 활용 예시
2.4 Text Annotation 상세
   - NER / Span / Relation Extraction / Sentiment / Document Classification
2.5 Image Annotation 상세 (1/2) — 유형 표
   - Bounding Box / Polygon·Instance Mask / Semantic Mask / Keypoint·Skeleton / Polyline / Classification Tag
2.6 Image Annotation 상세 (2/2) — 정밀도·정보량 비교
   - Classification → Bounding Box → Polygon → Semantic Mask → Keypoint (장점·고려사항)
2.7 Video Annotation 상세
   - Frame Classification / Object Tracking / Action / Event / Temporal Segment
2.8 Audio Annotation 상세
   - Sound Event / Speech-to-Text / Speaker / Intent / Emotion Annotation

## 3. How — 라벨 체계 설계 방안
3.1 전체 절차 개요 — 8단계 표준 프로세스
   - 대상 데이터 선정 → Taxonomy 설계 → Guideline 작성 → Pilot 라벨링 → IAA 측정·보정 → 본 라벨링 → QA·검수 → 데이터셋 버전 관리
   - 단계별 목적·선행조건·주요 산출물
3.2 ① 대상 데이터 선정
   - 카탈로그 기반, AI가 의미·맥락·판단 이해 어려운 데이터 우선
   - 대상 유형 4종(정형/비정형/멀티미디어/이벤트·로그) × Text·Image·Audio·Video별 주석 필요성
3.3 ② Taxonomy(분류 체계) 설계
   - 3원칙: 상호배타성 / 포괄성 / 일관성
   - Taxonomy 정의·역할, Before & After 예시
3.4 ② Taxonomy 구조 유형 — Flat / Hierarchical / Multi-label
   - 정의·장단점·적용 예시 비교
3.5 ③ Annotation Guideline 작성
   - 정의·필요성(주관 최소화·품질 확보·재작업 절감·IAA 향상)
   - 필수 구성요소 8: Objective·Definition·Scope·Rule·Positive/Negative Example·Boundary Case·Decision Rule
3.6 ③ 좋은 Guideline의 조건·필수요소
   - Completeness Illusion / Boundary Case 우선 / If-Then·결정규칙·Gold Standard·버전관리 등
3.7 ④ Pilot 라벨링
   - 데이터 설계(Train/Test/Hold-out 분할)·Ground Truth 구축·Pilot 테스트
   - 성능 지표(Accuracy·F1·Cohen's Kappa)·결과 분석·개선 방향 도출
3.8 ⑤ IAA 측정 및 가이드라인 보정
   - 지표: Cohen's κ / Fleiss' κ / Krippendorff's α (적용조건·임계값)
   - 해석 기준(Landis & Koch), 합의 규칙(다수결·가중·순차검토·다중 QC)
3.9 ⑤ Labeler 합의 시스템 설계
   - 랜덤 배정 → 합의 규칙 결정 → 검증 → 일관성 모니터링 → 고품질 데이터셋
3.10 ⑤ ML 라벨링 프로세스 활용 (Active/Transfer Learning·QA 자동화)
3.11 ⑤ Gold Standard Dataset
   - 개념·역할, 구축 프로세스, 핵심 요건, 필요 시점(수행 전/중)
3.12 ⑥ 본 라벨링 — 대규모 데이터셋 구축
   - Batch 생성·라벨링 수행·결과 검토·데이터셋 적재
   - 운영 관리 포인트(생산성·품질·예외 관리)
3.13 ⑥ AI 자동화 + HITL 검수 체계
   - AI 자동화(Pre-labeling·Active Learning·Weak Supervision/Snorkel)
   - Confidence 기반 라우팅(자동 승인 / Reviewer / SME 검수)
3.14 ⑥ 자동 라벨링 워크플로우 (AWS Ground Truth 사례)
   - 8단계 자동 라벨링 루프·핵심 체크포인트·목표 지표(정확도·mIoU)
3.15 ⑧ 데이터셋 버전 관리
   - 필요성(재현성·추적성·신뢰성·리스크 대응)·대상·흐름·이력 예시
   - 버전 규칙(Major/Minor/Patch)
3.16 Tech Stack — 솔루션사 비교 (1/2)
   - Labelbox / Scale AI / Label Studio
3.17 Tech Stack — 솔루션사 비교 (2/2)
   - Roboflow / Snorkel Flow / SageMaker Ground Truth / Prodigy / Cleanlab Studio

## 4. KPI (案)
4.1 핵심 KPI 정의 (지표·산식·해석·주기)
   - IAA(라벨 일관성) / 라벨 오류율(LER) / 처리량·건당 비용 / QA 통과율·재작업률 / AI Pre-label 채택률(ALAR)

## 5. Roadmap
5.1 3단계 전환 전략
   - Phase 1: Preparation (기반 정립) — Guideline v0.1·Taxonomy·Gold Set·Pilot·IAA 기준선 / 수작업 70~80%
   - Phase 2: AI Ready (AI 보조 효율화) — Pre-labeling·Confidence 라우팅·Active Learning·Cleanlab / AI 40~50%
   - Phase 3: 자동화 고도화 — Weak Supervision(Snorkel)·Foundation Model·합성데이터·Data Flywheel / AI 90~95%
   - 단계별 도입 기술(Label Studio·CVAT·Labelbox → Cleanlab·DVC/LakeFS → Snorkel Flow·SAM 2·LLM·MLOps)
