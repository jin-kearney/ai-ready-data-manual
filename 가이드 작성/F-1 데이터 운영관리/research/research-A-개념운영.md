# F-1 데이터 운영관리(DataOps) — 리서치 A: 개념·운영

> 수집 목적: F-1 가이드의 What / When / How 재료.
> 관점: "AI를 만드는 법"이 아니라 "그 AI가 쓸 데이터를 **안 멈추게 운영**하는 법". F-1은 데이터 파이프라인의 **실행·복구·변경관리**만 다룬다.
> 모든 사실에 출처 URL을 붙였다. 가격·버전 등 변동 수치는 단정하지 않는다.

---

## 0. 인접 주제와의 경계 (먼저 못박기)

F-1이 다루지 않는 것을 명확히 해야 "운영 인프라만"이라는 MECE 경계가 산다.

| 옆 주제 | 그 주제가 맡는 것 | F-1과의 경계 |
|---|---|---|
| C-1 Observability(관측성) | 이상을 "**감지**"한다(지표·알림·이상탐지) | F-1은 감지된 장애를 받아 "**복구·재처리**"한다 |
| C-2 데이터 품질관리 | "이 데이터 **써도 되나**" 품질 판정·기준 | F-1은 파이프라인이 **돌아가게** 하는 것(품질 판정 자체는 C-2) |
| C-3 데이터 계보(Lineage) | 사후 "어디서 와서 어디로 갔나" **추적** | F-1은 변경 시 "어디에 영향 가나"를 보고 통제(추적 자체는 C-3) |
| F-2 데이터 생애주기 | 데이터의 "**수명·보존·폐기**" | F-1은 살아 움직이는 파이프라인의 실행·변경(보존 정책은 F-2) |

쉬운 한 줄: F-1은 "**공장 생산라인을 멈추지 않게 돌리고, 멈추면 다시 돌리고, 라인을 바꿀 땐 뒷공정에 미리 알리는**" 일이다. 불량 감지·품질 합격판정·이력추적은 옆 부서 일.

---

## 1. DataOps란 무엇인가 (What — 정의·구성)

### 1.1 권위 있는 정의

- **Gartner**: DataOps는 "조직 전반에서 데이터 관리자(data managers)와 데이터 소비자(data consumers) 사이의 **데이터 흐름에 대한 소통·통합·자동화**를 개선하는 **협업적 데이터 관리 관행**(collaborative data management practice)"이다. 목표는 "데이터·데이터모델·관련 산출물의 **예측 가능한 전달과 변경 관리**(predictable delivery and change management)를 만들어 가치를 더 빨리 전달"하는 것.
  - 출처: <https://www.gartner.com/en/information-technology/glossary/dataops>
  - 쉬운 한 줄: 데이터를 만드는 쪽과 쓰는 쪽 사이에서, 데이터가 끊김 없이·예측 가능하게·바뀌어도 안 깨지게 흐르도록 만드는 운영 체계.

- **DataOps Manifesto**(업계 합의 선언문): "여러 조직·도구·산업에서 데이터를 다뤄본 경험을 통해, 분석을 개발·전달하는 더 나은 방법을 발견했고 이를 DataOps라 부른다." 18개 원칙으로 구성. Agile + DevOps + Lean Manufacturing(린 제조)에서 차용.
  - 출처: <https://dataopsmanifesto.org/en/>
  - 제조 현업과 맞닿는 핵심 원칙(원문 의역):
    - **#10 Orchestrate**: 데이터·도구·코드·환경·팀을 끝에서 끝까지 **조율**한다.
    - **#11 Make it reproducible**: 데이터·설정·코드를 **모두 버전관리**해 재현 가능하게.
    - **#14 Analytics is manufacturing**: 파이프라인을 **린 제조 라인처럼** 취급한다(← 제조 현업에 가장 직관적).
    - **#15 Quality is paramount / #16 Monitor**: 이상·보안 문제를 **자동 감지**하고 지속 모니터링.
    - **#7 Reduce heroism**: 영웅적 야근에 기대지 말고 **지속가능·확장가능한 프로세스**로.

