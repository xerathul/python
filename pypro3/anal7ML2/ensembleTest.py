# [Randomforest 문제1] 
# kaggle.com이 제공하는 'Red Wine quality' 분류 ( 0 - 10)
# dataset은 winequality-red.csv 
# https://www.kaggle.com/sh6147782/winequalityred?select=winequality-red.csv

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection._search import GridSearchCV

data = pd.read_csv('../testdata/winequality-red.csv')
print(data.head())
print(data.info())
print(data.describe())
xdf = data.drop(['quality'], axis = 1)
ydf= data['quality']

x_train, x_test, y_train, y_test = train_test_split(xdf, ydf, test_size = 0.3)
lmodel = LogisticRegression(solver = 'lbfgs', max_iter = 2000).fit(x_train, y_train)
demodel = DecisionTreeClassifier().fit(x_train, y_train)
rfmodel = RandomForestClassifier(n_estimators=200).fit(x_train, y_train)

lpredict = lmodel.predict(x_test)
print('LogisticRegression acc:{0:.5f}'.format(accuracy_score(y_test, lpredict)))
depredict = demodel.predict(x_test)
print('DecisionTreeClassifier acc:{0:.5f}'.format(accuracy_score(y_test, depredict)))
rfredict = rfmodel.predict(x_test)
print('RandomForestClassifier acc:{0:.5f}'.format(accuracy_score(y_test, rfredict)))

# LogisticRegression acc:0.56994
# DecisionTreeClassifier acc:0.57620
# RandomForestClassifier acc:0.68894


# min_samples_split : 노드 분할 최소 샘플 수?
# min_samples_leaf : 리프노드 최소 샘플 수?
# ...


print('-----------------')
# RandomForestClassifier
params = {'max_depth':[2,3,5,10,15],'min_samples_split':[2,3,5],'min_samples_leaf':[1,5,8]}
grid_clf2 = GridSearchCV(rfmodel, param_grid = params, scoring = 'accuracy', cv = 5)
grid_clf2.fit(x_train, y_train)
print(grid_clf2.best_params_)
print(grid_clf2.best_score_)
best_clf2 = grid_clf2.best_estimator_ #최적의 모델 얻기
bestPredict2 = best_clf2.predict(x_test)
print('RandomForestClassifier acc:{0:.5f}'.format(accuracy_score(y_test, bestPredict2))) #0.78771

 

