# Chapter05-02
# 일급 함수(일급 객체) -> 매우매우 중요하다. 코루틴, 클로져에 연결되는 개념. 함수형 프로그래밍이 가능해진다.
# 클로저 기초

# 파이썬 변수 범위(scope)

# Ex1
def func_v1(a):
    print(a)
    print(b)

# func_v1(10)-> 당연히 에러가 발생한다.

# Ex2
b = 20

def func_v2(a):
    print(a)
    print(b)

 
func_v2(10)

# Ex3
c = 30

def func_v3(a):
    print(a)
    print(c)
    c = 40

# func_v3(10)# -> UnboundLocalError가 발생한다. 

# 위 에러가 나타나는 이유는 변수 범위 때문이다. 
# 파이썬 인터프리터는 함수를 실행시키기 전에 한번 전체적으로 코드를 훑는데,
# c는 현재 func_v3 함수에서 지역변수로 간주하게 된다.

# 즉, print(c)는 c가 정의되기 전에 실행을 시키게 된 꼴이 되어버린것이다. (만약 c=40 이 없었다면 전역변수로서 실행되었을 것.)

# UnboundLocalError를 해결하기 위해서는 아래처럼 함수 선언시 global로 전역변수 처리해주면 된다.
def func_v3_1(a):
    global c
    b=10
    print(a)
    print(c)
    c = 40

# Closure(클로저) 사용 이유

## 스코프가 닫혀도 값을 기억한다.
### 예를 들어 위 func_v3_1을 기준으로 설명을 하면 b라는 변수의 값이 소멸이 되어야하는데 클로져는 그것을 기억하고 있다.

## 서버 프로그래밍에서 중요한 부분 -> 동시성(Concurrency) 제어 -> 메모리 공간에 여러 자원이 접근 -> 교착상태(Dead Lock)
### 과거 포항 지진(300만명이 동시에 네이버 접속), 디도스 공격이 들어올 때 서버가 이런 대응을 하면 문제 없을 것이다.
### 파이썬에서는 메모리를 공유하지 않고 메시지 전달로 처리한다.
### 파이썬에서 클로저는 공유하되 변경되지 않는(Immutable, Read Only) 적극적으로 사용 - 함수형 프로그래밍

## 클로저는 불변자료구조 및 ATOM, STM - 멀티스레드[Coroutine(단일 스레드 환경에서도 멀티 스레드인것 처럼 여러개의 일을 동시에 처리할 수 있는 기반을 만들 수 있다.)] 프로그래밍에 강점

## 정리: 클로저는 상태를 기억한다! -> 어떤 상태? "불변 상태"

a = 100

print(a+100)
print(a+1000)

# 결과 누적 (함수사용)
print(sum(range(1,51)))
print(sum(range(51,101)))


# 클래스 이용
class Averager():
    def __init__(self):
        self.series = []

    def __call__(self, v): # [매우 중요] 클래스가 callable 메서드를 들고 있으면 함수처럼 호출할 수 있다. __call__ 을 해주지 않으면 없다. 이건 사용자가 직접 정의해야하는 것이다.
        self.series.append(v)
        print(f'inner >> {self.series} / {len(self.series)}')

        return sum(self.series) / len(self.series)

# 인스턴스 생성
averager_cls = Averager()

print(dir(averager_cls))

# 누적
print(averager_cls(10)) # 함수처럼 실행한다
# --결과--
# 10.0

print(averager_cls(30))
# --결과--
# 20.0

print(averager_cls(50))
# --결과--
# 30.0

print(averager_cls(70))
# --결과--
# 40.0

print(averager_cls(193))
# --결과--
# 70.6

# 여기서 말하고 싶은거는 계속 누적되는 효과를 얻을 수 있다는 것이다. -> 이게 클로저의 개념이다!
## 클로저를 구현한 것이 아니라 개념을 이해하기 위해서 클래스의 callable 함수를 이용한것 

