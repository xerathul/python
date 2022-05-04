# Advertising.csv: 여러 매채에 광고비 사용에 따른 판매량 추정치 얻기
from statsmodels.formula.api import ols
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.stats.outliers_influence import variance_inflation_factor,\
    OLSInfluence
from statsmodels import api
plt.rc('font', family = 'malgun gothic')


advdf = pd.read_csv('../testdata/Advertising.csv')
print(advdf.head(), advdf.shape)    #(200, 5)

print('상관계수 (r):', advdf.loc[:, ['sales','tv']].corr()) #0.782224
print('상관계수 (r):', advdf.loc[:, ['sales','newspaper']].corr())  #0.228299
print('상관계수 (r):', advdf.loc[:, ['sales','radio']].corr())  #0.576223

print()

#단순 선형회귀
lm = ols('sales ~ tv', data = advdf).fit()
print(lm.summary())
print('설명력 :',lm.rsquared)
print('p값 : ', lm.pvalues[1])
# 설명력 : 0.611875050850071
# p값 :  1.467389700194655e-42

#시각화
# plt.scatter(advdf.tv, advdf.sales)
# plt.xlabel('tv')
# plt.ylabel('sales')
# x = pd.DataFrame({'tv':[advdf.tv.min(),advdf.tv.max()]})
# y_pred = lm.predict(x)
# plt.plot(x, y_pred, c = 'red')

# 미지의 tv 광고비에 따른 상품 판매량
x_new = pd.DataFrame({'tv':[220.12, 55.66,10]})
pred_new = lm.predict(x_new)
print('sales 예측값:', pred_new.values)

print('------------------')
print(advdf.corr()) #sales와의 상관관계 : tv > radio > newspaper
lm_mul = ols('sales ~ tv + radio + newspaper',data = advdf).fit()
print(lm_mul.summary())
print('설명력 :',lm_mul.rsquared)
print('p값 : ', lm_mul.pvalues[1])
# 설명력 : 0.896
# p값 :  1.5099599548140058e-81
#newspaper P>|t|: 0.860 > 0.05 이므로 독립변수에서 제거 고려

lm_mul = ols('sales ~ tv + radio',data = advdf).fit()
print(lm_mul.summary())     #Adj. R-squared: 0.896 Prob (F-statistic):  4.83e-98
# newspapers는 모델의 성능에 영향을 주지 못하는 변수

# 새로운 독립변수 값으로 종속변수 sales 예측
x_new2 = pd.DataFrame({'tv':[220.12, 55.66,10],'radio':[30.3, 40.4, 50.5]})
pred_new2 = lm.predict(x_new2)
print('sales 예측값2:', pred_new2.values)

print('**********선형회귀분석의 기존 가정 충족 조건****************')
# . 선형성 : 독립변수(feature)의 변화에 따라 종속변수도 일정 크기로 변화해야 한다.
# . 정규성 : 잔차항이 정규분포를 따라야 한다.
# . 독립성 : 독립변수의 값이 서로 관련되지 않아야 한다.
# . 등분산성 : 그룹간의 분산이 유사해야 한다. 독립변수의 모든 값에 대한 오차들의 분산은 일정해야 한다.
# . 다중공선성 : 다중회귀 분석 시 두 개 이상의 독립변수 간에 강한 상관관계가 있어서는 안된다.

# 잔차항 구하기 (예측값 - 실제값)
fitted = lm_mul.predict(advdf.iloc[:, 0:3])
# print(advdf.iloc[:, 0:3])
#print(fitted)
residual = advdf['sales'] - fitted
# print(residual)
print(np.mean(residual))    #1.1191048088221578e-15 0에근사

print('선형성 : 예측값과 잔차의 분포가 유사 해야 함---')
sns.regplot(fitted, residual, lowess = True, line_kws ={'color':'red'})   #선형회귀 모델의 적합성을 그릴 때 사용 - 잔차의 추세선을 시각화
plt.plot([fitted.min(), fitted.max()], [0,0], '--', color = 'grey')  #평균선
plt.show()
# 선형성을 만족하지 못함 : 다항회귀(비선형) 모델을 추천 - polynomialFeatures

print('정규성: 잔차항이 정규분포를 따라야 함')
sr = stats.zscore(residual)
(x, y), _ = stats.probplot(sr)
sns.scatterplot(x, y)
plt.plot([-3,3],[-3,3], '--',color = 'gray')
plt.show()
# 잔차가 정규성을 만족하지 않음: 데이터에 대해 표준화, 정규화, log를 씌우는 등의 작업을 시도
print('shapiro test: ',stats.shapiro(residual))
#shapiro test:  ShapiroResult(statistic=0.9180378317832947, pvalue=4.190036317908152e-09)
#pvalue=4.190036317908152e-09 < 0.05 이므로 정규성을 만족하지 못함

print(' 독립성 : 잔차가 자기 상관을 따르는지 확인 Durbin-Watson =0 ~ 4===')
# 독립성 : 독립변수의 값이 서로 관련되지 않아야 한다.
#Durbin-Watson:  2.081 2에 가까울수록 독립적 그러므로 독립성 만족

print('\n등분산성: 잔차의 분산이 일정해야 한다.')
sr = stats.zscore(residual)
sns.regplot(fitted, np.sqrt(np.abs(sr)), lowess = True, line_kws ={'color':'red'})
plt.show()
#등분산성 만족 못함 : 비선형인지 확인, 이상값 확인, 정규성 확인
#정규성은 만족하나 등 분산성은 만족하지 못한 경우 가중회귀분석(weighted regression)

print('\n다중 공선성: 독립변수들 간에 강한 상관관계가 없어야 함')
print(variance_inflation_factor(advdf.values, 2))   #tv 12.959997522373275
print(variance_inflation_factor(advdf.values, 3))   #radio 3.159805234217253

#VIF(Variable Inflation Factors: 분산 팽창 계수) 값 확인 : 10을 넘으면 다중 공선성을 의심
vifdf = pd.DataFrame()
vifdf['vif_value'] = [variance_inflation_factor(advdf.values, i) for i in range(2,4)]
print(vifdf)

print('\n 참고: 극단치 확인- ',"Cook's distance" )
cd, _ =OLSInfluence(lm_mul).cooks_distance   #극단값을 나타내는 지표 반환
print(cd.sort_values(ascending = False).head())

api.graphics.influence_plot(lm_mul, criterion='cooks')
plt.show()

print(advdf.iloc[[130,5,35,178,126]])
