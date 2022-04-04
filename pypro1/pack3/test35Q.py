from abc import *


class Employee(metaclass=ABCMeta):
    def __init__(self, irum, nai):
        self.irum= irum
        self.nai= nai
    @abstractclassmethod
    def pay(self):
        pass
    
    @abstractclassmethod
    def data_print(self):
        pass
    
    def irumnai_print(self):
        print('이름:{}, 나이:{}'.format(self.irum, self.nai),end=" ")

class Temporary(Employee):
   
    def __init__(self,irum, nai,ilsu, ildang):
        Employee.__init__(self, irum, nai)
        self.ilsu= ilsu
        self.ildang=ildang
    
    
    def pay(self):
        pay=self.ilsu*self.ildang
        return pay
   
    def data_print(self):
        self.irumnai_print()
        print(', 월급:{}'.format(self.pay()))

class Regular(Employee):
    
    def __init__(self,irum, nai,salary):
        super().__init__(irum, nai)
        self.salary= salary
    
    def pay(self):
        return self.salary
   
    def data_print(self):
        self.irumnai_print()
        print(', 급여:{}'.format(self.pay()))

class Salesman(Regular):
    
    def __init__(self, irum, nai, salary, sales, commission):
        Regular.__init__(self, irum, nai, salary)
        self.sales=sales
        self.commission=commission
    
    def pay(self):
        pay= super().pay()+ (self.sales*self.commission)
        return pay
    
    def data_print(self):
        self.irumnai_print()
        print(', 수령액:{}'.format(int(self.pay())))
        
t= Temporary('sul',24,10,15000)
t.data_print() 
print()
r= Regular('minsu', 24, 2000000)
r.data_print()
print()
s= Salesman('bada', 21, 1200000, 5000000, 0.25)
s.data_print()