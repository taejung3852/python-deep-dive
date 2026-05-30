# Python Deep Dive

파이썬 기초를 넘어 동작 원리나 깊이 있는 개념들을 직접 코드로 짜보면서 정리.
단순 암기보다는 '왜 이렇게 돌아가는지' 이해하는 것에 집중했다. 여기서 다진 기본기로 나중에 어떤 프로젝트든 자연스럽게 적응하는 것이 목표.

![Python](https://img.shields.io/badge/Python-3.13.2-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Progress-f0ad4e)
![Blog](https://img.shields.io/badge/Blog-Velog-20c997?logo=velog&logoColor=white)

---

## 학습 진행률

| 챕터 | 주제 | 핵심 키워드 | 상태 |
|:----:|------|------------|:----:|
| 02 | 클래스 심화 | OOP, 인스턴스/클래스/정적 메서드, 네임스페이스 | ✅ |
| 03 | 매직 메서드 | `__init__`, `__repr__`, 연산자 오버라이딩 | ✅ |
| 04 | 시퀀스 | 컨테이너/플랫, 가변/불변, 해시테이블, Dict/Set | ✅ |
| 05 | 일급 함수 | 클로저, 스코프(LEGB), 데코레이터 | ✅ |
| 06 | 병행성/비동기 | 이터레이터, 제너레이터, 코루틴, AsyncIO | 🔄 |

**진행률** `████████░░` **4 / 5 챕터 완료 (80%)**

---

## 전체 구조

```
python-deep-dive/
└── chapters/
    ├── 02_class/
    │   ├── 02_01_method_class.py   # OOP 기초, 클래스 vs 함수 중심 설계
    │   ├── 02_02_method_class.py   # 클래스 구조, 재사용성
    │   └── 02_03_method_class.py   # 인스턴스 생성, 클래스 관례
    ├── 03_magic_method/
    │   ├── 03_01_magic_method.py   # 매직 메서드 기초 (__init__, __str__ 등)
    │   ├── 03_02_magic_method.py   # 연산자 오버라이딩 (__add__, __mul__ 등)
    │   └── 03_03_magic_method.py   # 객체 추상화, namedtuple 활용
    ├── 04_sequence/
    │   ├── 04_01_sequence.py       # 시퀀스형 분류 (컨테이너/플랫, 가변/불변)
    │   ├── 04_02_sequence.py       # 리스트/튜플 고급, Unpacking
    │   ├── 04_03_sequence.py       # 해시테이블, Dict 내부 구조
    │   └── 04_04_sequence.py       # Dict/Set 심화
    ├── 05_first_class/
    │   ├── 05_01_first_class.py    # 일급 함수 개념 (런타임 초기화, 변수 할당)
    │   ├── 05_02_closure.py        # 클로저 기초, 변수 스코프(LEGB)
    │   ├── 05_03_closure.py        # 클로저 심화, 상태 보존
    │   ├── 05_04_decorator.py      # 데코레이터 구현 및 활용
    │   └── first_class_doc.md      # 개념 정리 문서
    └── 06_concurrency/             # 🔄 진행 중
        └── 06_01_iterator&generator.py  # 이터레이터, 제너레이터
```

---

## 챕터별 상세

### Chapter 02 — 클래스 심화

객체지향 프로그래밍의 핵심 개념을 코드로 직접 짜보며 정리. 함수 중심 설계의 한계와 클래스 중심 설계가 왜 필요한지부터 시작.

- 인스턴스 메서드 / 클래스 메서드 / 정적 메서드의 차이와 용도
- 클래스 네임스페이스와 인스턴스 네임스페이스 분리 이해
- 재사용성 높은 클래스 구조 설계 방법

### Chapter 03 — 매직 메서드 (Special Method)

파이썬의 `__dunder__` 메서드가 어떻게 동작하는지 내부 원리까지 파고들었다.

- `__init__`, `__str__`, `__repr__` 등 기본 매직 메서드
- `__add__`, `__mul__` 등 연산자 오버라이딩으로 커스텀 객체 연산 구현
- `namedtuple`과 객체 추상화 활용

### Chapter 04 — 시퀀스형

파이썬 내장 자료구조의 메모리 구조 차이를 이해하고 올바른 타입을 선택하는 기준 정립.

- 컨테이너(list, tuple, deque) vs 플랫(str, bytes, array) 구분
- 가변/불변 시퀀스의 차이와 성능적 의미
- 해시테이블 기반 Dict/Set의 내부 동작 원리

### Chapter 05 — 일급 함수 (First-Class Function)

클로저와 데코레이터로 이어지는 핵심 개념. 함수형 프로그래밍의 기반이 되는 내용이라 가장 집중해서 정리했다.

- 일급 객체(First-Class Object)로서의 함수: 변수 할당, 인자 전달, 반환
- LEGB 스코프 규칙과 `nonlocal` / `global`의 동작 차이
- 클로저를 활용한 상태 보존 패턴
- 데코레이터로 횡단 관심사(공통 로직) 분리

### Chapter 06 — 병행성/비동기 🔄

- 이터레이터(`__iter__`, `__next__`) 내부 동작
- 제너레이터로 메모리 효율적인 데이터 처리
- (예정) 코루틴, AsyncIO

---

## 환경

- Python 3.13.2 (강의는 3.7 기준)

## 커밋 규칙

| 태그 | 용도 |
|------|------|
| `feat:` | 예제 코드 추가 |
| `fix:` | 코드 오타나 잘못된 개념 수정 |
| `docs:` | README 등 문서 정리 |
| `chore:` | `.gitignore` 등 설정 변경 |
| `refactor:` | 기능 변경 없는 구조 개선 |

## 참고

- **강의:** [우리를 위한 프로그래밍 : 파이썬 중급](https://inf.run/CLcVD) — 강의를 들으며 고민한 흔적을 기록
- **블로그:** [Velog — Python 시리즈](https://velog.io/@parktaejung/series/Python) — 코드 실습 중 고민한 내용, 핵심 개념 정리
