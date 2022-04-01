#로또 생성기 : 클래스의 포함관계

import random

class LottoBall:
    def __init__(self, num):
        self.num= num
        
class LottoMachine:
    def __init__(self):
        self.ballList=[]
        
        for i in range(1,46):
            self.ballList.append(LottoBall(i)) #클래스의 포함관계

    def selectBall(self):
        for a in range(45):
            print(self.ballList[a].num, end=' ')
        random.shuffle(self.ballList)
        #섞은후
        print()
        for a in range(45):
            print(self.ballList[a].num, end=' ')
            
        return self.ballList[0:6]
    
class LottoUi:
    def __init__(self):
        self.machine=LottoMachine()  #클래스의 포함관계
    
    def playLotto(self):
        input('로또 번호 뽑기를 시작하려면 엔터키를 누르세요')
        selectBalls=self.machine.selectBall()
        print()
        print('당첨번호: ')
        for ball in selectBalls:
            print(ball.num, end=" ")
        
if __name__=="__main__":
    #aa=LottoUi()
    #aa.playLotto()
    LottoUi().playLotto()
