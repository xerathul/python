# 완성차: 여러개의 부품 클래스를 이용하여 완성 차를 생산 

import pack3.test27_handle

class PohamCar:
    turnShowMessage="정지"
    
    def __init__(self, ownerName):
        self.ownerName=ownerName
        self.handle = pack3.test27_handle.PohamHandle() #클래스의 포함관계
        
    def TurnHandle(self,q):
        if q>0: #회전량
            self.turnShowMessage=self.handle.RightTurn(q) #class에서 . 이 두개이상=> 포함관계
        elif q<0:
            self.turnShowMessage= self.handle.LeftTurn(q)
        elif q==0:
            self.turnShowMessage='직진'
            self.handle.quantity= q

if __name__ =='__main__':
    tom= PohamCar('Mr.Tom')
    tom.TurnHandle(10)
    print(tom.ownerName+'의 회전량은 '+tom.turnShowMessage+ str(tom.handle.quantity))
    
    tom.TurnHandle(0)
    print(tom.ownerName+'의 회전량은 '+tom.turnShowMessage+ str(tom.handle.quantity))
    
    print()
    sul= PohamCar('Ms.Tom')
    sul.TurnHandle(-10)
    print(sul.ownerName+'의 회전량은 '+sul.turnShowMessage+ str(sul.handle.quantity))
    
    