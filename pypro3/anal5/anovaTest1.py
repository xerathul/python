# [ANOVA 예제 1]
#
# 빵을 기름에 튀길 때 네 가지 기름의 종류에 따라 빵에 흡수된 기름의 양을 측정하였다.
# 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하는지를 분산분석을 통해 알아보자.
# 조건 : NaN이 들어 있는 행은 해당 칼럼의 평균값으로 대체하여 사용한다.

import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.formula.api import ols
import statsmodels.api as sm
from matplotlib import pyplot as plt
from statsmodels.stats.anova import anova_lm

kind = [1,2,3,4,2,1,3,4,2,1,2,3,4,1,2,1,1,3,4,2]
quantity= [64, 72, 68, 77, 56, np.nan, 95, 78, 55, 91, 63, 49, 70, 80, 90, 33, 44, 55, 66, 77]

data = pd.DataFrame({'kind': kind, 'quantity':quantity})
data = data.fillna(np.mean(data.quantity))
# 등분산 확인 : 만족하면 anova, 만족하지 않으면 welch_anova
# 등분산을 만족하지 않으면 데이터 가공을 생각할 수도 있다. - 표준화, 정규화, transformation(자연log를 씌움)
g1= data[data['kind']==1]
g1 =g1.fillna(np.mean(data['quantity']))
g2= data[data['kind']==2]
g3= data[data['kind']==3]
g4= data[data['kind']==4]

print(g1)

q1=g1.quantity
q2=g2.quantity
q3=g3.quantity
q4=g4.quantity
print('등분산성 확인: ', stats.levene(q1,q2,q3,q4))
#pvalue=0.2990565688 > 0.05 등분산성 만족

# 정규성 확인 => 정규성 만족
print(stats.shapiro(q1))
print(stats.shapiro(q2))
print(stats.shapiro(q3))
print(stats.shapiro(q4))

#f통계량을 얻기 위해 회귀분석 모델을 사용
print(stats.f_oneway(q1,q2,q3,q4))
#pvalue=0.898494>0.05 귀무가설 채택
#기름의 종류에 따라 흡수하는 기름의 평균에 차이가 없다.

#anova 사용
lmodel = ols('quantity ~ C(kind)', data = data).fit()
print(anova_lm(lmodel, typ=1))  #0.898495


#사후 검정(Post Hoc Test)
#분산분석은 세개 이상의 집단에 평균에 차이 유무만을 알려줌
#세개 이상의 집단 각각의 집단 간 평균의 차이를 알고 싶은 경우
from statsmodels.stats.multicomp import pairwise_tukeyhsd
turkey_result = pairwise_tukeyhsd(endog=data.quantity, groups = data.kind)
print(turkey_result)

turkey_result.plot_simultaneous(xlabel ='mean', ylabel='group')
plt.show()