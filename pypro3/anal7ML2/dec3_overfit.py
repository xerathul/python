# sklearn 모듈(라이브러리)이 지원하는 과적합 방지 함수(메소드)의 이해
# iris dataset을 사용

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection._split import train_test_split


iris = load_iris()
print(iris.keys())
train_data = iris.data
train_label = iris.target
print(train_data[:3])
print(train_label[:3])

#분류모델
dt_clf = DecisionTreeClassifier()   #sklearn의 다른 분류모델도 가능
dt_clf.fit(train_data, train_label)
pred = dt_clf.predict(train_data)
print('예측값:',pred)
print('실제값:',train_label)
print('분류 정확도:', accuracy_score(train_label, pred)) #실제값, 예측값 

# 정확도 100% : 과적합 문제 발생
# 모의고사 문제와 본고사 문제가 똑같음
# 모델의 포용성을 위해 과적합 문제를 해결하는 방안 
#참고 : 과적합 방지로 데이터 수를 늘릴 수 있다.
print('----과적합 방지 목적 처리 1 -----')
# train / test split (보통 7:3 or 8:2)
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, 
                                                    test_size = 0.3, random_state = 121)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape )  #(105, 4) (45, 4) (105,) (45,)
dt_clf.fit(x_train, y_train)    #모델 학습은 train data
pred2 = dt_clf.predict(x_test)  #모델 평가는 test data
print('예측값:',pred2)
print('실제값:',y_test)
print('분류 정확도:', accuracy_score(y_test, pred2)) #실제값, 예측값 분류 정확도: 0.955555555

print('----과적합 방지 목적 처리 2 -----')

#교차검증 : train/ test split 을 했으나, 여전히 과정합인 경우 -> 교차검증(k-fold)
# 본고사를 치르기 전에 모의고사를 여러번 보기 
# 모델학습 시 데이터의 편중을 방지하고자 학습데이터를 쪼개 학습과 평가를 병행
# 교차검증 중 가장 보편적인 방법으로 k-fold

from sklearn.model_selection._split import  KFold
import numpy as np

features = iris.data
label = iris.target
dt_clf=DecisionTreeClassifier(criterion = 'entropy', random_state = 123)
kfold = KFold(n_splits = 5)
cv_acc =[]
print('iris shape :', features.shape)    #iris shape : (150, 4)
# 전체 행 수가 150, 학습데이터 : 4/5(120개), 검증 데이터: 1/5(30개)

n_iter = 0

for train_index, test_index in kfold.split(features):
    # print('n_iter:',n_iter)
    # print('train_index:',len(train_index))
    # print('test_index:',len(test_index))
    # n_iter += 1
    xtrain, xtest = features[train_index], features[test_index]
    ytrain, ytest = label[train_index], label[test_index]
    
    dt_clf.fit(xtrain, ytrain)
    pred = dt_clf.predict(xtest)
    n_iter += 1
    # 반복할 때마다 정확도 측정
    acc = np.round(accuracy_score(ytest,pred),3)
    train_size = xtrain.shape[0]
    test_size = xtest.shape[0]
    print('반복수:{}, 교차검증 정확도:{}, 학습데이터 크기:{}, 학습데이터 크기:{}'.format(n_iter, acc, train_size, test_size))
    print('반복수:{}, validation data index:{}'.format(n_iter, test_index))
    cv_acc.append(acc)
    
print('평균검증 정확도:',np.mean(cv_acc))  #0.91999

print()
print('----과적합 방지 목적 처리 2-1 -----')
# 대출 사기 데이터인 경우 정상과 사기 데이터가 비율적으로 편향된 경우가 많다. 스팸이메일, 강우 여부
# 위와 같은 불균형 데이터인 경우는 KFold 보다는 StrarifiedKFold를 사용한다.
from sklearn.model_selection import StratifiedKFold
skfold = StratifiedKFold(n_splits = 5)
cv_acc = []
n_iter = 0

for train_index, test_index in skfold.split(features, label):

    xtrain, xtest = features[train_index], features[test_index]
    ytrain, ytest = label[train_index], label[test_index]
    
    dt_clf.fit(xtrain, ytrain)
    pred = dt_clf.predict(xtest)
    n_iter += 1
    # 반복할 때마다 정확도 측정
    acc = np.round(accuracy_score(ytest,pred),3)
    train_size = xtrain.shape[0]
    test_size = xtest.shape[0]
    print('반복수:{}, 교차검증 정확도:{}, 학습데이터 크기:{}, 학습데이터 크기:{}'.format(n_iter, acc, train_size, test_size))
    print('반복수:{}, validation data index:{}'.format(n_iter, test_index))
    cv_acc.append(acc)
    
print('평균검증 정확도:',np.mean(cv_acc))  #0.91999

print()
print('----과적합 방지 목적 처리 2-2 -----')
# cross_val_score를 이용하면 교차검증을 쉽게 할수 있다.
from sklearn.model_selection import cross_val_score

data = iris.data
label = iris.target

score = cross_val_score(dt_clf, data, label, scoring = 'accuracy', cv =5)
print('교차 검증별 정확도:', np.round(score, 3))
print('평균 검증 정확도: ', np.round(np.mean(score),3))

print('----과적합 방지 목적 처리 3 -----')
# GridSearchCV :교차 검증과 최적의 속성(하이퍼 파라미터)을 위한 튜닝을 한번에 처리
from sklearn.model_selection import GridSearchCV
# 여러개의 속성값 중 max_depth, min_samples_split 에 대해 최적의 값 찾기
parameters = {'max_depth':[1,2,3], 'min_samples_split':[2,3]}

grid_tree = GridSearchCV(dt_clf, param_grid = parameters, cv = 3, refit = True)
grid_tree.fit(x_train, y_train)

import pandas as pd
scores_df = pd.DataFrame(grid_tree.cv_results_)
# pd.set_option('max_columns', None)
print(scores_df)

print('GridSearchCV 의 최적 파라미터:', grid_tree.best_params_)
print('GridSearchCV 의 최고 정확도:', grid_tree.best_score_)

#dt_clf =DecisionTreeClassifier(..., max_depth = 3, min_samples_split = 2, ...)

# GridSearchCV 가 제공하는 최적의 파라미터로 모델(DecisionTreeClassifier) 생성
estimator = grid_tree.best_estimator_
print(estimator)
pred = estimator.predict(x_test)
print(pred)
print('모델 성능(정확도):', accuracy_score(y_test, pred))  #0.9555

