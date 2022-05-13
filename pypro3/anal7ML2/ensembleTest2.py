# [Randomforest 문제2]
#
# 중환자 치료실에 입원 치료 받은 환자 200명의 생사 여부에 관련된 자료다.
# 종속변수 STA(환자 생사 여부)에 영향을 주는 주요 변수들을 이용해 검정 후에 해석하시오. 
# 모델 생성 후 입력자료 및 출력결과는 Django를 사용하시오.
#
# 예제 파일 : https://github.com/pykwon  ==>  patient.csv
# <변수설명>
#   STA : 환자 생사 여부 (0:생존, 1:사망)
#   AGE : 나이
#   SEX : 성별
#   RACE : 인종
#   SER : 중환자 치료실에서 받은 치료
#   CAN : 암 존재 여부
#   INF : 중환자 치료실에서의 감염 여부
#   CPR : 중환자 치료실 도착 전 CPR여부
#   HRA : 중환자 치료실에서의 심박수
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection._search import GridSearchCV

cancer = pd.read_csv('../testdata/patient.csv')
print(cancer.info())

dfx = cancer.drop(['STA'], axis =1)
dfy = cancer['STA']

x_train, x_test, y_train, y_test = train_test_split(dfx, dfy)
print(x_train.shape, x_test.shape)
model= RandomForestClassifier().fit(x_train, y_train)
pred = model.predict(x_test)