### 1.2 DevOps와의 관계 (쉬운 비교)

소프트웨어 배포를 자동화·안정화한 DevOps의 원리를 **데이터 파이프라인**에 적용한 것이 DataOps. "DevOps는 소프트웨어 전달을 가속하고, DataOps는 **데이터 전달**을 가속한다." 둘 다 자동화·협업·지속개선·CI에 의존하지만 대상과 이해관계자가 다르다.
- 출처: <https://www.teradata.com/insights/data-platform/what-is-dataops>, <https://www.ibm.com/think/topics/dataops>, <https://www.astronomer.io/what-is-dataops/>
- 쉬운 한 줄: "코드 잘 내보내는 기술(DevOps)"을 "**데이터 잘 흘려보내는 기술(DataOps)**"로 옮긴 것.

### 1.3 핵심 구성요소 (What의 뼈대 — 6개)

| 구성요소 | 쉬운 한 줄 | F-1 KQ |
|---|---|---|
| 오케스트레이션/스케줄링 | 여러 단계 작업을 **정해진 순서·시각에** 자동으로 돌리는 관제탑 | KQ2 |
| 실행·배포 표준 (CI/CD) | 파이프라인을 **고치면 테스트 후 안전하게 운영에 반영**하는 절차 | KQ2 |
| 모니터링·알림 | 돌다가 **멈추면 담당자에게 즉시 알림**(감지 자체는 C-1) | KQ3 |
| 장애 복구(Runbook) | 멈췄을 때 **재처리·롤백·우회**로 되살리는 절차서 | KQ3 |
| 변경 관리 | 구조를 바꿀 때 **쓰는 쪽에 미리 알리고 안 깨지게** 통제 | KQ4 |
| 운영 대상·중요도 관리 | 어떤 파이프라인을 **얼마나 빡세게** 운영할지 차등 | KQ1 |

출처(구성요소 정리): <https://www.informatica.com/resources/articles/understanding-dataops.html>, <https://rivery.io/what-is-dataops/>

---

## 2. 파이프라인 실행·배포 표준화 (How — KQ2)

각 개념을 현업이 바로 이해할 한 줄 풀이 + 출처.

### 2.1 오케스트레이션과 DAG

- **DAG(Directed Acyclic Graph, 방향성 비순환 그래프)**: 작업(노드)과 "A 다음 B" 순서(엣지)를 그린 그림. **순환(되돌이) 없음**. 어떤 단계가 먼저고, 무엇이 무엇에 의존하는지를 정의.
  - 쉬운 한 줄: "**A 끝나야 B, B 끝나야 C**" 같은 작업 순서도. 한 단계가 실패하면 그 뒤 단계는 건너뛴다.
  - 출처: <https://www.databricks.com/blog/what-is-dag>
- **오케스트레이션(Orchestration)**: 이 작업들을 **스케줄대로 실행·의존성 관리·재시도·상태추적**하는 관제. 어느 단계가 왜 실패했고 뒷공정에 어떤 영향인지 보여준다.
  - 출처: <https://www.abstractalgorithms.dev/data-pipeline-orchestration-pattern-dag-retries-and-recovery>

### 2.2 멱등성(Idempotency)

- 같은 데이터를 **몇 번 다시 돌려도 결과가 똑같은** 성질. 그래서 **안심하고 재시도·백필**할 수 있다(중복·이중집계 없음).
- 쉬운 한 줄: "**두 번 돌려도 데이터가 두 배가 안 되는**" 설계. 재처리의 전제조건.
- 출처: <https://airbyte.com/data-engineering-resources/idempotency-in-data-pipelines>, <https://www.ml4devs.com/what-is/backfilling-data/>

### 2.3 재시도(Retry)

