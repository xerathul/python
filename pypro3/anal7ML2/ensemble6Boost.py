# ** XGBoost는 Gradient Boosting 알고리즘을 분산 환경에서도 실행할 수 있도록 구현해 놓은 라이브러로 
# Regression, Classification 문제를 모두 지원하며, 성능과 자원 효율이 좋아서 인기 있는 알고리즘이다.
# RandomForest와 마찬가지로 XGBoost는 여러 개의 Decision Tree를 조합해서 사용하는 Ensemble 알고리즘이다.
#pip install xgboost
# pip install lightbm

# brest_cancer dataset
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from xgboost import plot_importance
from lightgbm import LGBMClassifier
import matplotlib.pyplot as plt
import xgboost as xgb
from sklearn.metrics._classification import accuracy_score,\
    classification_report

data = load_breast_cancer()
x_feature = data.data
y_label = data.target
# print(data.feature_names)

cancer_df = pd.DataFrame(data = x_feature, columns=data.feature_names)
pd.set_option('max_columns', None)
print(cancer_df.head(2), cancer_df.shape)   #(569, 30)
print(data.target_names)    #['malignant' 'benign'] 양성/ 악성
print(np.sum(y_label == 0)) #212
print(np.sum(y_label == 1)) #357

x_train, x_test, y_train, y_test = train_test_split(x_feature, y_label, test_size = 0.2,
                                                    random_state = 12)#디폴트 
print(x_train.shape, x_test.shape)  #(455, 30) (114, 30)

#gbtree - 의사결정 기반 옵션 선형이면 leaner 도 가능
model = xgb.XGBClassifier(booster = 'gbtree', max_depth = 6, n_estimators = 500).fit(x_train, y_train)
#model = LGBMClassifier(booster = 'gbtree', max_depth = 6, n_estimators = 500).fit(x_train, y_train)

print(model)
pred = model.predict(x_test)
print('예측값:', pred[:10])
print('실제값:', y_test[:10])
print('분류 정확도 :', accuracy_score(y_test, pred))
print('분류 보고서 :\n', classification_report(y_test, pred))

# #시각화
# fig, ax = plt.subplots(figsize = (10,12))
# plot_importance(model, ax = ax)
# plt.show()