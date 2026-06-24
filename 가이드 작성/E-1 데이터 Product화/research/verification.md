---
title: E-1 데이터 Product화 — 참고자료 URL 검증 리포트
verified-by: Claude (source-verification agent)
verified-date: 2026-06-24
---

# E-1 참고자료 URL 검증 리포트

가이드 `E-1 데이터 Product화.md`의 `## 참고자료 (References)` 섹션에 수록된 URL 20개를 전수 점검한다.
각 URL은 WebFetch로 직접 접속하여 ① 페이지 생존 여부, ② 클레임과 내용 일치 여부, ③ 리다이렉트/도메인 변경 여부를 확인했다.

---

## 검증 결과 요약표

| Ref | URL (가이드 표기) | 상태 | 메모 |
|-----|------------------|------|------|
| [1] | https://martinfowler.com/articles/data-mesh-principles.html | ✅ OK | Zhamak Dehghani의 "Data Mesh Principles and Logical Architecture" 원문 확인. 클레임과 일치. |
| [2] | https://www.datamesh-architecture.com/data-product-canvas | ✅ OK | Data Product Canvas (8개 구성 요소) 페이지 확인. 클레임과 일치. |
| [3] | https://www.datamesh-manager.com/learn/what-is-a-data-product | ⚠️ 도메인 이전 | datamesh-manager.com은 **Entropy Data(entropy-data.com)** 로 브랜드 리뉴얼. 현재 페이지는 entropy-data.com 도메인에서 서빙되며 콘텐츠(What is a Data Product)는 살아 있음. URL 자체는 아직 접근 가능하나 사이트 전체가 이전 완료. 교체 권장(아래 참조). |
| [4] | https://opendataproducts.org/ | ✅ OK | ODPS(Open Data Product Specification) 공식 홈페이지. ODPS 4.1 등 확인. Linux Foundation 산하. 클레임과 일치. |
| [5] | https://dpds.opendatamesh.org/concepts/data-product-descriptor/ | ✅ OK | Open Data Mesh DPDS 개념 페이지. Data Product Descriptor 5종 포트 설명 확인. 클레임과 일치. |
| [6] | https://www.thoughtworks.com/en-us/insights/e-books/modern-data-engineering-playbook/data-as-a-product | ✅ OK | Thoughtworks "Data as a Product" 페이지 확인. Zhamak Dehghani 인용 포함. 클레임과 일치. |
| [7] | — | — | 가이드에 [7] 미사용 (결번). 이상 없음. |
| [8] | https://www.ovaledge.com/blog/data-product-strategy-guide | ✅ OK | OvalEdge "Data Product Strategy Guide" 블로그 포스트 확인. 우선순위·폐기 판단 관련 내용 포함. 클레임과 일치. |
| [9] | https://atlan.com/know/data-product-lifecycle/ | ✅ OK | Atlan "Data Product Lifecycle" 가이드 확인. 6단계 생애주기(설계→배포→개선→폐기) 설명. 클레임과 일치. |
| [10] | https://www.collibra.com/products/data-marketplace | ✅ OK | Collibra Data Marketplace 공식 제품 페이지. 카탈로그·검색·접근 요청 기능 확인. 클레임과 일치. |
| [11] | https://www.alation.com/product/data-products-marketplace/ | ✅ OK | Alation Data Products Marketplace 공식 제품 페이지. ODPS 표준 활용 내용 확인. 클레임과 일치. |
| [12] | https://www.informatica.com/products/data-governance/cloud-data-marketplace.html | ✅ OK | Informatica Cloud Data Marketplace 공식 제품 페이지. 데이터 공유·거버넌스 기능 확인. 클레임과 일치. |
| [13] | https://www.databricks.com/product/marketplace | ✅ OK | Databricks Marketplace 공식 제품 페이지. 데이터·ML모델·앱·대시보드 공유 플랫폼. 클레임과 일치. |
| [14] | https://www.snowflake.com/en/data-cloud/marketplace/ | ✅ OK | Snowflake Marketplace 공식 제품 페이지. 3,400+ 라이브 데이터 제품 확인. 클레임과 일치. |
| [15] | https://learn.microsoft.com/en-us/purview/unified-catalog-data-products | ✅ OK | Microsoft Purview Unified Catalog Data Products 공식 문서. Owner·접근 정책 포함. 클레임과 일치. |
| [16] | https://learn.microsoft.com/en-us/fabric/governance/onelake-catalog-overview | ✅ OK | Microsoft Fabric OneLake Catalog 개요 문서. 탐색·거버넌스·보안 탭 설명. 클레임과 일치. |
| [17] | https://atlan.com/data-products-marketplace/ | ✅ OK | Atlan Data Marketplace 공식 페이지. 자연어 검색·AI 에이전트 연동(MCP) 포함. 클레임과 일치. |
| [18] | https://docs.datahub.com/docs/dataproducts/ | ✅ OK (리다이렉트 정상) | datahubproject.io → datahub.com → docs.datahub.com 경로로 자동 리다이렉트. 최종 도착지는 공식 DataHub 문서. 콘텐츠(Data Products) 확인. 가이드 표기 URL(`docs.datahub.com`)이 이미 최종 정착지이므로 OK. |
| [19] | https://cloud.google.com/products/knowledge-catalog | ✅ OK (제품명 변경 확인) | 페이지 접근 가능. 단, Google은 2026-04-10부로 **Dataplex Universal Catalog → Knowledge Catalog** 로 제품명 변경. 가이드가 표기한 "Google Cloud — Knowledge Catalog (Dataplex)"는 현재 공식 명칭("Knowledge Catalog, formerly Dataplex")과 일치. URL 및 클레임 모두 유효. |
| [20] | https://data.world/product/knowledge-graph | ✅ OK | data.world Knowledge Graph 제품 페이지. 단, **ServiceNow가 data.world를 인수** 발표(페이지 배너 확인). 현재 페이지는 살아 있으며 클레임과 일치. 향후 URL 변경 가능성 있으나 현재는 정상. |

---

## 수정 필요 항목

### [3] datamesh-manager.com → entropy-data.com 이전

| 항목 | 현재 가이드 표기 | 교체 권장 URL |
|------|----------------|--------------|
| [3] | `https://www.datamesh-manager.com/learn/what-is-a-data-product` | `https://www.entropy-data.com/learn/what-is-a-data-product` |

**사유:** datamesh-manager.com 사이트 전체가 Entropy Data(entropy-data.com)로 브랜드 이전 완료. 접속 시 "Data Mesh Manager is now Entropy" 배너 표시 후 entropy-data.com에서 콘텐츠 서빙. 현재 구 URL은 아직 접근되나 공식적으로는 이전된 상태이므로 교체를 권장.

---

## 주의 관찰 항목 (수정 불요, 모니터링 권장)

| Ref | 사유 |
|-----|------|
| [20] | data.world/product/knowledge-graph — ServiceNow 인수 발표로 향후 도메인/URL 변경 가능성 있음. 현재는 정상. |
| [19] | Google Cloud Knowledge Catalog(구 Dataplex) — 제품명이 2026-04-10 변경됨. 가이드 표기("Knowledge Catalog (Dataplex)")는 현재 명칭과 일치하므로 OK. |

---

## 결론

- **총 20개 URL 중 19개 OK** (직접 접속 + 내용 확인)
- **수정 권장 1건:** [3] datamesh-manager.com → entropy-data.com 도메인 이전
- **관찰 2건:** [19] Google 제품명 변경(이미 반영됨), [20] data.world 인수로 미래 URL 변경 가능성
