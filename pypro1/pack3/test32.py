# 다중상속
# 복수의 클래스를 상속 가능: 순서가 중요
class Donkey:
    data='당나귀 만세'
    
    def skill(self):
        print('당나귀 스킬: 짐나르기')

class Horse:
    def skill(self):
        print('말 스킬: 달리기')
    
    def hobby(self):
        print('프로그램 짜기')

class Mule1(Donkey, Horse): #먼저 적어준 클래스에게 우선순위 존재
   
    pass

mu1= Mule1()
mu1.skill()
mu1.hobby()

print()

class Mule2(Horse, Donkey):
    def play(self):
        print('노새 고유 메소드')
        
    def hobby(self):
        print('노새는 걷기를 좋아함')
        
    def showHobby(self):
        self.hobby()
        super().hobby()
        print(self.data, super().data)
        
mu2=Mule2()
mu2.skill()
mu2.hobby()
mu2.showHobby()