- 일시적 실패(네트워크 끊김, API 호출 제한, 잠깐의 DB 잠금)는 흔하다. **자동으로 N번 다시 시도**(예: 3회, 5분 간격)하면 사람 손 없이 대부분 복구.
- 쉬운 한 줄: "**한 번 삐끗하면 자동으로 몇 번 더 해본다.**"
- 출처: <https://datadriven.io/tools/airflow-dag>

### 2.4 백필(Backfill)

- 평소엔 오늘치만 처리하는 파이프라인으로 **과거 기간을 소급 재처리**하는 것. 새 항목 추가·과거 오류 정정 시 옛 구간을 다시 채운다.
- 쉬운 한 줄: "**빠뜨렸거나 틀린 과거 데이터를 다시 채워 넣기.**" 멱등성이 있어야 안전.
- 출처: <https://www.thedataops.org/backfill/>, <https://www.ml4devs.com/what-is/backfilling-data/>

### 2.5 환경 분리 (dev / stg / prod)

- 개발(dev)·검증(staging)·운영(prod)을 **분리**해, 바꾼 것을 운영에 넣기 전에 따로 만든 공간에서 검증. 보통 같은 데이터웨어하우스 안 **서로 다른 스키마**로 나누는 게 가장 쉽고 비용 효율적.
- 쉬운 한 줄: "**시험 라인(dev/stg)에서 먼저 돌려보고 통과해야 본 라인(prod)에 올린다.**"
- 출처: <https://docs.getdbt.com/guides/set-up-ci>

### 2.6 CI/CD·테스트·버전관리

