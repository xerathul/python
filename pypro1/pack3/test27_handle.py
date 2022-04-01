# 완성 제품 의 부품 클래스로 핸들을 만들어보자


class PohamHandle:
    quantity= 0 #회전량
    
    def LeftTurn(self,quantity):
        self.quantity=quantity
        return '좌회전'
    
    def RightTurn(self, quantity):
        self.quantity=quantity
        return '우회전'
    
    #... 