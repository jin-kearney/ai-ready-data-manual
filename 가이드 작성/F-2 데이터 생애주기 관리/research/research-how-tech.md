# F-2 데이터 생애주기 관리 — How·Tech Stack 리서치 재료

> 작성일: 2026-06-26  
> 용도: F-2 가이드의 How(구축·운영 절차)·Tech Stack(솔루션 검토) 섹션 초안 재료  
> 관점: 데이터 준비 관점 고정 — AI가 쓸 데이터를 "쓸 건 남기고 안 쓸 건 정리"하는 체계

---

## 1. How — 구축·운영 절차 재료

### 1-1. 구축 절차 (5단계)

**[How — 구축 절차 섹션에 쓰임]**

생애주기 관리 구축의 핵심 단계는 다음과 같다. 각 단계에서 역할을 명확히 나눠야 자동화가 작동한다.

| 단계 | 내용 | 주요 역할(RACI 개념) |
|------|------|-------------------|
| ① 생애주기 단계 정의 | 데이터가 거치는 단계(활성→비활성→아카이빙→폐기) 및 각 단계 기준 명문화 | 데이터 오너(Accountable), 거버넌스위원회(Consulted) |
| ② 데이터 유형별 보존 기간 수립 | 데이터 유형·법적 요건 따라 보존 연한(Retention Schedule) 정의 | 법무·컴플라이언스(Consulted), 데이터 오너(Responsible), IT(Informed) |
| ③ 정책 엔진 설정 | 스토리지 또는 거버넌스 도구에 자동 규칙(티어 전환·만료 삭제) 입력 | IT·데이터 엔지니어(Responsible), 거버넌스(Accountable) |
| ④ 폐기·아카이빙 절차 수립 | 폐기 승인 워크플로우, 복원(Restore) 절차, 법적 보존(Legal Hold) 적용 방법 | 법무(Accountable), 데이터 오너(Responsible), IT(Responsible) |
| ⑤ 과정 데이터 보존 규칙 | AI 학습·검증에 쓰인 원시 데이터·전처리 이력 별도 보존 기간 설정 | 데이터 오너·AI팀(Responsible), 거버넌스(Accountable) |

**역할 분리 요약:**
- **데이터 오너**: 어떤 데이터를 얼마나 보존할지 결정 (비즈니스 판단)
- **거버넌스위원회**: 전사 정책 승인·예외 심의
- **법무·컴플라이언스**: 법적 보존 의무·산업 규제 요건 제시
- **IT·엔지니어**: 자동화 정책 설정·기술 실행
- **현업(제조부서)**: 데이터 발생·활용 맥락 제공

---

### 1-2. 제조업 데이터 유형별 보존 기간 기준

**[How — 보존 일정(Retention Schedule) 항목 사전에 쓰임]**

다음은 제조업(특히 에너지·연료전지·산업기기) 환경에서 참고할 수 있는 보존 기간 기준이다.  
**주의: 국내 법령·사내 정책·감사 요건에 따라 달라지므로 반드시 법무 검토 필요.**

| 데이터 유형 | 보존 기간(참고 기준) | 근거 |
|-----------|--------------|------|
| 공정 센서·IoT 원시 데이터 | 5년 이상 | 예측정비·품질 이력 분석 가치, NERC 기준 참고 |
| 제품 품질 검사·배치(Batch) 기록 | 1년(배치 유통기한 후) 또는 3년(배포 후) | FDA cGMP 기준 준용(제조업 일반) |
| 설비·장비 유지보수 기록 | 10년 | 장비 수명·감사 추적 |
| 직원 안전·유해물질 노출 기록 | 재직기간 + 30년 | OSHA 요건 |
| ERP 거래·생산 원가 데이터 | 5~7년 | 세무·감사 요건 |
| AI 학습에 쓰인 원시 데이터·라벨 | AI 모델 운영 기간 + 2~3년 | 모델 재현성·감사 추적 |
| 임시 작업 데이터·로그 | 30~90일 | 활용 완료 후 자동 삭제 |
| 설계도면·제품 사양 | 영구 또는 제품 단종 후 10년 | 제품 책임·지적재산 |

---

### 1-3. 운영 절차 — 폐기·복원·예외 관리

