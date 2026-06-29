---
title: "F-2 데이터 생애주기 관리 — 출처 검증 리포트"
date: 2026-06-29
checker: 출처 검증 에이전트 (WebFetch)
target-file: 가이드 작성/F-2 데이터 생애주기 관리/F-2 데이터 생애주기 관리.md
---

# F-2 출처 검증 리포트

## 요약

| 판정 | 개수 | 번호 |
|---|---|---|
| ✅ 살아있고 내용 일치 | 16 | [1][4][5][7][8][9][11][12][13][14][15][16][17][18][20][21] |
| ⚠️ 접속은 되나 내용/URL 주의 | 3 | [2][3][6] |
| ❌ 죽음·404 (교체 필요) | 2 | [10][19] |
| ❓ WebFetch 차단 (직접 확인 필요) | 2 | [22][23] |

---

## URL별 판정 상세

### 표준·개념

| # | 현행 URL | 판정 | 비고 |
|---|---|---|---|
| [1] | `https://www.dama.org/cpages/body-of-knowledge` | ✅ | "DAMA® Data Management Body of Knowledge" 페이지 정상 접속. 2nd Ed. 및 2025년 DAMA-DMBOK 3.0 프로젝트 언급 |
| [2] | `https://www.ibm.com/topics/information-lifecycle-management` | ⚠️ | HTTP 403 반환 (WebFetch 차단). IBM 개발자·토픽 페이지는 봇 차단이 잦음. 페이지 자체가 없어진 것이 아닐 가능성이 높으나, **브라우저 직접 확인 권장**. 대체 후보: `https://www.ibm.com/think/topics/information-lifecycle-management` |
| [3] | `https://www.iso.org/standard/62085.html` | ⚠️ | HTTP 403 반환 (ISO 사이트 봇 차단). ISO 공식 카탈로그 URL 형식은 맞음. 실제 접속 시 ISO 9001:2015 표준 정보 페이지로 정상 표시될 가능성 높음. **브라우저 직접 확인 권장**. |
| [4] | `https://www.pipc.go.kr/` | ✅ | 개인정보보호위원회 공식 사이트 정상 접속. 대한민국 공식 전자정부 사이트 확인 |
| [5] | `https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final` | ✅ | NIST SP 800-53 Rev.5 공식 페이지 정상 접속. "Security and Privacy Controls for Information Systems and Organizations" |
| [6] | `https://www.iso.org/standard/62542.html` | ⚠️ | HTTP 403 반환 (ISO 사이트 봇 차단). URL 형식은 ISO 15489-1:2016 표준 페이지로 올바름. **브라우저 직접 확인 권장**. |

---

### 보존 연한·규정(참고)

| # | 현행 URL | 판정 | 비고 |
|---|---|---|---|
| [7] | `https://www.law.go.kr/법령/상법` | ✅ (조건부) | 서버 자체는 응답하고 "상법" 제목도 표시됨. 다만 상시 접속자 집중 시 "사용자 많음" 오류 메시지가 표시될 수 있음. URL 구조는 유효. **상법 제33조 직접 링크**는 아래 교체 권고 참고. |
| [8] | `https://preteshbiswas.com/2023/07/13/iatf-169492016-clause-7-5-3-2-1-record-retention/` | ✅ | "IATF 16949:2016 Clause 7.5.3.2.1 Record retention" 정상 접속. N+1 calendar year 보존 기준 등 본문 인용 내용 일치 |
| [9] | `https://secureframe.com/blog/data-retention-policy` | ✅ | "Creating a Data Retention Policy: Examples, Best Practices & Template" 정상 접속. 내용 일치 |
| [10] | `https://oxmaint.com/blog/post/industrial-iot-data-storage-how-long-keep-sensor-data` | ❌ | HTTP 403 반환 후 내용 없음. 사실상 접근 불가 (봇 차단 또는 페이지 이동). **대체 URL 필요** — 아래 교체 권고 참고 |
| [11] | `https://www.grmdocumentmanagement.com/blog/business-records-retention-guide/` | ✅ | "Business Records Retention Guide: By Industry (2026)" 정상 접속. 2026.04.09 갱신본. 내용 일치 |

---

### 클라우드 스토리지 수명주기 정책 엔진

