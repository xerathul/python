# 회귀분석 문제 2) 
# testdata에 저장된 student.csv 파일을 이용하여 세 과목 점수에 대한 회귀분석 모델을 만든다. 
# 이 회귀문제 모델을 이용하여 아래의 문제를 해결하시오.  수학점수를 종속변수로 하자.
#   - 국어 점수를 입력하면 수학 점수 예측
#   - 국어, 영어 점수를 입력하면 수학 점수 예측

import pandas as pd
import numpy as np
from statsmodels.formula.api import ols

data = pd.read_csv('../testdata/student.csv')
print(data.head(), data.shape)
model = ols('data.수학 ~ data.국어', data = data).fit()
print(model.summary())
#R-squared:                       0.587
#Prob (F-statistic):           8.16e-05


data.국어 = int(input('국어점수를 입력하세요:'))
pred = model.predict(pd.DataFrame({'국어':data.국어}))
#print(pred)
print('예측된 수학 점수:', pred[0])

model2 = ols('수학 ~ 국어 + 영어',data =data).fit()
print(model2.summary())
#R-squared:                        0.656
#Prob (F-statistic):            1.52e-05

data.국어, data.영어 = map(int, input('국어와 영어점수를 입력하세요').split())
pred2 = model2.predict(pd.DataFrame({'국어':data.국어,'영어':data.영어}))
# print(data.국어, data.영어)
print('국어, 영어 점수로 예측된 수학점수:',pred2[0])