**[How — 운영 소절에 쓰임]**

#### 자동 정책이 처리하는 것

- 일정 기간이 지난 데이터 → 자동으로 저비용 스토리지 계층(Cold/Archive) 이동
- 만료된 데이터 → 자동 삭제(Expiration Action)
- 접근 빈도 기반 자동 계층 전환(Intelligent-Tiering)

#### 사람 승인이 필요한 것

- **폐기 승인(Disposal Authorization)**: 영구 삭제 전 데이터 오너·거버넌스 승인 기록 남기기. 특히 계약·법적 분쟁 관련 데이터는 법무 확인 필수.
- **법적 보존(Legal Hold)**: 소송·감사·조사 시 폐기 정책을 잠시 중단하고 데이터를 그대로 보존. 해제 시에도 명시적 승인 필요.
- **보존 예외(Retention Exception)**: 표준 보존 기간과 다르게 더 오래(또는 짧게) 보존해야 하는 데이터에 대한 개별 레이블/예외 정책 적용.
- **복원(Restore)**: 아카이빙·삭제된 데이터 복원 요청은 데이터 오너 승인 + IT 실행 + 로그 기록.

#### 미사용 데이터 정기 점검

- 분기 또는 반기마다 미사용·중복 데이터 현황 점검
- 활성 AI 프로젝트가 없는 데이터는 Cold/Archive로 이동 또는 폐기 검토
- 점검 결과는 거버넌스 위원회에 보고

---

### 1-4. Before → After 작성 규칙 재료

**[How — Before→After 소절에 쓰임]**

| 구분 | 나쁜 예 (Before) | 좋은 예 (After) |
|------|-----------------|----------------|
| 보존 기간 | 모든 데이터를 "일단 영구 보관" — 스토리지가 가득 차도 삭제 근거 없음 | 데이터 유형별 보존 연한 명문화 — "센서 원시 데이터 5년, 로그 90일" |
| 삭제 주체 | 담당자가 임의로 파일 삭제 — 이유·날짜 기록 없음 | 자동 만료 정책 + 삭제 전 오너 승인 → 폐기 로그 자동 생성 |
| 법적 보존 | 소송 중에도 보존 기간이 지나면 데이터 자동 삭제됨 | Legal Hold 설정 → 소송 해제 전까지 자동 삭제 차단 |
| 스토리지 비용 | 자주 쓰지도 않는 2년 된 센서 데이터가 고비용 Hot 스토리지에 방치 | 접근 빈도 기반 자동 티어 전환 → 비용 30~60% 절감 |
| 과정 데이터 | AI 모델 학습 후 원시 데이터·라벨 삭제 → 모델 재검증 불가 | AI 프로세스 데이터 별도 보존 정책 — 모델 운영 기간 + 3년 유지 |

---

## 2. Tech Stack — 솔루션 검토 재료

### 2-1. 클라우드 오브젝트 스토리지 수명주기 정책 엔진

**[Tech Stack — 클라우드 솔루션 비교 소절에 쓰임]**

#### 2-1-a. AWS S3 Lifecycle + S3 Intelligent-Tiering + Glacier

**공식 문서**: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html  
**S3 Intelligent-Tiering**: https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html

**스토리지 계층 구조:**
```
S3 Standard (Hot) → S3 Standard-IA (비활성화, 30일 이후)
  → S3 Glacier Instant/Flexible Retrieval (아카이빙, 90~365일)
  → S3 Glacier Deep Archive (장기 보존, 180일+)
```

**자동화 내용:**
- **Transition Actions**: 지정 일수 경과 후 저비용 계층 자동 이동
- **Expiration Actions**: 만료 기간 경과 시 자동 삭제
- **S3 Intelligent-Tiering**: 접근 빈도를 분석해 Hot/Cool/Archive 계층 자동 전환 (사람이 규칙 안 써도 됨)
- 기존 오브젝트에도 소급 적용 가능

**규정 준수:**
- **S3 Object Lock (WORM)**: 한번 쓰면 읽기만 허용, 정해진 기간 삭제·수정 불가
- **Legal Hold**: 보존 기간과 무관하게 잠금 유지

**적합 상황:** 클라우드 데이터 레이크, 대용량 IoT 센서 데이터 장기 보존, 규정 준수 아카이빙