| # | 현행 URL | 판정 | 비고 |
|---|---|---|---|
| [12] | `https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html` | ✅ | "Managing the lifecycle of objects" 정상 접속. Transition/Expiration 두 액션 설명 일치 |
| [13] | `https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html` | ✅ | "How S3 Intelligent-Tiering works" 정상 접속. 3 접근 계층(Frequent/Infrequent/Archive) 자동 이동 설명 일치 |
| [14] | `https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview` | ✅ | "Azure Blob Storage lifecycle management overview" 정상 접속. Hot/Cool/Cold/Archive 자동 계층 전환 설명 일치 |
| [15] | `https://learn.microsoft.com/en-us/azure/storage/blobs/access-tiers-overview` | ✅ | "Access tiers for blob data" 정상 접속. Hot/Cool/Cold/Archive 계층 설명 일치 |
| [16] | `https://cloud.google.com/storage/docs/lifecycle` | ✅ (리다이렉트) | `cloud.google.com` → `docs.cloud.google.com`으로 301 리다이렉트됨. "Object Lifecycle Management \| Cloud Storage \| Google Cloud Documentation" 정상 접속. **현행 URL이 리다이렉트를 거치므로 URL을 `https://cloud.google.com/storage/docs/lifecycle`으로 유지하거나 리다이렉트 목적지로 변경 가능. 둘 다 유효.** |
| [17] | `https://cloud.google.com/storage/docs/storage-classes` | ✅ (리다이렉트) | 동일하게 `docs.cloud.google.com`으로 301 리다이렉트. "Storage classes" 페이지 정상 접속. Rapid/Standard/Nearline/Coldline/Archive 5계층 설명 일치 |

---

### 거버넌스·아카이빙·ILM 솔루션

| # | 현행 URL | 판정 | 비고 |
|---|---|---|---|
| [18] | `https://learn.microsoft.com/en-us/purview/data-lifecycle-management` | ✅ | "Learn about Microsoft Purview Data Lifecycle Management" 정상 접속. 보존 정책·Legal Hold 설명 일치 |
| [19] | `https://www.informatica.com/products/data-archive.html` | ❌ | **404 Error** — 해당 URL은 Informatica 사이트에서 완전 삭제됨. 여러 대체 URL 시도(5개 이상) 모두 404. 현재 Informatica 제품 목록(`/products`)에도 "Data Archive" 독립 항목 없음. 아래 교체 권고 참고 |
| [20] | `https://www.cohesity.com/solutions/long-term-retention-and-archival/` | ✅ | "Long-term retention and data archival solution" 정상 접속. 불변 스냅샷·하이브리드 멀티클라우드 아카이빙 설명 일치 |
| [21] | `https://docs.min.io/aistor/administration/object-lifecycle-management/` | ✅ | "Object Lifecycle Management" (MinIO AIStor 공식 문서) 정상 접속. 시간·날짜 기반 자동 전환/만료 설명 일치 |

---

### 아카이빙·법적 보존 개념

| # | 현행 URL | 판정 | 비고 |
|---|---|---|---|
| [22] | `https://www.opentext.com/what-is/legal-hold` | ❓ | HTTP 444 (서버가 응답 없이 연결 닫음). OpenText 사이트 봇 차단. **브라우저 직접 확인 필요**. 대체 후보: `https://www.opentext.com/products/opentext-core-case-management` 또는 `https://www.ibm.com/think/topics/legal-hold` |
| [23] | `https://www.supermicro.com/en/glossary/cold-data-storage` | ❓ | HTTP 403 반환. Supermicro 사이트 봇 차단. **브라우저 직접 확인 필요**. 대체 후보: `https://aws.amazon.com/what-is/cold-storage/` |

---

## 교체 권고 목록

본문을 직접 수정할 때 교체가 필요한 URL은 아래와 같다.

### 필수 교체 (❌ 404 확정)

