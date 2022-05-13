#titanic dataset으로 LogisticRegression, DecisionTreeClassifier, RandomForestClassifier

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.tests.test_x13 import dataset

df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/titanic_data.csv')
print(df.head(), df.shape)  #(891, 12)
print(df.info())
df.drop(columns=['PassengerId','Name','Ticket'], inplace=True)
print(df.shape) #(891, 9)
pd.set_option('display.max_columns',None)
print(df.describe())
print(df.info())
print(df.isnull().sum())    #Age:177, Cabin:687, Embarked:2

# Null 처리: 0 또는 평균 또는 제거 또는 임의의 값으로 대체
df['Age'].fillna(df['Age'].mean(), inplace = True)
df['Cabin'].fillna('N', inplace=True)
df['Embarked'].fillna('N', inplace=True)
print(df.isnull().sum())

print()
#object type : Sex,Cabin, Embarked 이 칼럼들의 상태를 별도 확인
print('Sex:\n', df['Sex'].value_counts())    #male :577, female: 314
print('Cabin:\n', df['Cabin'].value_counts()) 
df['Cabin'] = df['Cabin'].str[:1]
print('Cabin:\n', df['Cabin'].value_counts()) 
print('Embarked:\n', df['Embarked'].value_counts())
print(df.head())

#성별이 생존확률에 어떤 영향을 가했는가?
print(df.groupby(['Sex','Survived'])['Survived'].count())
# 승객은 남자가 많지만, 생존자는 여자가 많음을 알 수있다.
print('여자 생존율;', 233 / (81 + 233))  #0.74203
print('남자 생존율;',109 / (468 + 109))  #0.18890

# #시각화: 성별 생존 확률
# sns.barplot(x= 'Sex', y = 'Survived', data = df, ci = 95)
# plt.show()
#
# #시각화 : 성별, class별 생존 확률
# sns.barplot(x= 'Pclass', y = 'Survived', data = df, hue = 'Sex', ci = 95)
# plt.show()

# 나이별 생존 확률
# print(df['Age'])
def ageCategory(age):
    msg = ''
    if age <= -1: msg ='unknown'
    elif age <= 7: msg ='baby'
    elif age <= 18: msg ='teenager'
    elif age <= 65: msg ='adult'
    else: msg = 'elder'
    return msg

df['ageCategory'] = df['Age'].apply(lambda a: ageCategory(a))
# print(df.head())

#시각화 : 나이별 생존 확률
# sns.barplot(x= 'ageCategory', y = 'Survived', data = df, hue = 'Sex', ci = 95,        
#             order =['unknown','baby','teenager','adult','elder'])
# plt.show()

del df['ageCategory']

# Dummy 변수 : 문자열 -> 숫자(범주형)
from sklearn import preprocessing

def labelIncode(datas):
    cols = ['Cabin','Sex','Embarked']
    for c in cols:
        la = preprocessing.LabelEncoder().fit(datas[c])
        datas[c] = la.transform(datas[c])
    return datas

df = labelIncode(df)
print(df.head(), type(df))
print(df['Cabin'].unique())     #[7 2 4 6 3 0 1 5 8]
print(df['Sex'].unique())       #[1 0]
print(df['Embarked'].unique())  #[3 0 2 1]

# 데이터 가공

print()
from sklearn.model_selection import train_test_split
feautureDf = df.drop(['Survived'], axis = 'columns')
labelDf = df['Survived']
print(feautureDf.head())
print(labelDf.head())

x_train, x_test, y_train, y_test= train_test_split(feautureDf, labelDf, test_size= 0.2, random_state = 1)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) #(712, 8) (179, 8) (712,) (179,)

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

lmodel = LogisticRegression(solver = 'lbfgs', max_iter = 500).fit(x_train, y_train)
demodel = DecisionTreeClassifier().fit(x_train, y_train)
rfmodel = RandomForestClassifier().fit(x_train, y_train)

lpredict = lmodel.predict(x_test)
print('LogisticRegression acc:{0:.5f}'.format(accuracy_score(y_test, lpredict)))
depredict = demodel.predict(x_test)
print('DecisionTreeClassifier acc:{0:.5f}'.format(accuracy_score(y_test, depredict)))
rfredict = rfmodel.predict(x_test)
print('RandomForestClassifier acc:{0:.5f}'.format(accuracy_score(y_test, rfredict)))

print('\nGridSearchCV -----')
from sklearn.model_selection import GridSearchCV

# min_samples_split : 노드 분할 최소 샘플 수?
# min_samples_leaf : 리프노드 최소 샘플 수?
# ...

# DecisionTreeClassifier
params = {'max_depth':[2,3,5,10,15],'min_samples_split':[2,3,5],'min_samples_leaf':[1,5,8]}
grid_clf = GridSearchCV(demodel, param_grid = params, scoring = 'accuracy', cv = 5)
grid_clf.fit(x_train, y_train)
print(grid_clf.best_params_)
print(grid_clf.best_score_)
best_clf = grid_clf.best_estimator_ #최적의 모델 얻기
bestPredict = best_clf.predict(x_test)
print('DecisionTreeClassifier acc:{0:.5f}'.format(accuracy_score(y_test, bestPredict))) #0.80447

print('-----------------')
# RandomForestClassifier
grid_clf2 = GridSearchCV(rfmodel, param_grid = params, scoring = 'accuracy', cv = 5)
grid_clf2.fit(x_train, y_train)
print(grid_clf2.best_params_)
print(grid_clf2.best_score_)
best_clf2 = grid_clf2.best_estimator_ #최적의 모델 얻기
bestPredict2 = best_clf2.predict(x_test)
print('RandomForestClassifier acc:{0:.5f}'.format(accuracy_score(y_test, bestPredict2))) #0.78771
