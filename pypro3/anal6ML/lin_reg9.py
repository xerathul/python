# Linear Regression 으로 선형회귀모델 - mtcars dataset

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics._regression import r2_score, mean_squared_error
from statsmodels import api
import statsmodels
from matplotlib import pyplot as plt

mtcars = statsmodels.api.datasets.get_rdataset('mtcars').data
print(mtcars.head())
print(mtcars.corr())

print()
#hp가  mpg에 영향을 준다라고 가정하고 모델을 생성

x = mtcars[['hp']].values
print(x[:5])
y = mtcars['mpg'].values
print(y[:5])

# plt.scatter(x,y)
# plt.show()

# 원래는 train / test로 분리 해야하나 생략
lmodel = LinearRegression().fit(x,y)
print('회귀계수(slope):',lmodel.coef_)  #[-0.06822828]
print('회귀계수(intercept):',lmodel.intercept_) #30.098860539622496

pred = lmodel.predict(x)
print('예측값:', np.round(pred[:5],1))
print('실제값:', y[:5])
# 예측값: [22.6 22.6 23.8 22.6 18.2]
# 실제값: [21.  21.  22.8 21.4 18.7]

# 모델 성능 평가    
print('MSE: ', mean_squared_error(y, pred)) #13.989822298268805
print('r2_score:', r2_score(y, pred))   #r2_score: 0.602437341423934(설명력) 60%정도의 설명력

print()
# 새로운 데이터로 예측
new_hp = [[110]]
new_pred = lmodel.predict(new_hp)

print('%s 마력인 경우 예상 연비는 약 %s'%(new_hp[0][0], new_pred[0]))






