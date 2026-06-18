# src-006: ISO/IEC 11179 — 메타데이터 레지스트리

- URL: https://en.wikipedia.org/wiki/ISO/IEC_11179
- 제목: ISO/IEC 11179 - Wikipedia
- 접속일: 2026-06-18

## 개요

ISO/IEC 11179는 IT 분야에서 데이터 요소(data element)를 등록·분류·명명·정의·식별하는
메타데이터 레지스트리(MDR) 국제 표준. 메타데이터를 표준화하여 데이터를 이해하고 교환 가능하게 만드는 목적.

## 데이터 요소 등록 필수 요건

데이터 요소는 반드시:
1. **등록(Registered)** — 등록 가이드라인(11179-6) 준수
2. **고유 식별(Uniquely Identified)** — 레지스트리 내 고유 식별자 부여 (11179-5)
3. **명명(Named)** — 명명·식별 원칙 준수 (11179-5)
4. **정의(Defined)** — 데이터 정의 작성 규칙 준수 (11179-4)
5. **분류(Classified)** — 분류 체계(Classification Scheme) 내 위치 지정 (11179-2)

## 핵심 구조 요소

- **객체 클래스(Object Class)** — 기술 대상 엔터티 (예: "기계", "제품")
- **특성(Characteristic)** — 객체 클래스의 속성 (예: "온도", "불량 여부")
- **데이터 요소 개념(Data Element Concept)** — 객체 클래스 + 특성 조합 (예: "기계 가동 온도")
- **값 영역(Value Domain)** — 특성의 허용 값 범위

## 코드 값 요건

열거형(enumerated) 값을 저장하는 데이터 요소는 각 코드 값의 의미를 정밀한 정의로 명시해야 함.

## 표준 구성 (Parts)

| Part | 내용 |
|------|------|
| 11179-1 (2023) | Framework — 전반 프레임워크 |
| 11179-3 | Registry metamodel and basic attributes |
| 11179-4 | Data definitions 작성 규칙 |
| 11179-5 | Naming and identification 원칙 |
| 11179-6 | Registration 가이드라인 |
| 11179-31 (2023) | Metamodel for data specification registration |
