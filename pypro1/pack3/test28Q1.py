class Machine:
    
    def showData(self):    
        
        coin = int(input('동전을 입력하세요 : '))
        cupCount = int(input('몇 잔을 원하세요 : '))
        return CoinIn(coin).culc(cupCount)
        
class CoinIn:
    
    def __init__(self, coin):
        self.coin = coin 
        
    def culc(self, cupCount):
        self.cupCount = cupCount
        totprice = cupCount * 200
        if self.coin < totprice or self.coin < 200:
            print('요금 부족')
            
        else:
            change = self.coin-(200 * cupCount)
            print('커피', str(self.cupCount) + '잔과', '잔돈', str(change) + '원') 

if __name__ == '__main__':
    aa = Machine()
    aa.showData()