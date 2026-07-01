# Microsoft Fabric + Purview 통합

> 작성일: 2026-06-10 | 조사 기준: 2025~2026년 최신 릴리스 (FabCon Vienna 2025 / FabCon Atlanta 2026 포함)

---

## 기본 정보

| 항목 | 내용 |
|------|------|
| 개발사 | Microsoft Corporation |
| 라이선스 | 상용 |
| 배포 형태 | SaaS — Azure (60+ 리전) |
| 최신 주요 릴리스 | FabCon Vienna (2025-09): Purview+Fabric 심층 통합 / FabCon Atlanta (2026-03): AI 거버넌스·DLP·IRM 확대 |
| 관련 제품군 | Microsoft Fabric, Microsoft Purview, Microsoft Entra, Power BI, Azure AI Foundry |

---

## 한 줄 포지셔닝

**Azure·M365 생태계에 완전 내장된 통합 분석 플랫폼 — Power BI에서 Lakehouse까지 단일 OneLake 위에서 운영하며 Purview로 전사 거버넌스를 구현.**

---

## 주요 기능

### 1. OneLake — 단일 저장소 레이어
- 전사 단일 논리적 데이터 레이크. 복사 없이 모든 Fabric 서비스(Lakehouse, Warehouse, KQL, Dataflow 등)가 동일 데이터 접근
- Delta Parquet 포맷 기반, Apache Iceberg 호환 경로 확장 중
- OneLake Catalog: Fabric 내 모든 아이템(데이터셋, 파이프라인, 레포트)을 통합 발견·탐색

### 2. Microsoft Purview 통합 거버넌스
- **Purview Unified Catalog**: 조직 전체 데이터 자산 발견, 데이터 제품 발행 워크플로우, Glossary 관리
- **자동 리니지**: Fabric 워크로드(Data Factory, Spark, SQL, Power BI)에서 소스→리포트까지 엔드투엔드 리니지 자동 캡처
- **민감도 레이블(Sensitivity Labels)**: M365 정보 보호 레이블을 Fabric 데이터 자산에 적용, 공개 API로 프로그래밍 관리(2026-03 GA)
- **DLP(Data Loss Prevention)**: Fabric Warehouse·KQL/SQL DB에 DLP 정책 적용 (민감정보 감지 시 접근 차단 또는 경고)
- **IRM(Insider Risk Management)**: Fabric Lakehouse 커버, 외부 공유·데이터 유출 행동 감지

### 3. AI 거버넌스 & Copilot 보호
- **AI 프롬프트·응답 민감정보 감지**: Fabric Copilot 및 AI 에이전트의 입력·출력에서 민감정보 탐지
- **과잉 공유(Oversharing) 위험 평가**: AI가 접근할 수 있는 데이터 범위 자동 평가
- **Unsafe AI 사용 조사**: AI 사용 이력 감사 및 이상 행동 탐지
- **DSPM(Data Security Posture Management)**: Purview가 Fabric 데이터 보안 태세 지속 모니터링

### 4. 데이터 품질
- **Purview Data Quality**: 거버넌스되지 않은 자산에도 품질 체크 확장
- **Data Factory 품질 규칙**: 파이프라인 내 인라인 데이터 품질 검증
- **Power BI 데이터셋 인증**: 데이터셋 인증(Certified/Promoted) 제도로 신뢰 데이터 표시

### 5. 접근 제어
- **Microsoft Entra ID 통합**: 조직 SSO·MFA·조건부 접근 정책 그대로 적용
- **Workspace 기반 RBAC**: Admin/Member/Contributor/Viewer 역할 체계
- **Object-level Security**: Lakehouse·Warehouse 내 테이블·열·행 수준 보안
- **Private Link / VNet Integration**: 네트워크 격리 옵션

### 6. 비즈니스 인텔리전스 & AI
- **Fabric Copilot**: 자연어로 데이터 탐색, 리포트 생성, DAX/SQL 작성 자동화 (F-SKU 전체 제공, 2026)
- **Power BI 통합**: 시맨틱 모델을 Glossary 용어와 연결, AI 기반 인사이트 자동 생성
- **Real-time Intelligence**: KQL 기반 스트리밍 데이터 분석·경보

---

## AI-Ready Data 주제 매핑

