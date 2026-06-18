# B-2 데이터 해설·주석(Data Annotation/Labeling) — 출처 검증 리서치

> 목적: 가이드 집필자가 인용할 수 있도록 **솔루션·표준의 공식 URL과 1줄 사실**을 검증한 레퍼런스.
> 접속 확인일: **2026-06-18** / 검증 방식: web_search + web_fetch
> 표기: `[이름](URL) — 1줄 설명 — ✅확인 / ⚠️미확인(사유)`
> 가격·버전 번호는 사실로 단정하지 않음("공식 문서/PoC 확인" 권장).

---

## 1) 어노테이션/라벨링 도구·플랫폼 (Annotation/Labeling Tools & Platforms)

| 도구 | 공식 URL | 1줄 설명 | 지원 어노테이션 유형 | OSS/상용 | 검증 |
|---|---|---|---|---|---|
| Labelbox | [labelbox.com](https://labelbox.com/) / [Annotate 제품](https://labelbox.com/product/annotate/) | 모든 인력·규모로 데이터를 라벨링하는 모델 평가·데이터 라벨링 플랫폼(Annotate) | 텍스트·이미지·오디오·비디오·지리공간·센서(멀티모달). NLP: NER·감성·POS·텍스트 분류 / 이미지: bbox·polygon·semantic seg·keypoint | 상용(SaaS) | ✅확인 |
| Scale AI (Scale Data Engine / Rapid) | [scale.com/data-engine](https://scale.com/data-engine) | 고품질 학습 데이터를 수집·큐레이션·어노테이션하는 데이터 엔진(human-in-the-loop + AI) | 텍스트·비디오·지리공간·이미지 등 | 상용 | ✅확인 |
| Label Studio (HumanSignal) | [labelstud.io](https://labelstud.io/) / [GitHub](https://github.com/HumanSignal/label-studio) / 기업판 [humansignal.com](https://humansignal.com/) | 다중 데이터 유형을 지원하는 오픈소스 데이터 라벨링·AI 평가 도구 | 오디오·텍스트·이미지·비디오·시계열 | **OSS**(Apache-2.0, 기업판 별도) | ✅확인 |
| Roboflow | [roboflow.com](https://roboflow.com/) / [Annotate](https://roboflow.com/annotate) | 컴퓨터 비전 데이터셋 관리·어노테이션·학습·배포 올인원 플랫폼 | 이미지 중심(bbox·polygon 등), 30+ 어노테이션 포맷 변환 지원 | 상용(코어). 오픈소스 라이브러리 `supervision` 별도 | ✅확인 |
| Snorkel Flow (Snorkel AI) | [snorkel.ai](https://snorkel.ai/) / [weak supervision 가이드](https://snorkel.ai/data-centric-ai/weak-supervision/) | 라벨링 함수(programmatic labeling)·약지도(weak supervision)로 학습 데이터를 대량 생성하는 데이터 중심 AI 플랫폼 | 텍스트 등(약지도/프로그래매틱 라벨링) | 상용(Flow). 연구용 OSS [snorkel-team/snorkel](https://github.com/snorkel-team/snorkel) 별도 | ✅확인 |
| Amazon SageMaker Ground Truth | [aws.amazon.com/sagemaker/ai/groundtruth](https://aws.amazon.com/sagemaker/ai/groundtruth/) / [문서](https://docs.aws.amazon.com/sagemaker/latest/dg/sms.html) | 인력+ML로 고품질 학습 데이터셋을 만드는 AWS 데이터 라벨링 서비스(셀프서비스 + 매니지드 Ground Truth Plus) | 텍스트·이미지·비디오·3D 포인트 클라우드 | 상용(AWS 매니지드) | ✅확인 |
| Prodigy (Explosion) | [prodi.gy](https://prodi.gy/) / [문서](https://prodi.gy/docs) | 자체 머신에서 도는 스크립트형 어노테이션 도구, spaCy와 긴밀 통합 | NER·텍스트 분류·POS·의존구문·엔티티 링킹·관계 추출 등(주로 NLP, 이미지도 가능) | 상용(라이선스 구매) | ✅확인 |
| Cleanlab / Cleanlab Studio | [cleanlab.ai](https://cleanlab.ai/) / OSS [github.com/cleanlab/cleanlab](https://github.com/cleanlab/cleanlab) / Studio 문서 [help.cleanlab.ai/studio](https://help.cleanlab.ai/studio/quickstart/web/) | 라벨 오류·이상치·중복 등 데이터 문제를 자동 탐지하고 더 나은 라벨을 제안하는 데이터 중심 AI 도구 | 텍스트·테이블·이미지 분류(라벨 오류 탐지) | OSS 라이브러리(`cleanlab`) + 상용 Studio | ✅확인 |
| CVAT | [cvat.ai](https://www.cvat.ai/) / [GitHub](https://github.com/cvat-ai/cvat) / [문서](https://docs.cvat.ai/) | 이미지·비디오·3D 비전 데이터셋 구축용 어노테이션 플랫폼(AI 보조 라벨링·QA) | 이미지·비디오·3D (객체 검출·분류·세그멘테이션) | **OSS**(Community는 MIT) + 클라우드·기업판 | ✅확인 |
| SAM 2 / Segment Anything (Meta) | [ai.meta.com/research/sam2](https://ai.meta.com/research/sam2/) / 데모 [sam2.metademolab.com](https://sam2.metademolab.com/) | 클릭·박스·마스크 입력으로 이미지·비디오의 객체를 빠르게 분할하는 통합 세그멘테이션 모델(프리라벨링 자동화에 활용) | 이미지·비디오 세그멘테이션(마스크 자동 생성) | **OSS**(모델 Apache-2.0, SA-V 데이터셋 CC BY 4.0) | ✅확인 |
| DVC (Data Version Control) | [dvc.org](https://dvc.org/) / [시작 문서](https://doc.dvc.org/start) | Git 확장 방식으로 데이터·모델을 버전 관리하는 CLI/VS Code 도구(데이터셋 버전 관리) | 데이터셋·모델 버전 관리(어노테이션 유형 아님) | **OSS**. (참고: 2025-11 lakeFS가 DVC 인수 발표 — [위키](https://en.wikipedia.org/wiki/Data_Version_Control_(software)) 기재, 세부는 ⚠️PoC 확인) | ✅확인 |
| lakeFS | [lakefs.io](https://lakefs.io/) / [문서](https://docs.lakefs.io/) | 객체 스토리지(S3/GCS/Azure)를 Git처럼 브랜치·커밋·머지하는 데이터 버전 관리 | 데이터레이크 버전 관리(어노테이션 유형 아님) | **OSS** + 기업판/클라우드 | ✅확인 |

> 주의: 위 OSS/상용 구분과 라이선스는 검색 시점 공식 페이지 기준. **정확한 에디션·라이선스·가격은 도입 시 공식 문서/PoC로 재확인**할 것. 버전 번호는 명시하지 않음.

---

## 2) 어노테이터 간 일치도(IAA, Inter-Annotator Agreement) 통계

| 지표 | 권위 출처 URL | 쉬운 설명 | 검증 |
|---|---|---|---|
| Cohen's kappa (κ) | [en.wikipedia.org/wiki/Cohen's_kappa](https://en.wikipedia.org/wiki/Cohen's_kappa) | **두 명**의 어노테이터가 범주형(categorical)으로 매긴 라벨의 일치도를, 우연히 맞을 확률을 빼고 보정한 지표. 범위 −1~1 | ✅확인 |
| Fleiss' kappa | [en.wikipedia.org/wiki/Fleiss'_kappa](https://en.wikipedia.org/wiki/Fleiss'_kappa) | Cohen κ를 **3명 이상(임의 수)** 의 어노테이터로 확장한 버전. 항목마다 평가자가 달라도 적용 가능(1971, Fleiss) | ✅확인 |
| Krippendorff's alpha (α) | [en.wikipedia.org/wiki/Krippendorff's_alpha](https://en.wikipedia.org/wiki/Krippendorff's_alpha) | **평가자 수·척도 종류(명목·순서·구간·비율)에 무관**하고 **결측(missing) 데이터도 처리**하는 일반화된 일치도 계수. 0(체계적 불일치)~1(완전 일치), 관행상 α≥.800 권장 | ✅확인 |

### Landis & Koch (1977) — κ 해석 기준 (Cohen's kappa 위키 인용, 정확히 확인)

| κ 범위 | 라벨 (원문) | 한글 |
|---|---|---|
| < 0 | No agreement | 일치 없음 |
| 0.00 – 0.20 | Slight | 미미 |
| 0.21 – 0.40 | Fair | 보통 이하 |
| 0.41 – 0.60 | Moderate | 보통 |
| 0.61 – 0.80 | Substantial | 상당 |
| 0.81 – 1.00 | Almost perfect | 거의 완벽 |

> 출처 원문(Cohen's kappa Wikipedia): *"...characterized values < 0 as indicating no agreement and 0–0.20 as slight, 0.21–0.40 as fair, 0.41–0.60 as moderate, 0.61–0.80 as substantial, and 0.81–1 as almost perfect agreement."* — ✅확인
>
> ⚠️ **주의(라벨 표기차)**: 의뢰서에는 <0.0 구간을 "poor"로 적었으나, Wikipedia가 인용한 **Landis & Koch 원문은 <0을 "No agreement"** 로 표기한다. ("poor"는 일부 2차 자료의 변형 표기.) 가이드에는 위 표의 **No agreement** 표기를 권장.

---

## 3) 이미지 어노테이션 유형 (Image Annotation Types)

> 권위 보조 출처: Sama [Image Annotation Guide](https://www.sama.com/blog/image-annotation-guide), Humans in the Loop [Types of image annotation](https://humansintheloop.org/types-of-image-annotation/), Roboflow [Annotation Formats](https://roboflow.com/formats), Labelbox [Annotate Overview](https://docs.labelbox.com/docs/annotate-overview) — ✅확인

| 유형 | 1줄 정의 | 검증 |
|---|---|---|
| Bounding Box | 객체를 감싸는 직사각형(축 정렬)으로 위치를 표시. 좌상단·우하단 좌표로 표현. 빠른 객체 검출용 | ✅확인 |
| Polygon / Instance Segmentation Mask | 객체 외곽을 따라 다각형으로 둘러싸 픽셀 영역을 채움. 같은 클래스라도 **개별 객체(instance)별**로 구분 | ✅확인 |
| Semantic Segmentation Mask | 이미지의 **모든 픽셀**에 클래스 라벨을 부여(사람·차·도로 등). 개별 객체 구분 없이 클래스 단위 | ✅확인 |
| Keypoint / Skeleton | 관절·이목구비 등 핵심 지점을 점으로 찍고 연결해 자세(skeleton)를 표현. 포즈 추정·얼굴 정렬용 | ✅확인 |
| Polyline | 닫지 않은 연결 선분(open). 차선·전선·균열·강줄기 같은 선형 피처용(영역을 채우지 않음) | ✅확인 |
| Classification Tag | 영역이 아니라 이미지/프레임 **전체에 라벨(태그)** 을 부여(예: 양품/불량). 분류 작업용 | ✅확인 |

---

## 4) 텍스트 어노테이션 유형 (Text Annotation Types)

> 권위 보조 출처: Label Your Data [Text Annotation](https://labelyourdata.com/articles/data-annotation/text-annotation), Prodigy 문서 [prodi.gy/docs](https://prodi.gy/docs), Labelbox NLP 도구 설명 — ✅확인

| 유형 | 1줄 정의 | 검증 |
|---|---|---|
| Named Entity Recognition (NER) | 텍스트에서 사람·기관·장소·날짜·수치 등 **개체(entity)** 를 찾아 유형을 라벨링. 정보 추출·지식그래프의 출발점 | ✅확인 |
| Span annotation | 자유 형식의 **텍스트 구간(span)** 을 태깅. 엔티티 링킹·관계 추출·중첩 엔티티 작업에 사용 | ✅확인 |
| Relation Extraction | 개체들이 **서로 어떻게 연결되는지(관계)** 를 매핑(예: A가 B에 소속) | ✅확인 |
| Sentiment annotation | 텍스트에 긍정/부정/중립 등 **감성·의견 라벨**을 부여. 리뷰·SNS·문의 톤 분석용 | ✅확인 |
| Document Classification | 문장·문서 **전체 단위로 라벨** 부여(스팸 탐지·주제 분류·문서 감성 등) | ✅확인 |

---

## 검증 요약 / 갭

- **1) 도구 12종 전부 공식 URL·1줄 설명·OSS/상용 구분 ✅확인.** OSS: Label Studio, CVAT(Community MIT), SAM 2(모델 Apache-2.0), DVC, lakeFS, Cleanlab 라이브러리, Snorkel(연구용 OSS). 상용/SaaS: Labelbox, Scale, Roboflow(코어), SageMaker GT, Prodigy, Snorkel Flow, Cleanlab Studio.
- **2) IAA 3종 + Landis & Koch 6밴드 ✅확인** — 밴드 경계·라벨을 Cohen's kappa Wikipedia 원문으로 그대로 확인. ⚠️ 단 <0 구간은 원문이 **"No agreement"**(의뢰서 "poor"는 변형 표기) — 위 §2 주의 참조.
- **3) 이미지 6유형 · 4) 텍스트 5유형 ✅확인** — 정의는 단일 1차 공식문서 1개로 못 박기보다 라벨링 플랫폼 docs/가이드 다수에서 일치 확인(업계 표준 명칭).
- **추가 발견(가이드 활용 가능)**: **DVC가 2025-11 lakeFS에 인수**됐다는 기재(위키). 세부 인수 조건은 ⚠️미확인 — 가이드에 단정 인용 시 공식 발표 재확인 권장.
- **단정 회피 항목**: 가격·버전 번호·정확한 에디션 차이는 일절 사실로 적지 않음 — 모두 "공식 문서/PoC 확인".
