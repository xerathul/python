# 회귀분석 문제 5) 
#
# Kaggle 지원 dataset으로 회귀분석 모델(LinearRegression)을 작성하시오.
# testdata 폴더 : Consumo_cerveja.csv
# Beer Consumption - Sao Paulo : 브라질 상파울루 지역 대학생 그룹파티에서 맥주 소모량 dataset
# feature : Temperatura Media (C) : 평균 기온(C)
#             Precipitacao (mm) : 강수(mm)
# label : Consumo de cerveja (litros) - 맥주 소비량(리터) 를 예측하시오

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

data = pd.read_csv('../testdata/Consumo_cerveja.csv')
print(data.head(), data.shape)  #(941, 7)
print(data.columns)
data.dropna(inplace=True) #dropna를 하지 않으면 모델 생성시 오류
print()

x = data.loc[:,['Temperatura Media (C)','Precipitacao (mm)']]
x.columns = ['tempt','rain']
x['tempt']=x['tempt'].apply(lambda x:x.replace(',','.'))
x['rain']= x['rain'].apply(lambda x:x.replace(',','.'))


print(x[:3], type(x))
y = data[['Consumo de cerveja (litros)']]
y.columns=['beer']
print(y[:3], type(y))

#model 생성
lmodel = LinearRegression().fit(x,y)
print('회귀계수(slope):',lmodel.coef_)  #[[ 0.80190566 -0.07366404]]
print('회귀계수(intercept):',lmodel.intercept_) #[8.76264285]

pred = lmodel.predict(x)
print('예측값:', np.round(pred[:5],2).T, type(pred))   #[[30.65 30.43 28.67 27.9  27.86]]
print('실제값:', y[:5].T,type(y))  #r2_score: 0.37339445073731026

#성능평가
print('r2_score:', r2_score(y, pred))

#새로운 데이터로 예측
new_data= [[28,10],[26,0],[30,0]]
new_pred = lmodel.predict(new_data)
print(new_pred)