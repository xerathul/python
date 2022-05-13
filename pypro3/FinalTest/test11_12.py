# [문항11] 다음 데이터는 동일한 상품의 포장지 색상에 따른 매출액에 대한 자료이다.
#
# 포장지 색상에 따른 제품의 매출액에 차이가 존재하는지 two-sample t-검정을 하시오.
# blue : 70 68 82 78 72 68 67 68 88 60 80
# red : 60 65 55 58 67 59 61 68 77 66 66
# (배점:10)

import numpy as np
import scipy.stats as stats
import pandas as pd

blue =[70, 68, 82, 78, 72, 68, 67, 68, 88, 60, 80]
red = [60, 65, 55, 58, 67, 59, 61, 68, 77, 66, 66]

df = pd.DataFrame([blue, red])
df = df.T
df.columns = ['blue','red']
print(df)
#귀무: 포장지 색상에 따른 제품의 매출액에 차이가 없다.
#대립: 포장지 색상에 따른 제품의 매출액에 차이가 있다.
print(np.mean(blue), np.mean(red))
#t-검정
two_sample = stats.ttest_ind(df.blue, df.red)
print(two_sample)
# Ttest_indResult(statistic=2.9280203225212174, pvalue=0.008316545714784403)
# 해석: pvalue=0.00831 < 0.05 이므로 필연적으로 발생된 데이터이다.
# 그러므로 귀무가설이 기각된다.(포장지 색상에 따른 제품의 매출액에 차이가 있다)
print('---------------------------------------------')
# [문항12] 단일표본 검정(one-sample t-test)에 대한 문제다.
#
# 남아 신생아 몸무게의 평균 검정을 수행하려고 한다.
# 파일명 : babyboom.csv (testdata 폴더에 있음) # 1:여아, 2:남아 (배점:10)
# 남아 신생아의 몸무게는 평균이 3000(g)으로 알려져 왔으나 이것이 틀렸다는 주장이 나왔다.
# 표본으로 남아를 뽑아 체중을 측정하였다고 할 때 새로운 주장이 맞는지 검정하시오.

# 귀무 : 남아 신생아의 몸무게는 평균이 3000(g) 이다.
# 대립 : 남아 신생아의 몸무게는 평균이 3000(g)이 아니다.

data = pd.read_csv('../testdata/babyboom.csv')
print(data.head(), data.shape)

boy = data[data.gender == 2]
print(boy.head())

one_sample = stats.ttest_1samp(boy.weight, popmean=3000)
print(one_sample)
#Ttest_1sampResult(statistic=4.47078356044109, pvalue=0.00014690296107439875)
#해석: pvalue=0.000146 < 0.05 이므로 귀무가설 기각, 대립가설 채택

# [문항13] 에이콘 주식회사에서 영업사원들의 '지각횟수'와 '판매횟수' 간에 관계가 있는지 알아보려고 한다.
# 영업사원 5명을 대상으로 한 달 동안 '지각횟수'와 '판매횟수'를 조사했더니 아래와 같은 결과를 얻었다.
# 둘 사이의 상관계수를 출력하고 상관관계가 있는지 설명하시오.
#
# 지각횟수(x) = 1,2,3,4,5
# 판매횟수(y) = 8,7,6,4,5 (배점:10)

import pandas as pd
import numpy as np

df = pd.DataFrame({'x':[1,2,3,4,5],'y':[8,7,6,4,5]})
print(df)
print(df.corr())
#      x    y
# x  1.0 -0.9
# y -0.9  1.0
# 결론, 지각횟수와 판매횟수 간에 강한 음의 상관관계가 존재한다.
