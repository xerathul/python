# iris dataset으로 선형회귀 분석
# 상관관계가 약한 경우/ 강한경우 분석 모델을 작성해 비교

import pandas as pd
import numpy as np
import seaborn as sns
from statsmodels.formula.api import ols
from matplotlib import pyplot as plt

iris = sns.load_dataset('iris')
print(iris.head(), iris.shape)  #(150, 5)
print(iris.corr())

#단순 선형회귀
# 1 상관관계가 약한 두 변수
result1 = ols(formula = 'sepal_length ~ sepal_width', data =iris).fit()
print(result1.summary())
#Prob (F-statistic):              0.152 >유의하지 않은 모델
#R-squared:                       0.014 > 두 변수의 설명력이 매우 약함

# plt.scatter(iris.sepal_width, iris.sepal_length)
# plt.show()

# 1 모델은 의미가 없는 모델
print('실제 값:', iris.sepal_length[:5].values)
print('예측 값:', result1.predict()[:5])
print('--------------------------')

# 2 상관관계가 강한 두 변수
result2 = ols(formula = 'sepal_length ~ petal_length', data =iris).fit()
print(result2.summary())
#Prob (F-statistic):           1.04e-4 < 0.05 => 유의한 모델
#R-squared:                       0.760 > 두 변수의 설명력이 강함

# plt.scatter(iris.petal_length, iris.sepal_length)
# plt.show()

# 1 모델은 의미가 있는 모델
print('실제 값:', iris.sepal_length[:5].values)
print('예측 값:', result2.predict()[:5])

# 새로운 값(petal_length) 으로 미지의 sepal_length 값 얻기
newData = pd.DataFrame({'petal_length':[1.1, 0.5, 5.0]})
yPred = result2.predict(newData)
print('예측결과:',yPred.values)

print('-----------------')

# 다중 선형회귀: 독립변수 복수
# result3 =ols(formula = 'sepal_length ~ petal_length+petal_width+sepal_width', data =iris).fit()
# print(result3.summary())
#Prob (F-statistic):           8.59e-62 < 0.05 => 유의한 모델
#R-squared:                       0.856 > 두 변수의 설명력이 강함

# 여러개의 독립변수는 join을 사용
column_select = '+'.join(iris.columns.difference(['sepal_length','species']))
print(column_select)
result3 =ols(formula = 'sepal_length ~ '+column_select, data =iris).fit()
print(result3.summary())
