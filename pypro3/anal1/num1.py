#numpy: 고속연산, ndarray를 지원
#데이터 분석 관련 모듈 전체 생태계의 핵심을 이루고 있기에 다룰 줄 알아야 한다.

from astropy.io.ascii.cparser import math

# 평균, 분산, 표준편차 구하기(모집단/ 표본 통계량)

#grades = [1, 3, -2, 4]  #변량(변수, 확률값, 관측값)
grades = [1,2,3,4,5,6,7,8,9]
def show_grades(grades):
    for g in grades:
        print(g, end=" ")
        
show_grades(grades)

def sum_grades(grades):
    tot=0
    for g in grades:
        tot += g
    return tot
    
sum_grades(grades)
print()
print('합은 ', sum_grades(grades))

def avg_grades(grades):
    tot= sum_grades(grades)
    avg= tot/len(grades)
    return avg

print('평균은', avg_grades(grades))

def var_grades(grades):
    avg= avg_grades(grades)
    var = 0
    for su in grades:
        var +=(su - avg) ** 2
    return var/len(grades)      #모집단으로 계산(파이썬)
    #return var/(len(grades) - 1     #표본집단으로 계산(R))

#분산이 크면 산포도가 크고 데이터가 흩어져 있다
    
print('분산은', var_grades(grades))

def std_grades(grades):
    return var_grades(grades) ** 0.5
    #return math.sqrt(grades)

print('표준편차는', std_grades(grades))
print('------------------------------------')
print('numpy로 계산')

import numpy as np
#print('합은', numpy.sum(grades))
print('합은', np.sum(grades))
print('평균은', np.average(grades))    
print('평균은', np.mean(grades))   #중간값
print('분산은', np.var(grades))
print('표준편차는',np.std(grades))