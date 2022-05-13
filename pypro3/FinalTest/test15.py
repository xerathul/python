# [문항15] 의사결정나무 분석으로 classification과 regression에 모두 사용될 수 있다.
# 아래에 iris dataset으로 의사결정나무 분석을 하려 한다. 빈 칸을 채우시오. (배점:10)
# de_model = ①________________________   
# col = ['sepal length', 'sepal width','petal length','petal width']
# fit = de_model.fit(train_data[col], train_data['target_names'])
# pred = fit.②_______________(test_data[col])  # model 예측치
# ac_score = metrics.③______________________(test_data['target_names'], pred)
# print('분류 정확도 : ', ac_score)
import numpy as np
from sklearn import model_selection, datasets, tree, metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler #표준화지원
from sklearn.linear_model import LogisticRegression
import pandas as pd


iris = datasets.load_iris()
#print(iris.DESCR)
print(iris.keys())
print(iris.target_names)
col = ['sepal length', 'sepal width','petal length','petal width']

dfx = pd.DataFrame(iris.data, columns = col)
dfy = pd.DataFrame(iris.target)
df = pd.concat([dfx, dfy], axis = 1)
print(df.head(), df.shape)

x_train, x_test, y_train, y_test = train_test_split(dfx, dfy, test_size = 0.3, random_state =0)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)


de_model =  tree.DecisionTreeClassifier(criterion = 'entropy')
col = ['sepal length', 'sepal width','petal length','petal width']
fit = de_model.fit(x_train, y_train)
pred = fit.predict(x_train)  # model 예측치
ac_score = metrics.accuracy_score(y_train, pred)
print('분류 정확도 : ', ac_score)