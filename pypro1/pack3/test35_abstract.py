# 추상메소드 - 다형성을 구현하기 위해 오버라이드를 하기위한 용도
#         - 추상메소드를 하나라도 가지고 있는 경우 대체적으로 추상클래스라고 한다.
from abc import *


class AbstractClass(metaclass= ABCMeta): #추상 클래스
    @abstractmethod
    def abcMethod(self): #추상 메소드
        pass
    
    def normalMethod(self): # 일반 메소드
        print('추상 클래스 내의 일반메소드')
        
#aa= AbstractClass()  TypeError: Can't instantiate abstract class AbstractClass with abstract method abcMethod

class Child1(AbstractClass):
    name='i am child 1'
   
    def abcMethod(self): # 추상의 파생 클래스는 반드시 추상 메소드 오버라이드
        print('추상메소드를 오버라이딩')
    
c1=Child1()
print(c1.name)
c1.abcMethod()
c1.normalMethod()

print()
class Child2(AbstractClass):
  
    def abcMethod(self):
       a= 1
       b=20
       print('추상메소드를 오버라이딩 해서 마법에서 풀림 ㅎㅎ')
    
    def normalMethod(self):#오버라이딩이 선택적
        print('부모 메소드를 댜시 정의함')

c2= Child2()
c2.abcMethod()
c2.normalMethod()

print('다형성---')
mbc=c1
mbc.abcMethod()
print()
mbc=c2
mbc.abcMethod()