# 회귀분석 문제 5) 
#
# Kaggle 지원 dataset으로 회귀분석 모델(LinearRegression)을 작성하시오.
# testdata 폴더 : Consumo_cerveja.csv
# Beer Consumption - Sao Paulo : 브라질 상파울루 지역 대학생 그룹파티에서 맥주 소모량 dataset
# feature : Temperatura Media (C) : 평균 기온(C)
#             Precipitacao (mm) : 강수(mm)
# label : Consumo de cerveja (litros) - 맥주 소비량(리터) 를 예측하시오

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics._regression import r2_score, mean_squared_error
from statsmodels import api
import statsmodels
from matplotlib import pyplot as plt

data = pd.read_csv('../testdata/Consumo_cerveja.csv')
print(data.head(), data.shape)  #(941, 7)
print(data.columns)

print()
x = data[['Temperatura Media (C)','Precipitacao (mm)']]
x.columns = ['tempt','rain']
x['tempt']=x['tempt'].apply(lambda x:x.replace(',','.'))
x['rain']= x['rain'].apply(lambda x:x.replace(',','.'))


print(x[:3], type(x.tempt[0]))
y = data[['Consumo de cerveja (litros)']]
y.columns=['beer']
print(y[:3], type(y))

#model 생성
lmodel = LinearRegression().fit(x,y)
print('회귀계수(slope):',lmodel.coef_)  #[-0.06822828]
print('회귀계수(intercept):',lmodel.intercept_) #30.098860539622496