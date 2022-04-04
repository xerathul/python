# 일급함수 지원 성립 조건

def func1(a,b):
    return a+b

func2=func1

print(func1(2,3))
print(func2(2,3))

print()
def func3(f):  #매개변수로 함수
    def func4(): # 내부 함수
        print('나는 내부 함수양')
    func4()
    return f #반환값이 함수

mbc= func3(func1) 
print(mbc)        
print(mbc(3,4))

print('-----람다(lamda) 함수 축약함수: 이름이 없는 한줄짜리 함수------')
# def를 쓸 정도로 복잡하지 않거나, def를 쓸수 없는곳에 사용
# 형식 : lambda 인자, ... : 표현식   <== return 없이 결과를 반환
def Hap(x,y): x+y
print('답른',Hap(1,2))

print((lambda x, y: x+y)(1,2))

g= lambda x, y: x*y
print(g(3,4))
imsi= g(3,4)
print(imsi)

hap=lambda m,n: m+n
print(hap(1,2),'합')
print()

#람다도 가변인수 사용 가능
kbs= lambda a, su=10: a+su
print(kbs(5))
print(kbs(5,6))

sbs= lambda a, *tu, **di:print(a,tu,di)
sbs(1,2,3,m=4,n=5)
sbs(1,2,3,4,5)

print()
li =[lambda a, b:a+b, lambda a,b:a*b]
print(li[0](3,4))
print(li[1](3,4))

print()
# filter(함수, sequence 자료)
print(list(filter(lambda a: a<5, range(10))))
print(list(filter(lambda a: a%2, range(10))))
print(list(filter(lambda a: a%5==0 and a%7==0, range(1,101))))