---

#### 2-1-b. Azure Blob Storage 수명주기 관리

**공식 문서**: https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview  
**계층 개요**: https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview

**스토리지 계층 구조:**
```
Hot (자주 접근) → Cool (30일 이상 비접근)
  → Cold (90일 이상) → Archive (180일+, 오프라인 스토리지)
```

**자동화 내용:**
- JSON 정책 문서로 규칙 정의 (조건: 생성일·마지막 수정일·마지막 접근일 기반)
- Cool에서 재접근 시 자동으로 Hot 복귀(`enableAutoTierToHotFromCool`)
- 컨테이너 단위·태그 단위 필터 적용 가능
- 정책 변경 후 최대 24시간 내 적용

**주의사항:**
- Archive 계층 데이터는 즉시 접근 불가 — Rehydrate(복원) 시간 필요 (최대 15시간)
- Immutable 컨테이너의 Blob은 수명주기 삭제 정책 적용 불가

**규정 준수:**
- Azure Immutable Blob Storage(WORM): 불변 저장 지원
- Microsoft Defender for Storage 연동으로 보안 감시

**적합 상황:** Microsoft 365 환경, 혼합 워크로드(온프렘+클라우드), Azure 생태계 중심 기업

---

#### 2-1-c. Google Cloud Storage Object Lifecycle Management

**공식 문서**: https://docs.cloud.google.com/storage/docs/lifecycle  
**스토리지 클래스**: https://docs.cloud.google.com/storage/docs/storage-classes

**스토리지 계층 구조:**
```
Standard → Nearline (최소 30일, 월 1회 미만 접근)
  → Coldline (최소 90일, 분기 1회 미만)
  → Archive (최소 365일, 연 1회 미만)
```

**자동화 내용:**
- **Lifecycle Rules**: age(나이)·날짜·스토리지 클래스·접두사/접미사 조건 기반
- **Autoclass**: 접근 패턴을 자동 분석해 Standard↔Nearline↔Coldline↔Archive 자동 전환 (수동 규칙 불필요)
- 삭제(Delete)·계층 전환(SetStorageClass)·미완료 업로드 취소(AbortIncompleteMultipartUpload) 지원

**주의사항:**
- 최소 보관 기간 위반 시 조기 삭제 수수료 발생
- Autoclass 활성화 시 수동 SetStorageClass 규칙과 병행 불가

**적합 상황:** GCP 중심 환경, 대용량 비정형 데이터, ML 파이프라인 데이터 아카이빙

---

### 2-2. ILM·Records Management·Retention 전용 솔루션

**[Tech Stack — 거버넌스·컴플라이언스 도구 소절에 쓰임]**

#### 2-2-a. Microsoft Purview Data Lifecycle Management

**공식 문서**: https://learn.microsoft.com/en-us/purview/data-lifecycle-management  
**시작 가이드**: https://learn.microsoft.com/en-us/purview/get-started-with-data-lifecycle-management

**핵심 기능:**
- **보존 정책(Retention Policies)**: Exchange·SharePoint·OneDrive·Teams 전체에 적용. "N년 보존 후 자동 삭제" 또는 "영구 보존" 설정.
- **보존 레이블(Retention Labels)**: 문서·이메일 단위로 더 긴 보존 기간 예외 적용. 사용자가 수동 부착 또는 콘텐츠 검사로 자동 부착.
- **Records Management**: 법적 기록물로 선언 → 수정·삭제 잠금. 규제 요건 준수용.
- **Adaptive Protection 연동**: 내부자 위험 발생 시 자동으로 보존 레이블 적용.

**Legal Hold 지원:** 소송·감사 시 보존 정책과 무관하게 콘텐츠 보존 가능.

**적합 상황:** Microsoft 365를 사내 협업 플랫폼으로 쓰는 기업, 이메일·문서 보존 컴플라이언스 중심

**배포 방식:** SaaS (Microsoft 365 구독)

---

#### 2-2-b. Informatica ILM (Data Archive)

**참고**: https://blogs.perficient.com/2016/03/16/information-life-cycle-management-using-ilm-data-archive/  
**대안 비교**: https://www.archondatastore.com/blog/informatica-data-archive-alternatives/