- **버전관리**: 데이터·설정·코드를 **모두 기록**해 언제든 이전 상태로 되돌릴 수 있게(Manifesto #11). 롤백의 토대.
- **데이터 테스트(data test)**: 변경분을 운영에 넣기 전 **자동으로 데이터 무결성 검사**(예: 고유값/누락 없음/허용값/관계 일치). 변경 PR마다 CI에서 실행.
- **CI/CD for data**: 고치면 → 자동 테스트 → 통과하면 → 운영에 자동 승격(promote). 사람 실수·운영 사고를 줄인다.
- 쉬운 한 줄: "**고친 걸 사람이 손으로 옮기지 말고, 자동 검사 통과한 것만 본 라인에 올린다.**"
- 출처: <https://docs.getdbt.com/guides/set-up-ci>, <https://datacoves.com/post/dbt-test-options>, <https://montecarlo.ai/blog-what-is-dbt-testing-definition-best-practices-and-more>

---

## 3. 장애 대응 Runbook (How — KQ3)

### 3.1 Runbook(런북)·On-call·인시던트 대응 (SRE 출처)

- **Runbook/Playbook**: 특정 장애·알림에 대한 **대응 절차서**. Google SRE는 "자동 알림에 어떻게 대응할지에 대한 상위 지침(playbook)"이라 정의. 좋은 런북은 **짧고, 알림에 직접 연결되며, 인시던트마다 사후 갱신**된다.
  - 쉬운 한 줄: "**이 알림이 뜨면 → 이렇게 하라**"를 적어둔 대응 카드.
  - 출처: <https://emmer.dev/blog/an-effective-incident-runbook-template/>, <https://sre.google/sre-book/emergency-response/>
- **On-call(당직)**: 정해진 기간 동안 **운영 장애에 즉시 대응할 수 있게 대기**. 진단·완화·해결·에스컬레이션 수행.
  - 출처: <https://sre.google/workbook/on-call/>
- **인시던트 관리(Google IMAG)**: 미국 재난대응 표준(ICS) 기반. "3C" = **조율(Coordinate)·소통(Communicate)·통제(Control)**. 주요 역할: 인시던트 지휘자(IC)·소통 담당(CL)·운영 담당(OL).
  - 쉬운 한 줄: 큰 장애일수록 "누가 지휘하고·누가 알리고·누가 실제로 고치나"를 미리 정해둔다.
  - 출처: <https://sre.google/resources/practices-and-processes/incident-management-guide/>

### 3.2 복구 수단 — 재처리·롤백·우회

- **재처리(Reprocess)**: 실패 구간을 다시 돌린다(멱등성 + 백필이 전제).
- **롤백(Rollback)**: 잘못된 변경·적재를 **이전 정상 상태로 되돌린다**. "실패 시 더 이른 시점의 올바른 상태로 복원해 실행을 재개." 버전관리·증분백업이 토대.
  - 출처: <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11556431>, <https://www.meegle.com/en_us/topics/etl-pipeline/etl-pipeline-recovery-point-objectives>
- **우회(Failover/Workaround)**: 주 경로가 죽으면 **예비 경로·임시 처리**로 서비스 유지.
- **RTO/RPO**: 복구 목표를 숫자로. **RTO**=얼마나 빨리 복구해야 하나(시간), **RPO**=얼마만큼의 데이터 손실까지 허용하나(시점). 예: "RTO 4시간·RPO 1시간 = 4시간 안에 복구하되 데이터 손실은 1시간치 이하."
  - 쉬운 한 줄: RTO="언제까지 살려라", RPO="과거 어디까지는 지켜라".
  - 출처: <https://launchdarkly.com/blog/rto-vs-rpo/>, <https://datasystemsauthority.com/data-systems-disaster-recovery-planning>

### 3.3 데이터 SLA / SLO / SLI (데이터에 적용)

- **SLI**(지표)=측정값(예: 데이터 신선도, 작업 완료 시각), **SLO**(목표)=내부 목표치, **SLA**(약정)=대외 약속(미달 시 패널티 가능).
  - 출처: <https://chronosphere.io/learn/know-the-sre-fundamentals-differences-between-sli-vs-slo-vs-sla/>
- **데이터 SLA의 차원**: 가용성(Availability)·**신선도(Freshness/Timeliness)**·정확성(Accuracy)·완전성·일관성·**스키마 안정성**에 대한 공표된 약속.
- **신선도 SLO 흔한 형식**: "X% 데이터를 Y분/시간 안에 처리" / "가장 오래된 데이터가 Y 이상 묵지 않음" / "작업이 Y 안에 성공 완료".
  - 쉬운 한 줄: "이 데이터는 **매일 오전 8시까지·최신 1시간 이내로** 준비된다"는 약속.
  - 출처: <https://www.getdbt.com/blog/data-slas-best-practices>, <https://sre.google/workbook/data-processing/>

### 3.4 데이터 파이프라인 장애 유형 (현업 예시 재료)

| 유형 | 무슨 일 | 쉬운 한 줄 |
|---|---|---|
| 소스 지연(Source delay/Late data) | 받아야 할 피드가 늦게/일부만 도착 | 4시간 늦게 온 불완전 배치로 결과가 틀어짐 |
| 스키마 변경/드리프트(Schema drift) | 소스 구조가 말없이 바뀜(컬럼 추가·타입 변경) | 뒷공정 매핑이 조용히 깨짐 |
| 부분 적재(Partial load) | API가 에러 없이 그냥 멈춰 데이터 일부만 적재 | 로그는 성공인데 실제론 반쪽 데이터 |
| 자원 경합(Resource contention) | 월말 등 피크에 자원 부족으로 타임아웃 | 마감철에 파이프라인이 느려지거나 못 뜸 |

출처: <https://www.digna.ai/why-data-pipelines-fail-production-detect-early>, <https://seattledataguy.substack.com/p/the-5-silent-failures-in-data-pipelines>, <https://learn.microsoft.com/en-us/azure/data-factory/concepts-data-flow-schema-drift>

---

## 4. 변경 관리 (How — KQ4)

### 4.1 데이터 계약(Data Contract)

- 데이터 **생산자(producer)와 소비자(consumer) 사이의 공식 합의**. 구조(스키마)·품질·의미(semantics)·운영 기대(SLO)·소유권을 사람·기계가 모두 읽을 수 있게 명문화. 2021년 Andrew Jones(GoCardless)가 "API 계약"을 데이터에 옮겨 정립.
  - 쉬운 한 줄: "내가 주는 데이터는 **이런 형태·이런 품질·이 시각까지**"라고 만든 쪽이 약속한 계약서. 스키마는 그 일부일 뿐.
  - 출처: <https://andrew-jones.com/data-contracts-101/>, <https://en.wikipedia.org/wiki/Data_contract>, <https://www.selectstar.com/resources/data-contracts>

### 4.2 스키마 진화(Schema Evolution)·호환성 모드

- 시간이 지나며 스키마를 바꾸되 **생산자·소비자가 계속 호환되게** 하는 것.
- **호환성 종류**(Confluent 분류):
  - **Backward(하위호환)**: 새 스키마를 쓰는 소비자가 옛 데이터도 읽음(예: 선택적 필드 추가, 필드 제거) — **정상 경로로 권장**.
  - **Forward(상위호환)**: 옛 스키마 소비자가 새 데이터도 읽음.
  - **Full**: 둘 다(선택적 필드 추가/제거만).
  - **Transitive**: 직전이 아니라 **모든 이전 버전**과 비교 검사.
  - 출처: <https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html>

### 4.3 Breaking change vs. Backward-compatible change

- **Breaking change(깨는 변경)**: 필드 이름 변경, 기본키 변경 등 → **소비자가 깨진다**. 신중한 전략 필요.
- **Backward-compatible(안 깨는 변경)**: 선택적 필드 추가(기본값 제공) 등 → 가벼운 변경. 새 필드엔 항상 기본값을 줘서 옛 데이터도 처리되게.
- **깨는 변경 다루는 패턴**:
  - **Expand-Contract(확장-수축)**: 새 스키마를 옛것과 **나란히** 도입 → 소비자를 새 필드로 이전 → **그 다음에야** 옛것 제거.
  - **버전 분리 스트림(v1/v2 병행)**: 모든 소비자가 옮길 때까지 두 버전을 동시 발행.
- 쉬운 한 줄: "**옛길을 바로 막지 말고, 새길을 먼저 깔고 다 옮긴 뒤 옛길을 닫는다.**"
- 출처: <https://estuary.dev/blog/real-time-schema-evolution/>, <https://www.dataexpert.io/blog/backward-compatibility-schema-evolution-guide>, <https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ads.5-ensure-backwards-compatibility-for-data-store-and-schema-changes.html>

### 4.4 변경 승인 프로세스 + 다운스트림 영향 검토

- 스키마/API/제공방식을 바꿀 때 **누가 이 데이터를 쓰는지(다운스트림) 먼저 확인 → 영향 검토 → 사전 공지 → 승인**. 현대 파이프라인은 시스템·도구·프로세스 간 의존이 복잡해 한 곳의 변경이 **연쇄적으로 깨질 수 있다.**
  - 출처: <https://www.getdbt.com/blog/data-sla-challenges-guide>, <https://medium.com/@bhagyarana80/data-contracts-9-versioning-rules-that-end-schema-wars-ac58badddc2c>
- (영향 "어디로 가나" 추적은 C-3 Lineage 도구가 보조 — F-1은 그 정보를 받아 통제·공지하는 절차를 맡는다.)

---

## 5. 운영 대상 선정·중요도 차등 (When/KQ1 — Tiering)

- 모든 파이프라인을 똑같이 운영하지 않는다. **중요도(criticality)에 따라 등급(Tier)을 매기고** 운영 강도(SLA·당직·테스트·복구속도)를 차등. 서비스 티어링은 회복력·SLA 보증·위험완화의 토대로, 자원을 등급순으로 배분한다.
  - 출처: <https://www.linkedin.com/pulse/service-criticality-tiers-standard-architecture-sherif-samy>
- **런북·복구도 티어별로 다르게**: 상위 티어는 더 빠른 복구(짧은 RTO)·더 엄격한 검증, 하위 티어는 느슨하게.
  - 출처: <https://cutover.com/blog/prescriptive-guidance-automated-runbooks-structuring-for-application-tiering-criticality>
- 제조 맥락 등급 예시(가이드 작성용 — 단정 금지, 본보기):
  - **Tier 1(미션 크리티컬)**: AI 서비스·RAG가 직접 먹는 핵심 흐름, 생산·품질 의사결정 입력 → 24/7 당직·최단 RTO·변경 시 풀 승인.
  - **Tier 2(중요)**: 정기 리포팅·대시보드 핵심 → 업무시간 대응.
  - **Tier 3(보조)**: 탐색·실험·내부 분석 → 베스트에포트.
- 쉬운 한 줄: "**AI·핵심 보고가 먹는 라인은 빡세게, 실험용 라인은 느슨하게.**"

---

## 6. 역할·책임(RACI) (How — KQ들 가로지름)

RACI = **R**esponsible(실행)·**A**ccountable(최종책임)·**C**onsulted(자문)·**I**nformed(통지).

| 역할 | 쉬운 설명 | 전형적 책임(F-1 맥락) |
|---|---|---|
| 데이터 엔지니어 | 파이프라인을 실제 만들고 고치는 사람 | 실행·복구·변경 구현(R) |
| 플랫폼/DataOps 담당 | 도구·인프라 운영, 장애 시 원인 짚는 사람 | 도구·환경 운영(R/C), 인프라 건강 |
| 데이터 오너(Owner) | 그 데이터의 의미·적정사용·품질기준의 **업무 책임자** | 변경 승인·우선순위·기준 결정(A) |
| 다운스트림 소비자(AI팀·분석팀) | 데이터를 받아 쓰는 쪽("어떻게 만들어지는지는 모름") | 변경·장애 시 **통지 대상(I)**, 영향 시 자문(C) |

- 핵심 메시지: "**데이터 품질·신뢰성은 한 역할이 못 가진다 — 팀 스포츠.**" RACI로 누가 R/A/C/I인지 못박아야 거버넌스 병목을 막는다.
- 출처: <https://www.pantomath.com/blog/data-quality-roles-and-responsibilities-the-data-reliability-raci>, <https://www.metaplane.dev/blog/raci-for-data-quality>

---

## 7. 현업 실행 키트 재료 (항목·예시값 — 제조 맥락)

### 7.1 운영 대상 파이프라인 등록표 (항목 사전)

| 항목 | 쉬운 의미 | 예시값(제조) | 필수/선택 | 작성 주체 |
|---|---|---|---|---|
| 파이프라인명 | 무엇을 나르는 라인인가 | `설비센서_시간집계` | 필수 | 데이터 엔지니어 |
| 소스 → 타깃 | 어디서 받아 어디로 | `MES DB → 분석 웨어하우스` | 필수 | 데이터 엔지니어 |
| 스케줄 | 언제·얼마나 자주 도나 | `매시 정각`, `일 1회 02:00` | 필수 | 데이터 엔지니어 |
| 중요도 등급(Tier) | 얼마나 빡세게 운영 | `Tier 1` | 필수 | 데이터 오너 |
| 데이터 오너 | 업무 책임자 | `생산기술팀 ○○○` | 필수 | 거버넌스 |
| SLA(신선도/완료시각) | 언제까지·얼마나 최신 | `매일 08:00까지, 1시간 이내` | 필수 | 오너+엔지니어 |
| 알림 대상 | 멈추면 누구에게 | `데이터엔지니어 당직, AI팀 채널` | 필수 | 플랫폼 담당 |
| 다운스트림 소비자 | 누가 쓰나(변경 시 통지처) | `예지정비 모델, 품질 대시보드` | 필수 | 데이터 오너 |
| 런북 링크 | 장애 시 대응 절차서 | `runbook/센서집계.md` | 권장 | 데이터 엔지니어 |

### 7.2 변경 사전 공지문(Change Notice) 항목

- 변경 대상(어느 파이프라인·테이블·필드)
- 변경 유형(깨는 변경 / 안 깨는 변경)
- 변경 내용(전 → 후, 예: 필드명 `temp` → `temp_celsius`)
- 영향받는 소비자(다운스트림 목록)
- 적용 예정일·전환 기간(병행 운영 기간)
- 마이그레이션 가이드(소비자가 해야 할 일)
- 담당자·문의처, 승인자
- (근거: data contract·schema evolution·expand-contract 패턴 §4)

### 7.3 Runbook 한 건의 구성 항목

- 트리거(이 알림/증상이 뜨면)
- 영향 범위·심각도(어떤 소비자가 멈추나, Tier)
- 진단 단계(무엇부터 확인 — 소스 도착? 부분적재? 스키마?)
- 복구 조치(재처리 / 롤백 / 우회 — 각 명령·순서)
- 복구 확인(무엇이 보이면 정상)
- 에스컬레이션(언제·누구에게 올림)
- 사후 기록(원인·재발방지, 런북 갱신)
- (근거: SRE runbook·IMAG §3.1)

---

## 8. KQ 1~4 커버리지 매핑

이 자료는 F-1의 4개 Key Question을 다음과 같이 덮는다. **KQ1(운영 대상·중요도)**은 §5 Tiering(criticality tier, 등급별 운영강도)과 §7.1 등록표(중요도 등급·SLA 항목)로 답한다 — "AI·핵심보고가 먹는 라인은 Tier 1로 빡세게". **KQ2(실행·배포 표준화)**는 §2 전체(오케스트레이션/DAG·멱등성·재시도·백필·환경분리·CI/CD·데이터 테스트·버전관리)로 답한다 — 실행 주기·배포 절차·테스트·승인의 표준. **KQ3(장애 복구)**는 §3(런북·on-call·IMAG 3C·재처리/롤백/우회·RTO/RPO·데이터 SLA/SLO·장애 유형)과 §7.3 런북 구성으로 답한다 — 감지(C-1)는 옆 주제, F-1은 받은 장애를 복구. **KQ4(변경 통제)**는 §4(데이터 계약·스키마 진화·호환성 모드·breaking vs compatible·expand-contract·변경 승인·다운스트림 영향검토)와 §7.2 변경 공지문으로 답한다. §1(정의·DevOps 관계·구성요소)·§6(RACI)·§0(인접 경계)은 네 질문을 관통하는 What/관점 토대다.

---

## 참고자료(References) — 분류별 정리

### 정의·개념(권위)
- Gartner — Definition of DataOps: <https://www.gartner.com/en/information-technology/glossary/dataops>
- The DataOps Manifesto: <https://dataopsmanifesto.org/en/>
- Teradata — What is DataOps: <https://www.teradata.com/insights/data-platform/what-is-dataops>
- IBM — What is DataOps: <https://www.ibm.com/think/topics/dataops>
- Astronomer — What is DataOps: <https://www.astronomer.io/what-is-dataops/>
- Informatica — Understanding DataOps: <https://www.informatica.com/resources/articles/understanding-dataops.html>

### 실행·배포(멱등성·DAG·CI/CD·테스트)
- Databricks — What is a DAG: <https://www.databricks.com/blog/what-is-dag>
- Airbyte — Idempotency in data pipelines: <https://airbyte.com/data-engineering-resources/idempotency-in-data-pipelines>
- ml4devs — Backfilling historical data with idempotent pipelines: <https://www.ml4devs.com/what-is/backfilling-data/>
- thedataops.org — Backfill: <https://www.thedataops.org/backfill/>
- abstractalgorithms — DAG scheduling, retries, recovery: <https://www.abstractalgorithms.dev/data-pipeline-orchestration-pattern-dag-retries-and-recovery>
- datadriven.io — Airflow DAG reference: <https://datadriven.io/tools/airflow-dag>
- dbt — Set up CI: <https://docs.getdbt.com/guides/set-up-ci>
- Datacoves — dbt test options: <https://datacoves.com/post/dbt-test-options>
- Monte Carlo — dbt testing: <https://montecarlo.ai/blog-what-is-dbt-testing-definition-best-practices-and-more>

### 장애·복구·SRE·SLA
- Google SRE — Emergency response: <https://sre.google/sre-book/emergency-response/>
- Google SRE — Incident management guide: <https://sre.google/resources/practices-and-processes/incident-management-guide/>
- Google SRE — Being on-call: <https://sre.google/workbook/on-call/>
- Google SRE — Data processing pipelines: <https://sre.google/workbook/data-processing/>
- Emmer.dev — Incident runbook template: <https://emmer.dev/blog/an-effective-incident-runbook-template/>
- dbt — Data SLAs best practices: <https://www.getdbt.com/blog/data-slas-best-practices>
- Chronosphere — SLA vs SLO vs SLI: <https://chronosphere.io/learn/know-the-sre-fundamentals-differences-between-sli-vs-slo-vs-sla/>
- LaunchDarkly — RTO vs RPO: <https://launchdarkly.com/blog/rto-vs-rpo/>
- Data Systems Authority — DR planning RTO/RPO: <https://datasystemsauthority.com/data-systems-disaster-recovery-planning>
- USPTO — Rollback recovery with data lineage: <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11556431>
- Meegle — ETL pipeline RPO: <https://www.meegle.com/en_us/topics/etl-pipeline/etl-pipeline-recovery-point-objectives>

### 장애 유형
- digna.ai — Why data pipelines fail: <https://www.digna.ai/why-data-pipelines-fail-production-detect-early>
- Seattle Data Guy — 5 silent failures: <https://seattledataguy.substack.com/p/the-5-silent-failures-in-data-pipelines>
- Microsoft Learn — Schema drift: <https://learn.microsoft.com/en-us/azure/data-factory/concepts-data-flow-schema-drift>

### 변경 관리·데이터 계약·스키마 진화
- Andrew Jones — Data Contracts 101: <https://andrew-jones.com/data-contracts-101/>
- Wikipedia — Data contract: <https://en.wikipedia.org/wiki/Data_contract>
- Select Star — Guide to data contracts: <https://www.selectstar.com/resources/data-contracts>
- Confluent — Schema evolution & compatibility types: <https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html>
- Estuary — Real-time schema evolution: <https://estuary.dev/blog/real-time-schema-evolution/>
- dataexpert.io — Backward compatibility schema evolution: <https://www.dataexpert.io/blog/backward-compatibility-schema-evolution-guide>
- AWS DevOps Guidance — Backwards compatibility for schema changes: <https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ads.5-ensure-backwards-compatibility-for-data-store-and-schema-changes.html>
- dbt — Data SLA challenges: <https://www.getdbt.com/blog/data-sla-challenges-guide>

### 중요도 티어링·RACI
- LinkedIn(Sherif Samy) — Service criticality tiers: <https://www.linkedin.com/pulse/service-criticality-tiers-standard-architecture-sherif-samy>
- Cutover — Runbooks by tier & criticality: <https://cutover.com/blog/prescriptive-guidance-automated-runbooks-structuring-for-application-tiering-criticality>
- Pantomath — Data reliability RACI: <https://www.pantomath.com/blog/data-quality-roles-and-responsibilities-the-data-reliability-raci>
- Metaplane — RACI for data quality: <https://www.metaplane.dev/blog/raci-for-data-quality>
