# function : 자원의 재활용 가능. 여러 개의 수행문을 하나의 이름으로 묶은 실행 단위 이다.
# 사용자 정의 함수형식 :def 함수명(para...): @@
# 내장함수 : maker 가 제공하는 함수
print('표준 출력 장치로 데이터를 출력하는 내장함수')
print(sum([1,2,3]))
print(bin(8),'2진수 표현')
print(int(1.7),float(2), str(5)+'5')
a=10
b=eval('a+5')
print(b)

print(all([True,False]))
print(any([True,False]))
a = [1,3,2,5,7,6]
res = all(i<10 for i in a)
print('모든 숫자가 10 미만?', res)

print()
x=[1,2,3]
y=['a','b']
for i in zip(x,y):
    print(i)
print(round(1.2), round(1.6))

import math # import 필요한 모듈
print(math.ceil(1.2),math.ceil(1.6))#올림
print(math.floor(1.2),math.floor(1.6))#내림
print(math.pi)
