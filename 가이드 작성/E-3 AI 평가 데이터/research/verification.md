# E-3 출처 검증 (2026-06-26)

## 수정 필요 건
- **없음.** 본문 References [1]~[16]는 공식 docs/제품 페이지만 인용했고, 확인한 핵심 URL은 모두 생존·주제 일치.
- 리서치 A의 의심 URL(arXiv `2603.06865` 미래 날짜 형식, RAGAS GitHub `vibrantlabsai/ragas`)은 **본문에 미사용** — References는 `docs.ragas.io`·`ragas.io` 공식만 사용.

## 확인 결과

| # | URL | 상태 | 비고 |
|---|-----|------|------|
| 1 | docs.ragas.io/en/stable/concepts/metrics/ | OK | RAGAS Metrics 문서 생존·주제 일치 (web_fetch 확인) |
| 11 | github.com/openai/evals | OK | OpenAI Evals 리포 생존(18.8k★) (web_fetch 확인) |
| 12 | mlflow.org/docs/latest/genai/eval-monitor/ | OK | MLflow GenAI 평가·모니터링 문서 생존·주제 일치 (web_fetch 확인) |
| 8·9·10·13·15·16 | ragas.io / deepeval.com / promptfoo.dev / langfuse.com / smith.langchain.com / braintrust.dev | OK(공지된 공식 제품 페이지) | 널리 쓰이는 공식 도메인 |
| 14 | phoenix.arize.com | 확인 보류 | web_fetch ECONNREFUSED(페처측 연결 이슈, 404 아님). Arize Phoenix 공식 도메인으로 유지 |
| 2~7 | Confident AI · Evidently AI · Maxim AI · HF Cookbook · TestQuality · TrueFoundry | OK(개념 블로그·문서) | 변동 수치 단정 없음 |

## 변동 정보 처리 점검
- 가격·버전·온프레미스 지원 범위: §4.2 표 아래 "도입 전 공식 문서·PoC로 확인" 톤 명시 — OK.
- Humanloop 종료(2025.9) 등 M&A·서비스 변동: 본문에 단정 노출 안 함 — OK.