| 주제코드 | 주제명 | 커버 수준 | 비고 |
|---------|--------|-----------|------|
| A-1 | 데이터 카탈로그 | ○ 완전 | OneLake Catalog + Purview Unified Catalog |
| A-2 | 메타데이터 관리 | ○ 완전 | Purview 자동 스캔·분류 |
| A-3 | 데이터 리니지 | ○ 완전 | Fabric 전체 자동 리니지, Power BI 포함 |
| C-3 | Business Glossary | ○ 완전 | Purview Glossary + Power BI 시맨틱 모델 |
| E-1 | 데이터 품질 | ○ 완전 | Purview DQ, Data Factory 규칙, 인증 제도 |
| C-1 | 접근 제어 | ○ 완전 | Entra ID + RBAC + 행·열 보안 |
| C-2 | 데이터 분류 | ○ 완전 | 민감도 레이블 + DLP + IRM |
| F-1 | DataOps | ○ 완전 | Data Factory, Git 통합, CI/CD |
| F-2 | 데이터 생애주기 | △ 부분 | OneLake 파일 삭제 정책, Time Travel(Delta 기반) |

---

## 강점

1. **Microsoft 생태계 최적화**: Azure AD·Teams·SharePoint·M365 보안 정책 재사용, 별도 ID 관리 불필요
2. **Power BI 통합**: 분석→거버넌스 일원화, 리니지가 리포트까지 연결
3. **AI 거버넌스 선도**: Copilot·AI 에이전트 출력 보호가 경쟁사 대비 가장 성숙
4. **All-in-One 라이선스**: Fabric capacity로 DI·SQL·Spark·Power BI 통합 과금 — 도구 난립 방지
5. **규정 준수 커버리지**: GDPR, CCPA, HIPAA, SOC2, ISO27001 등 광범위한 컴플라이언스 인증

---

## 약점·주의점

1. **Azure 종속성**: Azure 외 클라우드 또는 온프레미스 데이터는 별도 커넥터·게이트웨이 필요
2. **아이템 구분 복잡성**: Lakehouse/Warehouse/Eventhouse 등 여러 스토리지 형태가 공존하여 초기 설계 혼란
3. **대규모 Spark 워크로드**: Databricks 대비 MLOps·고급 ML 파이프라인 환경 미흡
4. **Purview 별도 설정 비용**: Purview를 풀로 활용하려면 추가 라이선스(E5 또는 별도 Purview SKU) 및 설정 공수 필요
5. **비(非) Azure 데이터 리니지**: 외부 소스(AWS·GCP·온프레미스 DB) 리니지는 커스텀 커넥터 개발 필요

---

## 가격 모델

- **Fabric Capacity (F-SKU)**: F2~F2048, CU(Compute Unit) 기반. F4부터 권장 운영 시작
- **Copilot**: 2026년부터 모든 유료 F-SKU에 포함 (F64 이상 제한 해제)
- **Microsoft Purview**: 일부 기능은 M365 E5에 포함, 고급 기능은 별도 Purview Add-on SKU
- **OneLake 저장소**: GB당 과금 (Azure Blob Storage 대비 소폭 프리미엄)
- 참고: https://azure.microsoft.com/en-us/pricing/details/microsoft-fabric/

---

## 연동 생태계

- **커넥터**: 1,000+ (Azure Data Factory 커넥터 + On-premises Data Gateway)
- **SAP 연동**: SAP BW, SAP HANA, SAP ECC 커넥터 (두산 같은 SAP 환경에 유리)
- **BI**: Power BI 네이티브, Tableau·Looker 외부 연결
- **AI/ML**: Azure AI Foundry, Azure ML, OpenAI Service 네이티브 통합
- **오픈 표준**: Delta Lake, Apache Parquet, Apache Iceberg(확장 중)
- **API**: Fabric REST API, Power BI REST API, MS Graph API
- **MCP**: Microsoft 365 Copilot Studio를 통한 에이전트 연동; Fabric 직접 MCP 서버는 로드맵 중
- **GitHub**: Git 통합으로 코드형 파이프라인 관리

---

## 출처

- https://learn.microsoft.com/en-us/fabric/governance/microsoft-purview-fabric
- https://www.microsoft.com/en-us/security/blog/2025/09/16/microsoft-purview-innovations-for-your-fabric-data-unify-data-security-and-governance-for-the-ai-era/
- https://techcommunity.microsoft.com/blog/microsoft-security-blog/new-microsoft-purview-innovations-for-fabric-to-safely-accelerate-your-ai-transf/4502156
- https://www.helpnetsecurity.com/2026/03/17/microsoft-purview-fabric-security-innovations/
- https://azure.microsoft.com/en-us/pricing/details/microsoft-fabric/
- https://petri.com/microsoft-fabric-purview-data-protection-governance/
