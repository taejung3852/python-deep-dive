# Chapter06-01
# 병행성(Concurrency)
# 이터레이터, 제네레이터
# Iterator, Generator

# 파이썬 반복 가능한 타입
# collections, text file, list, Dict, Set, Tuple, Unpacking, *args... : iterable 하다고 한다. 

# 반복 가능한 이유? -> 내부적으로 iter(x) 함수 호출
t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# print(dir(t))
# __iter__ 가 존재하는 것을 볼 수 있다. 
# 이터레이터 : 이터레이터 객체를 반환하는 함수. 즉, __iter__를 반환하는 함수.

for c in t:
    pass
    # print(c)

# while
w = iter(t)

# print(dir(w))
# __iter__ , __next__가 존재하는 것을 볼 수 있다. 

# t = 'ABCD'

# print(next(w))
# print(next(w))
# print(next(w))
# print(next(w))
# print(next(w)) -> StopIteration 발생 
# 내부적으로 next()가 호출될 때마다 __next__를 호출한다.
# 반복 가능한 객체가 인덱싱을 지원하더라도 내부적으로는 iter() -> next() -> StopIteration을 거친다.

while True:
    try:
        print(next(w))
    except StopIteration:
        break
# 위 for문으로 했을 때랑 내부적으로 똑같다. 단지 for 문이 StopIteration을 감싸서 우리 눈에 안보일 뿐.

print()

# 반복형 확인
print(hasattr(t, '__iter__')) # True
print(hasattr(w, '__next__')) # True

print()

# 좀 더 고급스럽게 확인
from collections import abc

print(isinstance(t, abc.Iterable)) # 반복 가능한가?
print(isinstance(w, abc.Iterable)) # 이터레이터 객체인가?
print()

# 제네레이터(Generator)
# 제네레이터 : 이터레이터 객체를 반환하는 함수. 즉, __iter__를 반환하는 함수.