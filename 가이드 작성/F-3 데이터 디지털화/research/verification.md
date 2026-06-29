# F-3 데이터 디지털화 — 참고자료 URL 검증 결과

검증 일자: 2026-06-29  
검증 방법: WebFetch + curl HTTP 상태 코드 확인

| 번호 | URL | 상태 | 조치 제안 |
|------|-----|------|-----------|
| [1] | https://velog.io/@shfur0657/AI-기반-예측-유지보수... | ✅ 살아있음 | 없음 |
| [2] | https://www.machinemetrics.com/blog/paperless-manufacturing | ✅ 살아있음 | 없음 |
| [3] | https://www.documentscanning.ai/blog/how-document-scanning-supports-manufacturing-digital-transformation | ✅ 살아있음 | 없음 |
| [4] | https://dovient.com/resources/blog/tacit-knowledge-manufacturing-hidden-asset | ✅ 살아있음 | 없음 |
| [5] | https://manual.to/the-tribal-knowledge-crisis-in-manufacturing/ | ✅ 살아있음 | 없음 |
| [6] | https://www.augmentir.com/glossary/tacit-knowledge | ✅ 살아있음 | 없음 |
| [7] | https://www.llamaindex.ai/blog/ocr-accuracy | ✅ 살아있음 | 없음 |
| [8] | https://www.abbyy.com/blog/ocr-vs-idp/ | ⚠️ 접속 불가(429 Rate Limit) | ABBYY 사이트 전체가 자동화 접근 차단 중. 수동 확인 권장. 최종 판정 보류. |
| [9] | https://oxmaint.com/industries/power-plant/power-plant-shift-to-digital-maintenance-transformation | ✅ 살아있음 (HTTP 200, curl 직접 접근 시 403이나 WebFetch 403은 봇 차단으로 추정; curl HTTP 200 확인) | 없음 |
| [10] | https://www.handwritingocr.com/blog/korean-handwriting-ocr | ❌ 404 Not Found | 해당 URL의 글이 존재하지 않음. 사이트(handwritingocr.com/blog/)는 살아있으나 한국어 OCR 전용 포스트 없음. 대체 URL: https://www.handwritingocr.com/blog/multilingual-handwriting-ocr 또는 Naver CLOVA OCR 공식 문서로 교체 권장. |
| [11] | https://www.erecordsusa.com/how-to-digitize-engineering-drawings-as-built-plans/ | ✅ 살아있음 | 없음 |
| [12] | https://www.idsys.ee/en/manufacturing/production-process-digitalization-manufacturing/ | ✅ 살아있음 | 없음 |
| [13] | https://www.yokogawa.com/library/resources/white-papers/the-differences-between-digitization-digitalization-and-digital-transformation-in-manufacturing/ | ✅ 살아있음 | 없음 |
| [14] | https://www.sealpath.com/blog/shadow-data-organizations/ | ✅ 살아있음 | 없음 |
| [15] | https://azure.microsoft.com/en-us/products/ai-services/ai-document-intelligence | ⚠️ 리다이렉트 → 새 URL | 301 영구 리다이렉트. 새 공식 URL: https://azure.microsoft.com/en-us/products/ai-foundry/tools/document-intelligence (HTTP 200 확인) |
| [16] | https://cloud.google.com/document-ai | ✅ 살아있음 | 없음 |
| [17] | https://aws.amazon.com/textract/ | ✅ 살아있음 | 없음 |
| [18] | https://www.abbyy.com/finereader-server/ | ⚠️ 접속 불가(429/보안 차단) | ABBYY 사이트 전체 봇 차단. 수동 확인 필요. 최종 판정 보류. |
| [19] | https://www.abbyy.com/vantage/ | ⚠️ 접속 불가(429/보안 차단) | ABBYY 사이트 전체 봇 차단. 수동 확인 필요. 최종 판정 보류. |
| [20] | https://www.ncloud.com/product/aiService/ocr | ✅ 살아있음 (CLOVA OCR 페이지 확인) | 없음 |
| [21] | https://www.upstage.ai/products/document-parse | ✅ 살아있음 | 없음 |
| [22] | https://github.com/PaddlePaddle/PaddleOCR | ✅ 살아있음 | 없음 |
| [23] | https://www.ncloud.com/product/aiService/clovaSpeech | ✅ 살아있음 (CLOVA Speech 페이지 확인) | 없음 |
| [24] | https://www.rtzr.ai/stt | ✅ 살아있음 | 없음 |
| [25] | https://openai.com/index/whisper/ | ⚠️ 403 Forbidden (봇 차단 추정) | openai.com 전체가 자동화 접근 403 반환. 페이지 자체는 존재할 가능성 높음(봇 차단). 대체로 공식 GitHub https://github.com/openai/whisper (HTTP 200 확인) 또는 OpenAI 문서 https://platform.openai.com/docs/guides/speech-to-text 권장. |

---

## 조치 요약

### 즉시 교체 권장
- **[10]** `handwritingocr.com/blog/korean-handwriting-ocr` → 404 사망. 대체 URL 제안:
  - `https://www.handwritingocr.com/blog/` (블로그 존재 확인, 한국어 전용 포스트 없음)
  - 또는 네이버 클라우드 CLOVA OCR 공식 페이지(`https://www.ncloud.com/product/aiService/ocr`)로 교체

### URL 갱신 필요
- **[15]** Azure Document Intelligence → 301 영구 리다이렉트.  
  현행: `https://azure.microsoft.com/en-us/products/ai-services/ai-document-intelligence`  
  갱신: `https://azure.microsoft.com/en-us/products/ai-foundry/tools/document-intelligence`

### 수동 확인 권장 (자동 접근 차단으로 판정 불가)
- **[8]** `abbyy.com/blog/ocr-vs-idp/` — ABBYY 사이트 전체 봇 차단(429). 브라우저로 수동 확인 필요.
- **[18]** `abbyy.com/finereader-server/` — 동일 이유.
- **[19]** `abbyy.com/vantage/` — 동일 이유.
- **[25]** `openai.com/index/whisper/` — OpenAI 사이트 봇 차단(403). 존재 가능성 높음. 대체: `https://github.com/openai/whisper`

### 정상 확인 (17건)
[1] [2] [3] [4] [5] [6] [7] [9] [11] [12] [13] [14] [16] [17] [20] [21] [22] [23] [24]
