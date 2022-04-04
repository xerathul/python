# 상속


class Person:
    say='난 사람이야'
    nai=20
    __abc='private' #private=현재 클래스 내에서만 유효하게됨
    def __init__(self,nai):
        print('person 생성자')
        self.nai= nai
    
    def printInfo(self):
        print('나이:{}, 이야기:{}'.format(self.nai, self.say))
    
    def hello(self):
        print('안녕')
        print(self.__abc)
        
print(Person.say, Person.nai)
p= Person(22)
p.printInfo()
p.hello()

print('****'*10)
class Employee(Person):
    say='일하는 동물'
    subject='근로자'
    def __init__(self):
        print('Employee Constructor')
    def printInfo(self):  #method override
        print('Employee Class 내의 printInfo')
    def eprintInfo(self):
        self.printInfo()
        super().printInfo()
        print(self.say, super().say)
        self.hello()
        
        
e= Employee()
print(e.say, e.nai)
print(e.subject)
e.printInfo()
e.eprintInfo()
print('****'*10)

class Worker(Person):
    def __init__(self,nai):
        print('Worker Constructor')
        super().__init__(nai)
    
    def wprintInfo(self):
        super().printInfo()
        
w= Worker('25')
print(w.say, w.nai)
w.printInfo()
w.wprintInfo()
print('----'*10)

class Programmer(Worker):
    def __init__(self, nai): 
        print('Programmer 생성자') 
        Worker.__init__(self, nai) #unBound method Call
        
    def wprintInfo(self): #오버라이딩
        print('Programmer 내에 작성된 wprintInfo')
    
    def hello2(self):
        print(super().__abc)
        
    @staticmethod
    def sbs(tel):
        print('sbs- static method',tel)
    
pr=Programmer(33)
print(pr.say, pr.nai)
pr.printInfo()
pr.wprintInfo()

print()
p.hello()
#pr.hello2() err(private이기 때문에)
pr.sbs(1040780887)

print()
print('class type---')
a = 10
print(type(a))
print(type(pr))
print(Programmer.__bases__)
print(Worker.__bases__)
print(Person.__bases__)

