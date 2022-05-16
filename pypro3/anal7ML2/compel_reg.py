# sklearn 이 지원하는 예측모델(연속형)

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score

adver = pd.read_csv('../testdata/Advertising.csv', usecols=[1,2,3,4])
print(adver.head())
print(adver.info())
x = np.array(adver.loc[:, 'tv':'newspaper'])
print(x[:2])
y = np.array(adver.sales)
print(y[:2])

print()
lmodel = LinearRegression().fit(x, y)
lpred = lmodel.predict(x)
print('LinearRegression pred:', lpred[:5])
print('LinearRegression real:', y[:5])
print('r2_score :', r2_score(y, lpred)) #0.8972

print()
kmodel = KNeighborsRegressor(n_neighbors =3).fit(x, y)
kpred = kmodel.predict(x)
print('KNeighborsRegressor pred:', lpred[:5])
print('KNeighborsRegressor real:', y[:5])
print('r2_score :', r2_score(y, kpred)) #0.96801

print()
kmodel = KNeighborsRegressor(n_neighbors =3).fit(x, y)
kpred = kmodel.predict(x)
print('KNeighborsRegressor pred:', lpred[:5])
print('KNeighborsRegressor real:', y[:5])
print('r2_score :', r2_score(y, kpred)) #0.96801

print()
kmodel = KNeighborsRegressor(n_neighbors =3).fit(x, y)
kpred = kmodel.predict(x)
print('KNeighborsRegressor pred:', lpred[:5])
print('KNeighborsRegressor real:', y[:5])
print('r2_score :', r2_score(y, kpred)) #0.96801

print()
rmodel = RandomForestRegressor(n_estimators = 100, criterion = 'mse').fit(x, y)
rpred = rmodel.predict(x)
print('RandomForestRegressor pred:', rmodel[:5])
print('RandomForestRegressor real:', y[:5])
print('r2_score :', r2_score(y, rpred)) #0.9972

print()
xmodel = XGBRegressor(n_estimators = 100, criterion = 'mse').fit(x, y)
xpred = xmodel.predict(x)
print('XGBRegressor pred:', xpred[:5])
print('XGBRegressor real:', y[:5])
print('r2_score :', r2_score(y, xpred)) #0.99999966