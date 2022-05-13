# [SVM 분류 문제] 심장병 환자 데이터를 사용하여 분류 정확도 분석 연습
#
# https://www.kaggle.com/zhaoyingzhu/heartcsv
# https://github.com/pykwon/python/tree/master/testdata_utf8         Heartcsv
#
# Heart 데이터는 흉부외과 환자 303명을 관찰한 데이터다. 
# 각 환자의 나이, 성별, 검진 정보 컬럼 13개와 마지막 AHD 칼럼에 각 환자들이 심장병이 있는지 여부가 기록되어 있다. 
# dataset에 대해 학습을 위한 train과 test로 구분하고 분류 모델을 만들어, 모델 객체를 호출할 경우 정확한 확률을 확인하시오. 
# 임의의 값을 넣어 분류 결과를 확인하시오.     
# 정확도가 예상보다 적게 나올 수 있음에 실망하지 말자. ㅎㅎ
#
# feature 칼럼 : 문자 데이터 칼럼은 제외
# label 칼럼 : AHD(중증 심장질환)

from sklearn import svm, metrics, preprocessing
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('../testdata/Heart.csv',index_col=0)
print(data.head(), data.shape)
print(data.info())
data = data.dropna()

dfx = data.drop(['AHD','Thal','ChestPain'], axis=1)
dfy = data['AHD']

print(dfx.head(3))
print(dfy[:3])

#더미화 
dfy = dfy.map({'No':0, 'Yes':1})
print(dfy[:3])


x_train, x_test, y_train, y_test = train_test_split(dfx, dfy, random_state = 1)
print(x_train.shape, x_test.shape)  #(222, 13) (75, 13)

# model C option = 오류 허용 정도를 지정하는 건데, 클수록 오류를 덜 허용하는
# 상황에 따라 C를 적절하게 선택해줘야 합니다. Noise가 많은 데이터라면 C를 작게 하는 것이 좋고, 
# Noise가 별로 없는 데이터라면 C를 크게 하는 것이 좋습니다.

model = svm.LinearSVC(C=1, random_state = 1).fit(x_train, y_train)
pred = model.predict(x_test)

print('실제값:', y_test[:10].values)
print('예측값:', pred[:10])

print('acc:', metrics.accuracy_score(y_test, pred)) #acc: 0.746666
print( metrics.classification_report(y_test, pred))





