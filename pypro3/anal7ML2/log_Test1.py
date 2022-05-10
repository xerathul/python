# [로지스틱 분류분석 문제2] 
# 게임, TV 시청 데이터로 안경 착용 유무를 분류하시오.
# 안경 : 값0(착용X), 값1(착용O)
# 예제 파일 : https://github.com/pykwon  ==>  bodycheck.csv
# 새로운 데이터(키보드로 입력)로 분류 확인. 스케일링X

import pandas as pd
from sklearn.model_selection._split import train_test_split
from statsmodels import api as sm
import statsmodels.formula.api as smf
import numpy as np
from sklearn.linear_model._logistic import LogisticRegression

data = pd.read_csv('../testdata/bodycheck.csv')
# print(data.head(), data.shape)  #(20, 6)
data = data[['게임','TV시청','안경유무']]
# print(data.head())

arr = data.values
x = arr[:,:2]
y = arr[:, 2]
# print(x, y)
formula = '안경유무 ~ 게임 + TV시청'
# model = smf.glm(formula = formula, data = data ,family=sm.families.Binomial()).fit()
# print(model)
# print(model.summary())
model = LogisticRegression()
model.fit(x, y)
print('예측값:', model.predict(x[:5]))
print('실제값:', y[:5])
print((model.predict(x) !=y).sum())   #다맞음?
print('분류 정확도:', model.score(x, y))

a, b = map(int,input('새로운 데이터를 입력하세요(게임시간 TV시청):').split())
# print(a, b)
newData = np.array([[a,b]])
# print(newData)
if model.predict(newData)[0] == 0:
    print('안경을 착용하지 않은것으로 예상됩니다.')
else:
    print('안경을 착용한 것으로 예상됩니다.')

