# ols 사용 : 가장 기본적인 결정론적 선형회귀 방법. 불확실성이 있다.

import pandas as pd
from statsmodels.formula.api import ols

df = pd.read_csv('../testdata/drinking_water.csv')
print(df.head())
print(df.corr())

# 회귀분석 : 만족도와 적절성은 인과관계가 있다라는 가정 하에    #0.766853
model = ols(formula = '만족도 ~ 적절성', data = df).fit()     #fit() 학습을 하는 것

print(model.summary())
# 독립변수 x의 분산이 종속변수 y의 분산을 설명하는 분산 : R-squared (설명력)
# R 값이 1에 가까울수록 회귀선 근처에 값들이 분포되어있고, 0에 가까울수록 값이 분산되어 있다.
# 독립변수가 2개 이상 일 때는 수정된 결정계수 사용(Adj. R-squared)
# 회귀분석에서 기울기= 0 귀무가설 아니면 대립가설

#                             OLS Regression Results                            
# ==============================================================================
# Dep. Variable:                    만족도  R-squared(설명력):                 0.588
# Model:                            OLS   Adj. R-squared:                  0.586
# Method:                 Least Squares   F-statistic:                     374.0
# Date:                Tue, 03 May 2022   Prob (F-statistic)(p-vlaue):  2.24e-52  모델이 유의한지 확인 < 0.05
# Time:                        10:19:52   Log-Likelihood:                -207.44
# No. Observations:                 264   AIC:(변수가 많을 때 이 값이 작을수록 좋음) 418.9
# Df Residuals:                     262   BIC:                             426.0
# Df Model:                           1                                         
# Covariance Type:            nonrobust                                         
# ==============================================================================
#                  coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# Intercept      0.7789      0.124      6.273      0.000       0.534       1.023
# 적절성            0.7393      0.038     19.340      0.000       0.664       0.815
# ==============================================================================
# Omnibus:                       11.674   Durbin-Watson:(잔차의 독립성 확인)     2.185    2에 가까을수록 좋음
# Prob(Omnibus):                  0.003   Jarque-Bera (JB):               16.003
# Skew:                          -0.328   Prob(JB):                     0.000335
# Kurtosis:                       4.012   Cond. No.(다중공성성)                13.4
# ==============================================================================

print(model.rsquared)   #하나씩 보기
print('실제 값', df.만족도[:5].values)
print('예측값:', model.predict()[:5])

#시각화
import numpy as np
import matplotlib.pyplot as plt

plt.scatter(df.적절성, df.만족도)
slope, intercept = np.polyfit(df.적절성, df.만족도,1)
plt.plot(df.적절성, df.적절성  * slope + intercept, 'b')

plt.show()