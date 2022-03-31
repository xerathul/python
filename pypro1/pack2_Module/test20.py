#사용자 정의 모듈 작성 및 읽기


a= 10
print(a+10)
print('작업을 하다가... 외부모듈 읽기')

print(dir())

list1=[1,3]
list2=[2,4]

import pack2_Module.myMod1
pack2_Module.myMod1.listHap(list1,list2)
#print(dir())

def listTot(*ar):
    print(ar)
    if __name__ == '__main__':
        print('이 파일이 메인이네')
        
listTot(list1,list2)

print()
from pack2_Module.myMod1 import kbs
kbs()

from pack2_Module.myMod1 import mbc, price
mbc()
print(price) 

print()
import other.myMod2
print(other.myMod2.Hap(5, 3))
from other.myMod2 import Cha
print(Cha(5, 3))

import myMod3
print(myMod3.Gop(5, 3))

from myMod3 import Nanugi, Gop
print(Nanugi(5, 3))