# 선형/ 비선형(다항)회귀 모델 : boston_housing dataset
import pandas as pd
import numpy as np
from sklearn.preprocessing._data import PolynomialFeatures
from sklearn.linear_model._base import LinearRegression
from sklearn.metrics._regression import r2_score
import matplotlib.pyplot as plt
plt.rc('font', family ='malgun gothic')

df = pd.read_csv('../testdata/housing.data', header=None, sep="\s+")
print(df.head(), df.shape)
df.columns = ['crim', 'zn','indus','chas','nox','rm','age','dis',
              'rad','tax','ptratio','b','lstat','medv']
print(df.corr())    #lstat, medv :-0.737663

x = df[['lstat']].values
y = df['medv'].values

print(x[:3])
print(y[:3])
model = LinearRegression()
# 다항특성
quad = PolynomialFeatures(degree =2)
cubic = PolynomialFeatures(degree =3)
x_quad = quad.fit_transform(x)
x_cubic = cubic.fit_transform(x)
print(x_quad[:2])
print(x_cubic[:2])

# 단순회귀
model.fit(x, y)
x_fit = np.arange(x.min(), x.max(), 1)[:,np.newaxis]
y_lin_fit = model.predict(x_fit)
print('단순회귀 예측값:', y_lin_fit[:3])
model_r2 = r2_score(y, model.predict(x))
print('단순회귀 model_r2:', model_r2)   # 0.54414629

# 다항회귀 : 2차
model.fit(x_quad, y)

y_quad_fit = model.predict(quad.fit_transform(x_fit))
q_r2 = r2_score(y, model.predict(x_quad))
print('다항회귀 : 2차 q_r2:', q_r2)   #0.640716

# 다항회귀 : 3차
model.fit(x_cubic, y)

y_cubic_fit = model.predict(cubic.fit_transform(x_fit))
c_r2 = r2_score(y, model.predict(x_cubic))
print('다항회귀 : 2차 c_r2:', c_r2)   #0.657847

#시각화 
plt.scatter(x, y, c='gray', label = 'train data')
plt.plot(x_fit, y_lin_fit, linestyle=':', label = 'linear(d=1), $R^2 =%.2f$'%model_r2, c='b', lw=3)
plt.plot(x_fit, y_quad_fit, linestyle='-', label = 'quad(d=2), $R^2 =%.2f$'%q_r2, c='r', lw=2)
plt.plot(x_fit, y_cubic_fit, linestyle='--', label = 'cubic(d=3), $R^2 =%.2f$'%c_r2, c='k', lw=3)
plt.xlabel('하위계층비율')
plt.ylabel('주택가격')
plt.legend()
plt.show()
