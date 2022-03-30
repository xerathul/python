# closure : scope에 제약을 받지 않는 변수들을 포함하고 있는 코드 블럭이다
# 내부함수의 멤버를 함수 밖에서 참조가 가능. 내부함수의 주소를 반환해 사용
from sympy.physics.units import amount

def funcTimes(a,b):
    c= a*b
    return c

print(funcTimes(2, 3))

kbs= funcTimes(2,3) #실행 결과를 치환
print(kbs)

kbs= funcTimes # 주소 치환
print(kbs)
print(kbs(2, 3))
print(id(kbs),id(funcTimes))

del funcTimes
print(kbs(2,3))

mbc= sbs=kbs
print(mbc(2,3))
print(sbs(2,3))

print('크로저를 사용하지 않은 경우')
def out():
    count=0
    def inn():
        nonlocal count
        count +=1
        return count
    print(inn())
out()
out()
    
print('크로저를 사용한 경우')
def outer():
    count=0
    def inner():
        nonlocal count
        count +=1
        return count
    return inner #<==요거를 클로저 : 내부함수의 주소를 반환

var1=outer() # car car1= newCar()
print(var1)
print(var1())  
print(var1())
imsi= var1()
print(imsi)
print()
var2= outer() # car car2= newCar()
print(var2())
print(var2())
print(id(var1),id(var2),type(var1), type(var2))

print('수량 * 단가 * 세금을 출력하는 함수')
def outer2(tax): # tax = 지역변수
    def inner2(su, dan):
        amount = su* dan * tax
        return amount
    return inner2

#1분기에는 수량*단가에 대해 tax가 0.1이 부과
q1 = outer2(0.1)
result1= q1(5,50000)
print('result1: ', result1)
result2= q1(2,10000)
print('result2: ', result2)
print()
q2= outer2(0.05)
result3= q2(5,50000)
print('result3: ', result3)
result4= q2(2,10000)
print('result4: ', result4)


