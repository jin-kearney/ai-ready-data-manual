# src-006 — Microsoft Purview: Unified Catalog Workflows

**URL:** https://learn.microsoft.com/en-us/purview/unified-catalog-workflows  
**제목:** Workflows in Unified Catalog | Microsoft Learn  
**접속일:** 2026-06-18 (문서 최종 업데이트: 2026-04-20)

---

## 개요

Microsoft Purview Unified Catalog 워크플로우: 접근 요청 승인, 데이터 제품·용어집 게시 등 승인 시나리오를 관리하는 자동화된 반복 가능한 프로세스.

## 워크플로우 유형

1. **데이터 제품 접근 요청** — 데이터 제품 접근 요청 및 승인 생성 관리
2. **카탈로그 큐레이션 (게시 워크플로우)** — 데이터 제품·용어집 용어의 거버넌스 도메인별 게시 자동화

## 역할 요건

- **게시 워크플로우** 생성·관리: Governance Domain Creator 역할
- **데이터 제품 접근 워크플로우** 생성: Data Product Owner 역할

## 데이터 제품 접근 워크플로우 구성 절차

1. Unified Catalog에서 데이터 제품 상세 페이지 또는 Workflows 페이지 진입
2. **New Workflow** 선택
3. 이름·설명 입력
4. Workflow category: **Data product access** 선택
5. Create → 기본 템플릿 편집
6. **Start and wait for an approval** 설정:
   - **Pending on all**: 여러 승인자 모두 승인 필요
   - **Pending on any**: 승인자 중 1명만 승인하면 됨
7. Condition 설정: yes/no 분기 구성
   - If yes → 접근 요청 승인
   - If no → 접근 요청 거절
8. Set scope: 적용 도메인/데이터 제품 선택

## 카탈로그 큐레이션(게시) 워크플로우 흐름

- 거버넌스 도메인 데이터 제품 오너·데이터 스튜어드가 드래프트 단계에서 광범위하게 협업
- 카탈로그 게시 전 최종 검토 보장
- 게시 승인 유형: Pending on all / Pending on any 선택
- If yes → 데이터 제품 게시, If no → 드래프트 상태 유지

## 추가 액션 옵션
- Start and wait for approval (단계 추가)
- Condition (분기 추가)
- Approve/Complete/Reject data subscription
- Send email notifications (이메일 알림 자동 발송)

## 주요 제한 사항
- 현재 버전에서 메타데이터 변수, 이메일 템플릿 커스터마이징 미지원
- 외부 커넥터 미포함
- 단일 데이터 제품 또는 거버넌스 도메인 전체에만 동일 승인자 목록으로 접근 워크플로우 구성 가능
- 보안 그룹을 승인자로 추가 시 이메일 사용 가능한 그룹이어야 함
