#1. 클래스의 포함관계 연습문제 https://cafe.daum.net/flowlife/RUrO/24


class Machine:
    def __init__(self,coin):
        self.coin=coin
        
    def showData(self):
        #print(self.coin,self.cupCount)
        if self.coin < self.cupCount*200:
            self.errorMsg=True
            return self.errorMsg
        elif self.coin>= self.cupCount*200:
            change= self.coin-self.cupCount*200
            return change
    
class Coinin:
    
    def __init__(self):
        
        insertcoin=int(input('동전을 입력하세요: '))
        self.machine=Machine(insertcoin)
      
    def cupCount(self):
        insertCup=int(input('몇잔을 원하세요: '))
        self.machine.cupCount=insertCup
 
    def Result(self):
        self.cupCount()
        result= self.machine.showData()
        if result==True:
            print('요금이 부족합니다')
        else: 
            print('커피',self.machine.cupCount,'잔 과 잔돈',result)

if __name__=="__main__":
    
    Coinin().Result()