#모델 맛보기 4: linregress 를 사용. model 생성 o
from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#IQ에 따른 시험 성적 값 예측
score_iq = pd.read_csv('../testdata/score_iq.csv')
print(score_iq.info())
print(score_iq.head(3), score_iq.shape)  #(150, 6)

x = score_iq.iq
y = score_iq.score

#상관계수 확인
print(np.corrcoef(x, y)[0,1])    #numpy 0.882220
print(score_iq.corr())      #pandas 0.882220

#시각화
# plt.scatter(x,y)
# plt.show()

#선형회귀분석
model = stats.linregress(x, y)
print(model)
print('x slope:', model.slope, 'y bias:',model.intercept)   #x slope: 0.6514309527270085 y bias: -2.8564471221975936
print('p-value:', model.pvalue)     #p-value: 2.8476895206672287e-50 < 0.05 유의한 모델

# y = model.slope*x + model.intercept
print('IQ에 따른 점수 예측 :',model.slope * 140 + model.intercept)
print('IQ에 따른 점수 예측 :',model.slope * 120 + model.intercept)

#linregress는 predict를 지원하지 않음
#그래서 numpy의 polyval을 사용
print('IQ에 따른 점수 예측 :',np.polyval([model.slope, model.intercept],140))
newdf = pd.DataFrame({'iq':[55,66,77,88,150]})
print('새로운 점수 예측:', np.polyval([model.slope, model.intercept], newdf))