**핵심 기능:**
- ERP(SAP·Oracle EBS·PeopleSoft·Siebel)·CRM 데이터를 운영 DB에서 분리해 아카이빙
- 비활성 데이터를 Informatica Data Vault(압축률 최대 98%)로 이동 → 운영 DB 성능 개선
- 레거시 시스템 폐기 지원(애플리케이션 은퇴 시 데이터 보존)
- 보존 정책·폐기 정책 설정

**특이사항:** Cohesity가 Veritas를 인수(2024년 말)하면서 유사 솔루션 시장 재편 중. Informatica ILM 자체도 Salesforce 인수 후 로드맵 변동 — 도입 전 최신 상태 확인 필요.

**적합 상황:** 대형 ERP 중심 제조업체, 레거시 시스템 데이터 보존·폐기 자동화

**배포 방식:** 온프렘 / 클라우드 (요확인)

---

#### 2-2-c. Cohesity (구 Veritas 인수 후 통합)

**공식 페이지**: https://www.cohesity.com/solutions/long-term-retention-and-archival/

**핵심 기능:**
- **DataProtect**: 자동 백업·복구·불변 스냅샷·클라우드 티어링 통합
- **CloudArchive / CloudArchive Direct**: 클라우드 또는 S3 호환 스토리지로 직접 아카이빙
- **Cloud Tier**: 온프렘 데이터를 퍼블릭 클라우드(Hot→Cold 계층)로 자동 이동
- **WORM + 불변성**: 설정된 기간 동안 삭제·수정 차단
- 중복 제거·압축 적용으로 스토리지 효율화

**2024년 변화:** Cohesity가 Veritas 사업부문 인수(2024년 말) → 엔터프라이즈 아카이빙 시장 단일화 추세.

**적합 상황:** 온프렘 백업·아카이빙, 랜섬웨어 복구, 클라우드 계층화 아카이빙

**배포 방식:** 온프렘 어플라이언스 / SaaS / 하이브리드

---

### 2-3. 온프렘·폐쇄망 환경 솔루션

**[Tech Stack — 온프렘/폐쇄망 소절·제조업 특이사항에 쓰임]**

#### 2-3-a. MinIO AIStor (온프렘 오브젝트 스토리지)

**공식 문서**: https://docs.min.io/aistor/administration/object-lifecycle-management/  
**제품 페이지**: https://www.min.io/product/aistor/automated-data-tiering-lifecycle-management

**핵심 기능:**
- 온프렘 / 에지 / 에어갭(Air-Gapped, 폐쇄망) 환경에 설치 가능한 S3 호환 오브젝트 스토리지
- **수명주기 정책**: 오브젝트 나이·태그·접두사·버전 상태 기반 자동 만료 또는 계층 전환
- **Object Tiering**: 콜드 스토리지(고밀도 HDD·S3 호환 외부 스토리지) 자동 이동. 메타데이터는 1차 스토리지에 유지 — 투명한 접근 보장.
- **불변성(WORM)**: SOC 2·HIPAA·FINRA·SEC 17a-4 준수. 자동 보존 실행.
- **버전 관리**: 랜섬웨어·실수 삭제 시 시점 복구 지원

**폐쇄망 적합성:** 모든 텔레메트리가 자체 관리 환경 내에 보존 — 외부 클라우드 없이 운영.

**적합 상황:** 인터넷 연결 불가 제조 현장, 데이터 주권 요구, 온프렘 데이터 레이크 구축

---

#### 2-3-b. NAS Hot + 테이프/오브젝트 Cold 아키텍처 (온프렘 전통 방식)

**참고**: https://www.supermicro.com/en/glossary/cold-data-storage

**구성 원리:**
```
운영 NAS (Hot)
  → 아카이빙 NAS / 오브젝트 스토리지 (Warm/Cold)
  → 테이프(LTO) / 고밀도 JBOD (Archive)
```

**역할:**
- **운영 NAS (Hot)**: 현재 작업·AI 학습 중인 데이터. 빠른 접근 필요.
- **아카이빙 NAS / 오브젝트 스토리지 (Cold)**: 6개월~5년 비활성 데이터. 가끔 접근.
- **테이프(LTO) (Archive)**: 5년 이상 장기 보존. 법적 의무 보존·재난 복구. 비용 가장 저렴.

