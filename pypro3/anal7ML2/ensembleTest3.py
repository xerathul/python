# [XGBoost 문제] 
# kaggle.com이 제공하는 'glass datasets'
# 유리 식별 데이터베이스로 여러 가지 특징들에 의해 7가지의 label(Type)로 분리된다.
# glass.csv 파일을 읽어 분류 작업을 수행하시오.

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from xgboost import plot_importance
from lightgbm import LGBMClassifier
import matplotlib.pyplot as plt
import xgboost as xgb
from sklearn.metrics._classification import accuracy_score,\
    classification_report
from sklearn import preprocessing

data = pd.read_csv('../testdata/glass.csv')
print(data.info(), data.shape)

dfx = data.drop(['Type'], axis = 1)
dfy = data['Type']
print(dfx.head(2))
print(dfy.head(2))
print(dfy.unique(), type(dfy))

#dummy
dfy = preprocessing.LabelEncoder().fit(dfy).transform(dfy)

print(np.unique(dfy))
x_train, x_test, y_train, y_test =train_test_split(dfx, dfy)
print(x_train.shape, x_test.shape)  #(160, 9) (54, 9)

model = xgb.XGBClassifier(booster = 'gbtree', n_estimators = 500).fit(x_train, y_train)
#print(model)
pred = model.predict(x_test)
print('예측값:', pred[:10])
print('실제값:', y_test[:10])
print('분류 정확도 :', accuracy_score(y_test, pred))
print('분류 보고서 :\n', classification_report(y_test, pred))

#시각화
fig, ax = plt.subplots(figsize = (10,12))
plot_importance(model, ax = ax)
plt.show()