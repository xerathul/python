#class

kor= 100

def abc():
    print('함수라고 해')

class MyClass:
    kor= 90 #self의 변수
    
    def abc(self):
        print('난 메소드야!')
    
    def show(self):
        #kor=88
        print(self.kor)
        print(kor) #지역변수에서 먼저 찾고 없으면 글로벌 변수를 찾아감
        self.abc() #클래스 내의 메소드
        abc() #모듈의 function
        
my= MyClass()
my.show()

print('------------')

class OurClass:
    a=1
    
print(OurClass.a)

our1=OurClass()
print(our1.a)

our2=OurClass()
print(our2.a)
our2.b= 2

print(our2.b)
# print(our1.b) error