**자동화 방법:**
- NAS 벤더(NetApp·Dell EMC·HPE Nimble 등)의 ILM 기능 또는 스크립트 기반 정책 엔진으로 자동 이동
- 폐쇄망이면 클라우드 없이 사내 스토리지 계층만으로 운영

**적합 상황:** 클라우드 연결 불가 제조 현장, 기존 테이프 인프라 보유, 초대용량 원시 센서 데이터 장기 보존

---

### 2-4. 솔루션 비교표

**[Tech Stack — 솔루션 비교표에 쓰임]**

| 솔루션 | 유형 | 배포 | 무엇을 자동화 | 적합 상황 |
|--------|------|------|--------------|---------|
| **AWS S3 Lifecycle + Glacier** | 클라우드 오브젝트 스토리지 | 클라우드 | 계층 전환·만료 삭제·WORM | 클라우드 데이터 레이크, IoT 대용량 아카이빙 |
| **S3 Intelligent-Tiering** | 클라우드 (접근빈도 자동) | 클라우드 | 접근 패턴 분석 → 자동 계층 전환 | 접근 패턴이 불규칙한 데이터셋 |
| **Azure Blob Storage Lifecycle** | 클라우드 오브젝트 스토리지 | 클라우드 | Hot/Cool/Cold/Archive 자동 전환, 재접근 시 Hot 복귀 | Azure·M365 중심 기업 |
| **GCS Object Lifecycle (Autoclass)** | 클라우드 오브젝트 스토리지 | 클라우드 | Autoclass로 접근 기반 4계층 자동 관리 | GCP 환경, ML 파이프라인 |
| **Microsoft Purview DLM** | 컴플라이언스·거버넌스 플랫폼 | SaaS | 이메일·문서 보존 정책·레이블·Legal Hold·Records 잠금 | M365 기반, 법적 기록 관리 |
| **Informatica ILM** | ERP 아카이빙 솔루션 | 온프렘/클라우드 | ERP 비활성 데이터 분리·압축 아카이빙, 레거시 폐기 | 대형 ERP 환경, SAP·Oracle 보유 |
| **Cohesity DataProtect** | 백업·아카이빙 통합 플랫폼 | 온프렘/SaaS/하이브리드 | 불변 스냅샷·WORM·클라우드 티어링·자동 아카이빙 | 온프렘 중심, 랜섬웨어 대비 |
| **MinIO AIStor** | 온프렘 오브젝트 스토리지 | 온프렘/에어갭 | 태그·나이 기반 수명주기, Cold 티어링, WORM | 폐쇄망 제조 현장, 데이터 주권 |
| **NAS + 테이프(LTO)** | 전통 스토리지 티어링 | 온프렘 | 수동+스크립트 기반 계층 이동, 장기 테이프 보존 | 기존 인프라 활용, 초대용량 Cold |

---

### 2-5. 선정 기준 (제조업 관점)

**[Tech Stack — 선정 기준 소절에 쓰임]**

제조 현장에서 생애주기 관리 솔루션을 고를 때 확인할 항목:

| 기준 | 확인 내용 |
|------|---------|
| **정책 엔진 자동화** | 시간·태그·접근빈도 기반 자동 계층 전환 지원 여부 |
| **배포 방식** | 클라우드 전용인가, 온프렘·에어갭 가능한가 (폐쇄망 제조 환경 필수 확인) |
| **WORM·불변성** | 법적 보존·규제 준수 요건 충족 여부 |
| **Legal Hold** | 소송·감사 중 자동 삭제 차단 기능 여부 |
| **복원 속도** | 아카이빙된 데이터 복원에 얼마나 걸리나 (Archive 계층은 수 시간~수일) |
| **기존 시스템 연동** | ERP·MES·SCADA 등 기존 제조 시스템과 연동 가능한가 |
| **감사 로그** | 폐기·복원·예외 처리의 이력이 자동 기록되는가 |
| **비용 모델** | 저장+접근+복원 복합 비용 구조 이해 필요 (클라우드 Archive는 복원 비용 높음) |

---

## 3. 경계(Where) 재료

