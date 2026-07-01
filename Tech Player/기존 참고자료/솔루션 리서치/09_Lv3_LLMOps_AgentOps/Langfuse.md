# Langfuse — 오픈소스 LLM 엔지니어링 플랫폼

> 작성일: 2026-06-10 | 조사 기준: 2025~2026 최신 동향

---

## 기본 정보

| 항목 | 내용 |
|------|------|
| 개발사 | Langfuse GmbH → ClickHouse 자회사 (2026.01 인수) |
| 라이선스 | MIT (오픈소스 코어) |
| 배포 형태 | 클라우드 SaaS (langfuse.com) / Docker·K8s 셀프호스팅 (무제한 무료) |
| 최신 동향 | ClickHouse 인수 (2026.01, $400M Series D) / OpenTelemetry Native SDK (v3) / 업계 최다 채택 오픈소스 LLM 플랫폼 |

---

## 한 줄 포지셔닝

**"MIT 라이선스로 완전 셀프호스팅 가능한 LLM 엔지니어링 통합 플랫폼 — 트레이싱·Prompt·평가·피드백을 하나로"**

---

## 주요 기능

### 트레이싱 (Observability)
- LLM 호출, 검색, 임베딩, 에이전트 액션 전체를 추적
- **OpenTelemetry (OTEL) Native**: v3부터 표준 OTel 기반 SDK로 전환, 다양한 프레임워크와 표준화된 통합
- 지연시간(Latency), 토큰 사용량, 비용, 오류율 대시보드
- **ClickHouse 기반 스토리지**: 대규모 트레이스 고성능 쿼리 지원

### Prompt 관리 (D-3)
- **Prompt Management**: 중앙화된 Prompt Registry
- 버전 관리 및 롤백, 팀 협업 에디터
- Playground: 실제 프로덕션 예시로 Prompt 이터레이션
- Link to traces: Prompt 변경이 출력 품질에 미치는 영향 직접 추적

### 평가 (E-3)
- **LLM-as-judge**: 사실성, 관련성, 유해성 등 자동 평가
- **인간 어노테이션**: 수동 레이블링 UI, 작업 큐(Annotation Queue)
- 사용자 피드백(thumbs up/down, 수치 점수) API 수집
- **Experiments**: 데이터셋 기반 Prompt·모델 A/B 비교 실험

### 데이터셋 관리 (E-3)
- 트레이스에서 평가 예시 자동 추출
- 데이터셋 버전 관리, 실험 결과 비교

### 피드백 수집 (E-4)
- 프로덕션 피드백 → 데이터셋 보강 → 평가 재실행 완전 Feedback Loop
- 메트릭 시계열 모니터링, 품질 저하 알림

---

## AI-Ready Data 주제 매핑

| 코드 | 주제 | 커버 수준 | 설명 |
|------|------|-----------|------|
| D-2 | API/Tool 연계 (MCP) | △ | Tool 호출 추적 가능, MCP 직접 통합은 LiteLLM 경유 권장 |
| D-3 | Prompt/Harness 자산화 | ○ | Prompt Registry·버전관리·Playground·실험 완비 |
| E-3 | AI 평가 데이터 | ○ | 데이터셋·LLM-judge·인간 어노테이션·실험 완비 |
| E-4 | Feedback Loop | ○ | 프로덕션 피드백 → 데이터셋 환류 완전 지원 |

---

## 강점

- **MIT 라이선스 + 셀프호스팅 무제한 무료**: 기업 보안·데이터 주권 요건 완벽 충족
- **OpenTelemetry 표준 준수**: 벤더 종속성 없이 어떤 프레임워크와도 통합
- **ClickHouse 인수 시너지**: 대규모 트레이스 스토리지·분석 성능 강화 (2026~)
- 트레이싱·Prompt·평가·피드백이 하나의 통합 플랫폼에 연결
- 가장 많이 채택된 오픈소스 LLM 플랫폼으로 커뮤니티·문서 풍부

## 약점·주의점

- ClickHouse 인수 이후 장기 라이선스 정책 변동 가능성 주시 필요 (현재 MIT 유지 선언)
- Agent 복잡도 증가 시 LangSmith 대비 Agent 특화 시각화 상대적으로 약함
- 셀프호스팅 운영: ClickHouse + PostgreSQL + 앱서버 인프라 관리 필요
  - 인프라 비용 예상: $270~$1,000/월 (트레이스 볼륨에 따라)

---

## 가격 모델

| 플랜 | 가격 | 주요 포함 |
|------|------|-----------|
| Hobby (Cloud) | 무료 | 월 50만 관측, 기본 기능 |
| Pro (Cloud) | $59/월 | 월 500만 관측, 팀 협업 |
| Team (Cloud) | $499/월 | SSO, 고급 RBAC, 더 많은 할당량 |
| Enterprise (Cloud/Self-host) | 협의 | 전용 지원, SLA |
| **셀프호스팅** | **무료 (인프라 비용만)** | MIT, 기능 제한 없음 |

---

## 연동 생태계

- **SDK**: Python, TypeScript/JS
- **프레임워크**: OpenAI, Anthropic, LangChain, LlamaIndex, DSPy, Vercel AI SDK, AWS Bedrock
- **게이트웨이**: LiteLLM (네이티브 연동), Portkey
- **OpenTelemetry**: OTLP 수신, 표준 계측기 모두 지원
- **인프라**: Docker Compose / K8s Helm Chart / ClickHouse Cloud

---

## 출처

- https://langfuse.com/
- https://github.com/langfuse/langfuse
- https://langfuse.com/docs
- https://langfuse.com/integrations/native/opentelemetry
- https://clickhouse.com/blog/clickhouse-acquires-langfuse-open-source-llm-observability
- https://langfuse.com/blog/joining-clickhouse
- https://langfuse.com/pricing-self-host
- https://coverge.ai/blog/langfuse-pricing
