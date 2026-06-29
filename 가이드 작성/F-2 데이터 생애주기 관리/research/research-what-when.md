# F-2 데이터 생애주기 관리 — What·When 리서치 메모

> 작성일: 2026-06-26 | 클러스터: What(무엇인가·무엇을 갖추나) + When(어디부터 하나)
> 이 파일은 가이드 작성자가 KQ별로 재료를 바로 쓸 수 있도록 정리한 1차 조사 메모다.

---

## 목차

1. [생애주기 단계 모델 (KQ1)](#1-생애주기-단계-모델)
2. [단계별 역할·책임 (KQ1)](#2-단계별-역할·책임)
3. [보존 기간 결정 기준 (KQ2)](#3-보존-기간-결정-기준)
4. [제조업·한국 법령별 보존 연한 (KQ2)](#4-제조업한국-법령별-보존-연한)
5. [과정 데이터 보존 판단 (KQ3)](#5-과정-데이터-보존-판단)
6. [아카이빙 vs 폐기 절차 (KQ4)](#6-아카이빙-vs-폐기-절차)
7. [저장소 계층화 (KQ5)](#7-저장소-계층화)
8. [현업 실행 키트 재료 (KQ1~5 공통)](#8-현업-실행-키트-재료)
9. [출처 목록](#9-출처-목록)

---

## 1. 생애주기 단계 모델

**사용처: KQ1 · What 섹션 "단계 정의"**

### 1-1. 주요 표준·프레임워크 비교

| 프레임워크 | 단계 수 | 단계 명칭 |
|---|---|---|
| DAMA-DMBOK (6단계) | 6 | 생성(Creation) → 저장(Storage) → 사용(Usage) → 공유(Sharing) → 아카이빙(Archiving) → 파기(Destruction) |
| 확장 8단계 모델 | 8 | 생성(Creation) → 수집(Collection) → 저장(Storage) → 처리(Processing) → 분석(Analysis) → 공유(Sharing) → 아카이빙(Archiving) → 파기(Destruction) |
| ITGOV 4단계 정책 모델 | 4 | 생성(Genesis) → 사용(Active Life) → 아카이빙(Long-Term Store) → 삭제(Deletion) |

**현업 적용 권장:** DAMA-DMBOK 6단계를 기본으로 하되, 제조 현장에 맞게 "생성/수집 → 사용(Active) → 보관(Inactive) → 아카이빙 → 폐기"로 단순화하고 **재사용 루프**를 추가한다.

### 1-2. 단계별 정의 (가이드 작성용)

| 단계 | 영문 | 정의 | 제조 현장 예시(두산퓨얼셀 맥락, 가상) |
|---|---|---|---|
| **생성·수집** | Creation / Capture | 시스템·센서·사람이 데이터를 최초 만들거나 외부에서 받아들이는 순간 | 스택 성능시험 센서 로그 수신, 검사원이 외관 불량 기록 입력 |
| **사용(Active)** | Active Use | 업무 분석·AI 학습·보고·실시간 의사결정에 활발히 쓰이는 기간 | 셀 제조 데이터로 수율 분석, AI 모델 학습에 성능시험 로그 활용 |
| **보관(Inactive)** | Retention | 일상적 사용은 줄었지만 규정·재사용·감사를 위해 보관하는 기간 | 출하 품질 성적서를 3년 보관(고객 클레임 대비) |
| **아카이빙** | Archiving | 저비용 저장소로 옮기되 필요 시 복원 가능한 상태로 장기 보존 | 내구 시험 로그를 콜드 스토리지로 이전, 규제 감사 시 복원 가능 |
| **폐기** | Disposal / Deletion | 보존 기간 만료·더 이상 가치 없음을 확인 후 안전하게 삭제 | 채용 탈락자 이력서 6개월 후 삭제, 구형 공정 파라미터 파기 |
| **재사용 루프** | Reuse | 아카이브된 데이터를 새 AI 학습·규제 감사·신제품 개발에 재활용 | 과거 불합격 셀 데이터로 새 불량 탐지 모델 재학습 |

> 출처: DAMA-DMBOK 개요([[1]](#ref1)), Agility-at-Scale DLM for AI([[2]](#ref2)), ITGOV DLM Policy([[3]](#ref3)), Risolv DLM([[4]](#ref4))

---

## 2. 단계별 역할·책임

**사용처: KQ1 · What 섹션 "단계별 책임자·관리 기준"**

### 2-1. 3대 역할 정의

| 역할 | 영문 | 위치 | 생애주기에서 하는 일 |
|---|---|---|---|
| **데이터 오너** | Data Owner | 임원급 비즈니스 리더 (예: 제조본부장, 품질담당 임원) | 데이터 도메인의 보존 기간·분류 등급·접근 정책 결정·예산 승인 |
| **데이터 스튜어드** | Data Steward | 실무 담당자 (예: 품질관리팀 담당자, 데이터 거버넌스 팀) | 생성 시 메타데이터·분류 적용, 품질 규칙 유지, 보존 정책 준수 점검, 아카이빙·폐기 실행 조정 |
| **데이터 커스터디언** | Data Custodian | IT/인프라 엔지니어 | 스토리지 계층 이동 자동화, 접근 권한 설정, 암호화·백업, 실제 폐기 실행 |

### 2-2. 단계별 RACI 스케치 (가이드 작성 참고용)

| 단계 | 오너(Accountable) | 스튜어드(Responsible) | 커스터디언(Responsible) | 법무·컴플라이언스(Consulted) |
|---|---|---|---|---|
| 생성·수집 | 도메인 오너 | 메타데이터 등록 | 시스템 연동 | — |
| 사용 | 도메인 오너 | 품질 점검 | 접근권한 관리 | — |
| 보관 결정 | 도메인 오너 | 보존 기간 검토 | 스토리지 할당 | 규제 요건 확인 |
| 아카이빙 | 도메인 오너 | 아카이빙 판단 | 계층 이동 실행 | — |
| 폐기 | 도메인 오너 | 폐기 대상 확인 | 안전 삭제 실행 | 법적 보존 여부 최종 확인 |

> 출처: Data Governor 역할 정의([[5]](#ref5)), Agility-at-Scale DLM([[2]](#ref2))

---

## 3. 보존 기간 결정 기준

**사용처: KQ2 · What/When 섹션 "보존 기간 결정 5가지 기준"**

### 3-1. 5대 결정 기준

| 기준 | 설명 | 제조 현장 예 |
|---|---|---|
| **① 법적·규제 의무** | 법령이 최소 보존 기간을 강제함(→ 이 이상은 반드시 보관) | 상법: 회계장부 10년, 세법: 세금계산서 5년, 근로기준법: 임금대장 3년 |
| **② 업무 재사용 가치** | 실제 업무·분석에 다시 쓸 가능성(자주 참조 vs 거의 안 씀) | 현재 생산 중인 모델 품질 성적서: 높음 / 단종 10년 전 모델 데이터: 낮음 |
| **③ AI 학습 가치** | 모델 재학습·이상 탐지·희소 사례 학습에 필요한 역사 깊이 | AI 예측 모델은 12~24개월 이상 센서 이력이 필요, 3~5년 초과 시 한계 수익 체감 |
| **④ 감사 필요성** | 내부감사·외부인증·고객 감사 시 소환 가능성 | ISO 9001 심사, 고객 클레임 소명, 산업부 검사 등 |
| **⑤ 저장 비용·위험** | 보관 비용 vs 삭제 리스크(규정 위반·재발급 불가) 트레이드오프 | 고주파 센서 원시 데이터: 용량 크고 비용 높음 → 다운샘플링 후 보관 검토 |

**실무 원칙:** "법적 의무가 있으면 무조건 보관, 없으면 비용·가치 기준으로 결정한다."

> 출처: GRM Document Management Retention Guide([[6]](#ref6)), SecureFrame Retention Policy([[7]](#ref7)), Oxmaint IIoT Retention Guide([[8]](#ref8))

### 3-2. 보존 기간 결정 흐름 (가이드 다이어그램 재료)

```
데이터 유형 식별
    ↓
법적 의무 있음? → YES → 법정 연한 이상 보관 (예외 없음)
    ↓ NO
업무 재사용 가치 높음? → YES → 비용 대비 보관 기간 설정
    ↓ NO
AI 학습 가치 있음? → YES → 최소 12~24개월 보관
    ↓ NO
감사 가능성 있음? → YES → 감사 주기 기준 보관
    ↓ NO
→ 폐기 대상으로 분류
```

---

## 4. 제조업·한국 법령별 보존 연한

**사용처: KQ2 · 보존 기간 표준값 목록 (현업 실행 키트 ㉢)**

### 4-1. 한국 법령 기준 (제조업 관련)

| 문서·데이터 유형 | 보존 기간 | 근거 법령 |
|---|---|---|
| 회계장부·재무제표·주주총회 의사록 | **10년** | 상법 제33조 |
| 세금계산서·영수증·거래 기록 | **5년** | 국세기본법·법인세법 |
| 임금대장·채용·해고·근로계약서 | **3년** (퇴직 후) | 근로기준법 |
| 전표·유사 서류 | **5년** | 상법 제33조 |
| 채용 탈락자 이력서 | **14~180일** (채용 결정 후) | 채용절차공정화법 |

> 출처: Cloudike 문서보존기간 총정리([[9]](#ref9)), 상법 제33조([[10]](#ref10))

### 4-2. 국제 품질 표준 기준 (제조업)

| 표준 | 핵심 요건 | 보존 기간 기준 |
|---|---|---|
| **ISO 9001** | 품질 기록 보존 의무 명시 (기간은 조직이 결정) | 자체 결정 (최소 3년 관행) |
| **IATF 16949** (자동차 부품) | 제품 수명 + 1년 (N+1 원칙) | PPAP, 설계·공정 기록, 툴링 기록 등 |
| **OSHA** (미국, 참고) | 유해물질 노출 기록 | 재직 기간 + 30년 |
| **FDA 21 CFR** (의약·식품 참고) | 제조 기록 | 최소 2년 |

**에너지·연료전지 제조 특이사항:** 두산퓨얼셀처럼 발전설비를 납품하는 경우, 고객사의 설비 수명(15~20년)에 맞춰 기술 문서·성능 이력 보존 기간을 연장하는 계약 조건이 붙을 수 있다(고객 요건이 법령 기준 초과 시 고객 요건 우선). 확인 필요.

> 출처: IATF 16949 Clause 7.5.3.2.1([[11]](#ref11)), ISO 9001 Control of Quality Records([[12]](#ref12)), GRM Retention Guide([[6]](#ref6))

### 4-3. IoT·센서 데이터 보존 권고 (제조 현장)

| 데이터 유형 | 권장 보존 기간 | 저장 계층 |
|---|---|---|
| 고주파 원시 센서 데이터 (Raw) | **7~30일** (엣지 보관) | Hot (엣지/온프렘) |
| 집계 데이터 (시간·일 평균 등) | **90일~1년** | Hot → Warm |
| AI 예측 모델 학습용 이력 | **12~24개월** | Warm |
| 품질·OEE 기록 (규제 감사용) | **5~10년** | Cold / Archive |
| 사고·이상 이벤트 데이터 | **2~7년** (사건별) | Cold (별도 포렌식 저장소) |

> 비고: 3~5년 초과 트렌드 데이터는 AI 정확도 한계 수익 체감 — 비용 대비 효과 재검토 권장.

> 출처: Oxmaint Industrial IoT Retention Guide([[8]](#ref8))

---

## 5. 과정 데이터 보존 판단

**사용처: KQ3 · "중간 과정 데이터를 어떻게 관리할 것인가" 섹션**

### 5-1. 왜 과정 데이터가 AI에 중요한가

- 최종 합격품 데이터만으로 학습한 AI는 **불량·이상을 인식하지 못한다** — 실패 사례 없이 실패 탐지 불가.
- 설계 실험(DoE)의 **실패 조건 데이터까지 포함**해야 대표성 있는 모델을 만들 수 있다.
- 제조 특성상 불량품은 희소(드물다) → 불합격 데이터가 오히려 희귀·고가치 학습 자산이다.
- 계측 오류 등으로 데이터를 제외할 경우에도 **제외 이유를 메타데이터로 보존**해야 한다 (Audit Trail).

> 출처: BioPharm International, AI in Drug Manufacturing([[13]](#ref13)), Quality Magazine, Why AI in Manufacturing Fails([[14]](#ref14))

### 5-2. 보존할 과정 데이터 유형 (제조 현장)

| 과정 데이터 유형 | AI 재사용 가치 | 보존 권장 |
|---|---|---|
| 불합격·불량 제품 검사 기록 | 매우 높음 (희소 사례, 불량 탐지 학습) | **보존** — 별도 라벨로 분류 |
| 실패한 공정 파라미터 실험 기록 | 높음 (파라미터 최적화 모델) | **보존** — 실패 이유 메타데이터 포함 |
| 중간 검사 결과 (최종 합격 전 중간값) | 중간 (공정 흐름 이해) | **보존** — 원시 데이터 또는 집계 |
| 검토 의견·엔지니어 주석 | 중간 (맥락 이해, 지식 자산화) | **선택적 보존** — D-2/D-3 연계 |
| 재작업(Rework) 이력 | 높음 (재작업 패턴 → 원인 분석) | **보존** |
| 단순 중복 원시 센서 로그 | 낮음 | 집계 후 원시 삭제 검토 |

### 5-3. 과정 데이터 보존 판단 기준 (가이드 다이어그램 재료)

> **판단 질문 3가지:**
> 1. 이 데이터로 AI가 "다음에 같은 실패를 예측"할 수 있는가?
> 2. 이 데이터가 다른 곳에서 재현·재생성이 가능한가? (가능하면 삭제 후보)
> 3. 규제 감사나 고객 클레임 시 소명에 필요한가?
>
> 3가지 중 하나라도 YES → 보존 (분류만 달리하여 적절한 계층으로)

---

## 6. 아카이빙 vs 폐기 절차

**사용처: KQ4 · "폐기와 아카이빙을 어떻게 수행할 것인가" 섹션**

### 6-1. 핵심 구분

| 항목 | 아카이빙 | 폐기(삭제) |
|---|---|---|
| 정의 | 저비용 저장소로 이동, 복원 가능 | 완전하고 안전한 삭제, 복원 불가 |
| 목적 | 규제 보존·미래 재사용·감사 대비 | 비용 절감·개인정보 위험 제거 |
| 접근성 | 느림 (수 시간~수 일) | 해당 없음 (삭제됨) |
| 전제 조건 | 아직 보존 의무 있음 | 보존 기간 만료 + 법적 보존 대상 아님 |
| 검색·감사 | 인덱싱·풀텍스트 검색 가능 (Enterprise Archive) | 파기 증적만 남김 |

### 6-2. 법적 보존(Legal Hold) 개념

- **법적 보존(Legal Hold / Litigation Hold):** 소송·규제 조사·내부 감사가 예상될 때, 정상적 폐기 절차를 **중단**하고 관련 데이터를 보존하는 법적 의무.
- 법무팀이 "보존 명령(Hold Notice)"을 발행 → IT·데이터팀이 해당 데이터 자동 삭제 루틴 일시 정지.
- 법적 보존 대상 데이터는 **보존 기간이 만료되어도 삭제 불가**.
- 위반 시 증거 인멸로 간주 → 법원 제재·벌금·패소 판결 위험.

> 출처: OpenText Legal Hold([[15]](#ref15)), Everlaw Data Preservation([[16]](#ref16)), Archon Enterprise Archiving([[17]](#ref17))

### 6-3. 폐기 절차

| 단계 | 내용 |
|---|---|
| 1. 보존 만료 확인 | 보존 일정표(Retention Schedule)의 보존 기간 도달 여부 확인 |
| 2. 법적 보존 여부 검토 | Legal Hold 대상인지 법무팀 확인 (해당 시 폐기 금지) |
| 3. 오너 승인 | 데이터 오너 최종 승인 |
| 4. 안전 삭제 실행 | 전자: 보안 와이핑(Secure Wipe)·암호화 키 삭제 / 물리: 파쇄 |
| 5. 파기 증적 기록 | 언제·무엇을·어떻게 삭제했는지 감사 로그 보존 (규제 증적) |

### 6-4. 데이터 3분류 (처리 방향 결정)

| 분류 | 기준 | 처리 방향 |
|---|---|---|
| **법적 보존 대상** | 규제·계약·소송 보존 의무 | 폐기 금지, 아카이빙 (Enterprise Archive) |
| **업무·AI 재사용 대상** | 보존 가치 있고 접근 가능해야 함 | 계층 이동 (Warm/Cold), 인덱싱 유지 |
| **폐기 대상** | 보존 기간 만료, 재사용 가치 없음, 법적 의무 없음 | 안전 삭제 + 파기 증적 |

---

## 7. 저장소 계층화

**사용처: KQ5 · "저장 비용과 리스크를 어떻게 통제할 것인가" 섹션**

### 7-1. 4계층 아키텍처

| 계층 | 별칭 | 접근 빈도 | 응답 속도 | 비용 | 주요 용도 |
|---|---|---|---|---|---|
| **Hot** | Tier 1 (Active) | 매일~수시 | 밀리초~초 | 가장 높음 | 실시간 분석, AI 학습 중인 데이터, 운영 대시보드 |
| **Warm** | Tier 2 (Managed) | 월 1~수 회 | 초~분 | 중간 | 최근 1~7년 규제 데이터, 간헐적 조회 |
| **Cold** | Tier 3 (Deep Cold) | 연 1회 이하 | 수 시간 | 매우 낮음 | 7년 초과 장기 보존, 법적 의무 데이터 |
| **Archive** | Tier 4 (Disposition) | 거의 없음→자동 삭제 | 해당 없음 | 최저 | 보존 만료 후 자동 파기 대기 또는 파기 완료 증적 |

> 클라우드 예: Hot = S3 Standard / Azure Hot, Warm = S3 Standard-IA / Azure Cool, Cold = S3 Glacier / Azure Archive

### 7-2. 자동 계층 이동(Auto-Tiering) 원리

- 데이터가 **N일 동안 접근되지 않으면** 자동으로 다음 계층으로 이동.
- 예시 정책: Hot 90일 미접근 → Warm, Warm 1년 미접근 → Cold, Cold 7년 도달 → 파기 검토.
- 이동 전 압축(Compression)·중복 제거(Deduplication)·컬럼형 변환으로 용량 축소.
- **이동 기준은 접근 빈도 + 생성일자 조합**으로 설정.

### 7-3. 비용 절감 효과 (참고 수치, 실제는 클라우드·온프렘 환경마다 다름)

- Hot에서 Cold로 이동 시 GB당 비용이 약 1/10~1/20 수준으로 줄어드는 것이 일반적 (확인 필요, 클라우드 사업자별 상이).
- 3년 기준 전체 운영 비용은 Enterprise Archive 플랫폼이 콜드 스토리지 단독보다 거버넌스 비용 포함 시 오히려 유리한 경우 있음.

> 출처: Archon Storage Tiering([[18]](#ref18)), Archon Enterprise vs Cold Storage([[17]](#ref17)), Azure Storage Tiers([[19]](#ref19)), AWS IoT SiteWise Data Storage([[20]](#ref20))

---

## 8. 현업 실행 키트 재료

**사용처: What/How 섹션 "항목 사전·표준값·템플릿" (현업 실행 키트 ㉠㉢㉣)**

### 8-1. ㉠ 보존 정책 항목 사전 (Retention Schedule 열 정의)

| 항목명 | 쉬운 의미 | 예시값 (두산퓨얼셀 맥락, 가상) | 필수/선택 | 작성 주체 |
|---|---|---|---|---|
| **데이터 유형** | 어떤 종류의 데이터인가 | 스택 성능시험 데이터 / 셀 외관검사 기록 / 품질 성적서 | 필수 | 데이터 오너 |
| **보존 기간** | 얼마나 오래 보관하나 | 5년 / 제품 수명+1년 / 무기한 | 필수 | 데이터 오너 (법무 검토) |
| **보존 근거** | 왜 이 기간인가 | 세법(국세기본법) / 고객 계약 / ISO 9001 / AI 재사용 가치 | 필수 | 데이터 오너·법무 |
| **보관 위치** | 어디에 저장하나 | MES 데이터베이스 / S3 Glacier / 사내 아카이브 서버 | 필수 | 데이터 커스터디언 |
| **보관 등급** | Hot/Warm/Cold 중 어디인가 | Hot (0~1년) → Warm (1~5년) → Cold (5년+) | 필수 | 데이터 커스터디언 |
| **폐기 방식** | 어떻게 지우나 | 보안 와이핑 / 암호화 키 삭제 / 물리 파쇄 | 필수 | 데이터 커스터디언 |
| **법적 보존 여부** | 소송·감사 시 삭제 금지인가 | Y / N / 조건부 | 필수 | 법무팀 |
| **데이터 오너** | 최종 책임자 | 품질보증팀장 / 제조기술팀장 | 필수 | 거버넌스 위원회 |
| **검토 주기** | 보존 정책을 언제 다시 확인하나 | 연 1회 / 계약 갱신 시 | 선택 | 데이터 스튜어드 |
| **과정 데이터 여부** | 최종 결과가 아닌 중간 과정 데이터인가 | Y (불합격 기록) / N (최종 성적서) | 선택 | 데이터 스튜어드 |

### 8-2. ㉢ 표준값 목록 (고르는 허용값)

**보관 등급 (Storage Tier)**
- Hot / Warm / Cold / Archive

**폐기 방식**
- 보안 와이핑(Secure Wipe) / 암호화 키 삭제(Crypto-Erase) / 물리 파쇄 / 클라우드 삭제 API

**보존 근거 유형**
- 법적 의무 / 고객 계약 / 내부 정책 / AI 학습 가치 / 업무 재사용 가치 / 감사 필요성

**법적 보존 상태**
- 정상(Normal) / 법적 보존(Legal Hold) / 폐기 예정(Scheduled for Disposal) / 폐기 완료(Disposed)

### 8-3. ㉣ 빈 보존 정책 표 양식 (가이드에 삽입용)

```
| 데이터 유형 | 보존 기간 | 보존 근거 | 보관 등급 | 폐기 방식 | 법적보존 | 데이터 오너 |
|---|---|---|---|---|---|---|
| (예) 스택 성능시험 원시 로그 | 2년 | AI 학습 가치 | Hot→Warm | 보안 와이핑 | N | 제조기술팀장 |
| (예) 셀 외관검사 성적서 | 5년 | 국세기본법 | Warm→Cold | 보안 와이핑 | N | 품질보증팀장 |
| (예) 불합격 셀 분석 기록 | 7년 | AI 학습+감사 | Cold | 보안 와이핑 | 조건부 | 품질보증팀장 |
| (예) 내구시험 장기 로그 | 제품수명+1년 | IATF/고객계약 | Archive | 보안 와이핑 | Y | 제조기술팀장 |
```

> 비고: 두산퓨얼셀 맥락 예시값은 가상(실제 법무·품질팀 검토 필수).

---

## 9. 출처 목록

<a id="ref1"></a>**[1]** DAMA-DMBOK Data Lifecycle Overview — Risolv Consulting: https://www.risolv.me/understanding-the-flow-of-information-through-data-lifecycle-management/

<a id="ref2"></a>**[2]** Data Lifecycle Management for AI: Stages, Governance — Agility at Scale: https://agility-at-scale.com/ai/data/data-lifecycle-management/

<a id="ref3"></a>**[3]** Data Lifecycle Management Policy (creation → usage → archival → deletion) — ITGOV Docs: https://www.itgov-docs.com/blogs/data-governance/6-data-lifecycle-management-policy-creation-usage-archival-deletion

<a id="ref4"></a>**[4]** Understanding the Flow of Information through Data Lifecycle Management — Risolv: https://www.risolv.me/understanding-the-flow-of-information-through-data-lifecycle-management/

<a id="ref5"></a>**[5]** Data Steward vs Data Owner vs Data Custodian — The Data Governor: https://thedatagovernor.com/data-steward-vs-data-owner-vs-data-custodian/

<a id="ref6"></a>**[6]** Business Records Retention Guide by Industry — GRM Document Management: https://www.grmdocumentmanagement.com/blog/business-records-retention-guide/

<a id="ref7"></a>**[7]** Creating a Data Retention Policy: Examples, Best Practices & Template — SecureFrame: https://secureframe.com/blog/data-retention-policy

<a id="ref8"></a>**[8]** Industrial IoT Data Storage: How Long Should You Keep Sensor Data? — Oxmaint: https://oxmaint.com/blog/post/industrial-iot-data-storage-how-long-keep-sensor-data

<a id="ref9"></a>**[9]** 2026년 대비 회사 문서 보존기간 총정리 — Cloudike: https://cloudike.kr/blog/%EA%B3%BC%ED%83%9C%EB%A3%8C-%ED%8F%AD%ED%83%84-%ED%94%BC%ED%95%98%EA%B8%B0-2026%EB%85%84-%EB%8C%80%EB%B9%84-%ED%9A%8C%EC%82%AC-%EB%AC%B8%EC%84%9C-%EB%B3%B4%EC%A1%B4%EA%B8%B0%EA%B0%84-%EC%B4%9D/

<a id="ref10"></a>**[10]** 상법 제33조 (상업장부등의 보존) — CaseNote: https://casenote.kr/%EB%B2%95%EB%A0%B9/%EC%83%81%EB%B2%95/%EC%A0%9C33%EC%A1%B0

<a id="ref11"></a>**[11]** IATF 16949:2016 Clause 7.5.3.2.1 Record Retention — Pretesh Biswas: https://preteshbiswas.com/2023/07/13/iatf-169492016-clause-7-5-3-2-1-record-retention/

<a id="ref12"></a>**[12]** ISO 9001 Control and Retention of Quality Records Procedure — BPR Hub: https://www.bprhub.com/blogs/iso-9001-quality-record-retention-procedure

<a id="ref13"></a>**[13]** Building a Strong Data Foundation for AI in Drug Manufacturing — BioPharm International: https://www.biopharminternational.com/view/data-foundation-ai-drug-manufacturing

<a id="ref14"></a>**[14]** Why AI in Manufacturing Fails Without Quality Data — Quality Magazine: https://www.qualitymag.com/articles/99678-why-ai-in-manufacturing-fails-without-quality-data

<a id="ref15"></a>**[15]** What is Litigation Hold? Legal Requirements & Solutions — OpenText: https://www.opentext.com/what-is/legal-hold

<a id="ref16"></a>**[16]** Data Preservation and Legal Holds — Everlaw: https://www.everlaw.com/guides/the-everlaw-guide-to-ediscovery/data-preservation-and-legal-holds/

<a id="ref17"></a>**[17]** Enterprise Data Archiving vs. Cold Storage — Archon Data Store: https://www.archondatastore.com/blog/enterprise-data-archiving-vs-cold-storage/

<a id="ref18"></a>**[18]** Exploring Storage and Data Tiering: Concepts, Models & Solutions — Archon: https://www.archondatastore.com/blog/storage-tiering-and-data-tiering/

<a id="ref19"></a>**[19]** Exploring Azure Storage Tiers: Hot, Cool, and Archive — CertLibrary: https://www.certlibrary.com/blog/exploring-azure-storage-tiers-hot-cool-and-archive-explained/

<a id="ref20"></a>**[20]** Hot, Warm, and Cold data paths with IoT on Azure — Microsoft Tech Community: https://techcommunity.microsoft.com/blog/fasttrackforazureblog/hot-warm-and-cold-data-paths-with-iot-on-azure/2336035

---

*이 메모는 리서치 1차 조사본이다. 가이드 작성 시 각 출처 URL 접속 재확인 권장.*
