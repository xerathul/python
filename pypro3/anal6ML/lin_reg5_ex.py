'''
회귀분석 문제 2) 
testdata에 저장된 student.csv 파일을 이용하여 세 과목 점수에 대한 회귀분석 모델을 만든다. 
이 회귀문제 모델을 이용하여 아래의 문제를 해결하시오.  수학점수를 종속변수로 하자.
  - 국어 점수를 입력하면 수학 점수 예측
  - 국어, 영어 점수를 입력하면 수학 점수 예측
'''

import pandas as pd
import statsmodels.formula.api as smf
from pandas.core.frame import DataFrame

df = pd.read_csv('../testdata/student.csv')
print(df.corr())  

model1 = smf.ols(formula="수학 ~ 국어", data=df).fit()
print(model1.summary())   

df.국어 = int(input("국어 점수를 입력하세요: "))
# print(df.국어.info())
# print(DataFrame({'국어':df.국어}))
predict_math = model1.predict(DataFrame({'국어':df.국어}))
print("예상수학점수: ", predict_math[0])

model2 = smf.ols(formula="수학 ~ 국어 + 영어", data=df).fit()
df.국어 = int(input("국어 점수를 입력하세요: "))
df.영어 = int(input("영어 점수를 입력하세요: "))

predict_math2 = model2.predict(DataFrame({'국어':df.국어, '영어': df.영어}))
print("예상수학점수: ", predict_math2[0])
