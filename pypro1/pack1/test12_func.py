#함수 작성
from pack1.test5_if import res
a=1
b=a+1
print(b)
def DoFunc1():
    print('DoFunc1 수행')
    
c= b+20

# 함수 호출
DoFunc1() #함수 호출
#딴짓 하다가..
res=DoFunc1()
print(res)
print(DoFunc1())

print(DoFunc1)
print(id(DoFunc1))
print(id(print))
print(id(sum))

DoFunc2= DoFunc1 #주소를 치환
DoFunc2()

print('------')
def doFunc3(arg1, arg2):
    res= arg1+arg2
    #return res
    if res%2==1:
        return
    else:
        return res

doFunc3(1, 10)
print(doFunc3(2, 10))
aa=doFunc3(1, 10)
print(aa)

print('------')

def area_tri(a, b):
    c = a*b/2
    area_print(c)
    
def area_print(c):
    print('삼각형의 면적은',c)
    
area_tri(5, 6)

print('------')
def func1():
    print('func1 멤버 처리')
    def func2():
        print('func2 멤버 처리: 내부함수')
    func2()
func1()

print('------')

def swap(a,b):
    return b,a

a=10; b=20
c= swap(a, b)
print(c)
print(c[0],c[1])

print('------')
#if 조건식 안에 함수 사용
def isOdd(arg):
    return arg % 2 ==1

myDict= {x:x*x for x in range(11) if isOdd(x)}
print(myDict)

print('**************')
print('현재 파일(모듈)의 객체 목록: ', globals())
print(dir(__builtins__))
print('프로그램 종료')