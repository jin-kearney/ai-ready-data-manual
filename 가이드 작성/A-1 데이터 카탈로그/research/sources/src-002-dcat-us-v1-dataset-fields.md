# src-002: DCAT-US v1.1 Dataset-Level Fields (Project Open Data)

- URL: https://resources.data.gov/resources/dcat-us/
- 제목: DCAT-US Schema v1.1 (Project Open Data Metadata Schema)
- 접속일: 2026-06-18

## 데이터셋 레벨 필드

### Required (필수)
| 필드 | 설명 |
|------|------|
| title | 데이터 자산의 사람이 읽을 수 있는 이름 |
| description | 데이터 자산의 설명(abstract) |
| keyword | 탐색 지원용 태그·키워드 |
| modified | 데이터셋 최종 변경일 |
| publisher | 발행 기관(상위 기관 포함) |
| contactPoint | 담당자 이름·이메일 |
| identifier | 카탈로그 내 고유 식별자 |
| accessLevel | 접근 수준: public / restricted public / non-public |

### Required-if (조건부 필수)
| 필드 | 조건 |
|------|------|
| license | 라이선스 또는 비라이선스 상태 |
| rights | 접근 제한 사유 설명 |
| spatial | 지리적 적용 범위 있을 때 |
| temporal | 시간적 적용 범위 있을 때 |
| distribution | 접근URL 또는 다운로드URL 있을 때 |

### Optional/Expanded (선택)
| 필드 | 설명 |
|------|------|
| accrualPeriodicity | 데이터셋 발행 주기 |
| conformsTo | 데이터셋이 따르는 표준 URI |
| dataQuality | 정보 품질 지침 충족 여부 |
| describedBy | 데이터 사전(Data Dictionary) URL |
| isPartOf | 부모 데이터셋 식별자 |
| issued | 공식 발행일 |
| language | 데이터셋 언어 |
| landingPage | 데이터셋 허브 페이지 URL |
| references | 관련 문서 URL |
| theme | 주제 카테고리 |

## 배포(Distribution) 레벨 필드
| 필드 | 필수여부 | 설명 |
|------|---------|------|
| accessURL | Required-if | API 또는 인터페이스를 통한 간접 접근 URL |
| downloadURL | Required-if | 직접 다운로드 URL |
| mediaType | Required-if | IANA 미디어 타입 |
| format | Optional | 파일 형식 사람이 읽을 수 있는 설명 |
| title | Optional | 배포본 이름 |
| description | Optional | 배포본 설명 |
