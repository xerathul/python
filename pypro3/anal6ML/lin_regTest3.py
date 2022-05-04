# 회귀분석 문제 3) 
#
# kaggle.com에서 carseats.csv 파일을 다운 받아 Sales 변수에 영향을 주는 변수들을 선택하여 선형회귀분석을 실시한다.
# 변수 선택은 모델.summary() 함수를 활용하여 타당한 변수만 임의적으로 선택한다.
# 회귀분석모형의 적절성을 위한 조건도 체크하시오.
# 완성된 모델로 Sales를 예측.

from statsmodels.formula.api import ols
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.stats.outliers_influence import variance_inflation_factor,\
    OLSInfluence
from statsmodels import api

data = pd.read_csv('../testdata/Carseats.csv')
print(data.info())
print(data.corr())

#여러개의 독립변수 묶기
columns = '+'.join(data.columns.difference(['Sales']))
print(columns)
model = ols('Sales ~ '+columns, data= data).fit()
print(model.summary())
#Adj. R-squared:     0.870, Prob (F-statistic):    1.60e-166

#p-value 가 0.05 이상인 변수 빼기
column_select = '+'.join(data.columns.difference(['Sales','US','Urban','Education','Population','ShelveLoc','CompPrice']))
model2 = ols('Sales ~ '+column_select, data= data).fit()
print(model2.summary())
#Adj. R-squared:                  0.534 ,Prob (F-statistic):           1.25e-170
# 영향을 주지 않는 변수들 이였다.

print('**********선형회귀분석의 기존 가정 충족 조건****************')

#잔차항 구하기 (예측값 - 실제값)
data = data.drop(['US','Urban','Education','Population','ShelveLoc','CompPrice'], axis = 1)
#print(data)
fitted = model2.predict(data)
# print(fitted)
residual = data['Sales'] - fitted
print(np.mean(residual))    #-3.1828539803768764e-13 0에 근사


print('\n선형성 : 예측값과 잔차의 분포가 유사 해야 함---')
sns.regplot(fitted, residual, lowess = True, line_kws ={'color':'red'})
plt.plot([fitted.min(), fitted.max()], [0,0],'--', color ='grey')   #평균선
plt.show()

print('정규성: 잔차항이 정규분포를 따라야 함')
sr = stats.zscore(residual)
(x, y), _ = stats.probplot(sr)
sns.scatterplot(x, y)
plt.plot([-3,3],[-3,3], '--',color = 'gray')
plt.show()
print('shapiro test: ',stats.shapiro(residual))
#pvalue=0.0004423 < 0.05 이므로 정규성을 만족하지 못함

print(' 독립성 : 잔차가 자기 상관을 따르는지 확인 Durbin-Watson =0 ~ 4===')
# 독립성 : 독립변수의 값이 서로 관련되지 않아야 한다.
#Durbin-Watson:  1.963 2에 가까울수록 독립적 그러므로 독립성 만족

print('\n등분산성: 잔차의 분산이 일정해야 한다.')
sr = stats.zscore(residual)
sns.regplot(fitted, np.sqrt(np.abs(sr)), lowess = True, line_kws ={'color':'red'})
plt.show()

#VIF(Variable Inflation Factors: 분산 팽창 계수) 값 확인 : 10을 넘으면 다중 공선성을 의심
df = data.drop(['Sales'],axis=1)
print(df.info())
df2 = pd.DataFrame()
df2['vif_value'] = [variance_inflation_factor(df.values, i) for i in range(df.shape[1])]
print(df2)