| # | 교체 필요 이유 | 교체 후보 URL | 비고 |
|---|---|---|---|
| **[10]** oxmaint.com | 봇 차단 / 사실상 접근 불가 | `https://aws.amazon.com/iot/industrial-iot/` 또는 `https://www.seebo.com/industrial-iot-data/` | 산업 IoT 데이터 보관 기간 주제 대체 자료. 내용 수준에 맞는 대안으로 검토 필요 |
| **[19]** Informatica `/products/data-archive.html` | 404 확정. Informatica가 Data Archive 제품 URL 구조 전면 변경 | `https://docs.informatica.com/data-archive/current-version.html` 또는 기술 문서 접근 불가 시 **제품 설명을 일반 기술 설명으로 대체** (예: ILM 개념 출처로 `https://www.techtarget.com/searchstorage/definition/information-lifecycle-management`) | Informatica 공식 Data Archive 페이지를 찾지 못했음. 직접 Informatica 사이트에서 현 제품 URL 확인 필요 |

### 권장 교체 또는 보완 (⚠️ 또는 ❓)

| # | 현행 URL 상태 | 권장 조치 |
|---|---|---|
| **[2]** IBM ILM | WebFetch 봇 차단. 페이지 자체는 살아있을 가능성 높음 | 브라우저 확인 후 유효하면 유지. 없으면 `https://www.ibm.com/think/topics/information-lifecycle-management` 시도 |
| **[7]** 상법 law.go.kr | URL 자체는 유효하나 **제33조 직접 앵커가 없음**. 더 정확한 링크로 교체 권장 | `https://www.law.go.kr/법령/상법/(20230622,19358,20230321)/제33조` (서버 부하 시 오류 가능성 있으나 조문 직접 링크) 또는 `https://www.law.go.kr/법령/상법` (현행 유지, 주석에 "제33조" 명시) |
| **[22]** OpenText Legal Hold | HTTP 444 봇 차단 | 브라우저 직접 확인. 없으면 `https://www.ibm.com/think/topics/legal-hold` 또는 `https://www.techtarget.com/searchcompliance/definition/legal-hold` |
| **[23]** Supermicro cold storage | HTTP 403 봇 차단 | 브라우저 직접 확인. 없으면 `https://aws.amazon.com/what-is/cold-storage/` |

---

## 보존 연한 수치 점검

본문에 단정적으로 쓰인 보존 연한 수치와 출처의 정합성을 점검했다.

| 수치 | 본문 표현 | 점검 결과 |
|---|---|---|
| **상법 10년** | "회계장부 10년(상법)" | 상법 제33조는 "상업장부와 영업에 관한 중요서류 10년 보존"을 규정. [7] URL 자체는 유효(상법 전문). 내용 일치. |
| **세금 관련 5년** | "세금 관련 5년" | 국세기본법 제85조의3 등에 근거한 통상 5년 기준. 법령 명칭 또는 조문 링크가 없으므로 **출처가 약함** — "세법(국세기본법)"으로 명시하거나 법령 링크 추가 권장 |
| **임금대장 3년** | "임금대장 3년" | 근로기준법 제42조에 근거한 3년. 마찬가지로 법령 링크가 없음 — **출처가 약함**. "근로기준법 제42조" 링크 추가 권장 |
| **IATF N+1년** | 직접 언급 없음(참고 출처로만 사용) | [8] URL 내용에 "N+1 calendar year" 기준 명시. 본문 인용 없으므로 이상 없음 |

> **보존 연한 전반 주의사항**: 본문 §2.3에 "본 가이드의 연한은 참고 예시이며 실제 값은 법무·품질 부서가 확정한다"는 면책 문구가 있어 위험 수준은 낮음. 단, 세금 5년·임금대장 3년에 대응하는 법령(국세기본법·근로기준법) 출처가 [7] 상법 링크 하나에 묶여 있으므로, 각각 별도 각주로 분리하거나 "상법·세법·근로기준법 등[\[7\]](#ref7)"으로 복수 명시하는 것이 정확도를 높인다.

---

## 결론 요약

- **즉시 교체 필요**: [19] Informatica Data Archive URL (404 확정)
- **봇 차단으로 판정 불확실 — 브라우저 직접 확인 후 교체 결정**: [10] oxmaint, [22] OpenText, [23] Supermicro
- **나머지 19개 URL ([1][4][5][7][8][9][11][12][13][14][15][16][17][18][20][21] + [2][3][6] ISO/IBM)**: 유효 또는 높은 확률로 유효 — 유지 가능
- **보존 연한 출처**: 세금 5년·임금대장 3년에 대한 출처가 약함 — 각주 보완 권장

검증일: 2026-06-29