**[Where — 다른 주제와의 관계 섹션에 쓰임]**

F-2 데이터 생애주기 관리의 역할 경계:

| 인접 주제 | 경계 기준 |
|----------|---------|
| **C-3 데이터 계보(Lineage)** | 데이터가 어디서 왔는지·어떻게 변환됐는지 추적 = C-3. F-2는 "언제까지 보존하고 언제 버릴지" 시간축만 담당. |
| **F-4 데이터 접근권한·보안** | 누가 데이터에 접근할 수 있는지 = F-4. F-2는 데이터가 존재하는 기간과 계층을 결정하지, 접근 통제를 하지 않는다. |
| **C-2 데이터 품질** | 데이터가 품질 기준을 충족하는지 판정 = C-2. 품질 미달 데이터의 폐기 결정이 F-2 정책과 연결될 수 있으나, 판정 자체는 C-2 소관. |
| **F-1 DataOps·파이프라인** | 파이프라인이 데이터를 어떻게 처리·배포하는지 = F-1. F-2는 파이프라인이 생성한 데이터를 "얼마나 두고 언제 버릴지"만 담당. |
| **E-1 데이터 상품화(Data Product)** | 재사용 가능한 데이터 상품으로 패키징 = E-1. 상품화된 데이터의 버전 관리·폐기 스케줄은 F-2 정책을 따름. |

**F-2의 핵심 역할 한 줄:** "시간축(얼마나 두고 언제 버리나)"을 전담하며, 접근통제·품질판정·계보추적은 각각 전담 주제가 맡는다.

---

## 4. 출처 목록

| 번호 | 이름 | URL |
|------|------|-----|
| 1 | AWS S3 Lifecycle Management (Official) | https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html |
| 2 | AWS S3 Intelligent-Tiering (Official) | https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html |
| 3 | AWS S3 Lifecycle Transition (Official) | https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-transition-general-considerations.html |
| 4 | Azure Blob Storage Lifecycle Management (Official) | https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview |
| 5 | Azure Blob Access Tiers (Official) | https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview |
| 6 | GCS Object Lifecycle Management (Official) | https://docs.cloud.google.com/storage/docs/lifecycle |
| 7 | GCS Storage Classes (Official) | https://docs.cloud.google.com/storage/docs/storage-classes |
| 8 | Microsoft Purview Data Lifecycle Management (Official) | https://learn.microsoft.com/en-us/purview/data-lifecycle-management |
| 9 | Microsoft Purview 시작 가이드 (Official) | https://learn.microsoft.com/en-us/purview/get-started-with-data-lifecycle-management |
| 10 | MinIO AIStor Lifecycle Management (Official) | https://docs.min.io/aistor/administration/object-lifecycle-management/ |
| 11 | MinIO AIStor Data Tiering 제품 페이지 | https://www.min.io/product/aistor/automated-data-tiering-lifecycle-management |
| 12 | Cohesity Long-term Retention & Archival | https://www.cohesity.com/solutions/long-term-retention-and-archival/ |
| 13 | Informatica ILM 소개 (Perficient) | https://blogs.perficient.com/2016/03/16/information-life-cycle-management-using-ilm-data-archive/ |
| 14 | ILM 개념 설명 (Archon Datastore) | https://www.archondatastore.com/blog/information-lifecycle-management/ |
| 15 | 제조업 Records Retention 스케줄 (FileCloud) | https://www.filecloud.com/manufacturing-industry-records-retention-schedule/ |
| 16 | 데이터 보존 규제 가이드 (RDS Data) | https://rdsolutionsdata.io/what-is-data-retention-rules-compliance-and-strategies-across-industries/ |
| 17 | Cold Storage 개념 (Supermicro) | https://www.supermicro.com/en/glossary/cold-data-storage |
| 18 | Veritas Enterprise Vault (아카이빙) | https://www.veritas.com/content/dam/www/en_us/documents/data-sheet/DS_enterprise_vault_V0969.pdf |
| 19 | WORM Storage 개념 설명 | https://devsecopsschool.com/blog/worm-storage/ |
| 20 | Data Lifecycle Management 개요 (Komprise) | https://www.komprise.com/glossary_terms/data-lifecycle-management/ |
