#로지스틱 회귀분석
#분류모델 :이항분류가 기본
#독립변수 : 연속형, 종속변수 : 범주형
# 출력된 연속형 자료를 logit변환해 sigmoid function 함수로 0~1사이의 실수 값이 나오도록 한후
# 0.5를 기준으로 분류

import math
from statsmodels import api as sm
import numpy as np
from sklearn.metrics._classification import accuracy_score
def sigmoid(x):
    return 1/ (1+math.exp(-x))

print(sigmoid(3))
print(sigmoid(1))
print(sigmoid(-2))
print(sigmoid(-5))
#======================================

#mtcars dataset으로 분류작업 

mtcarData = sm.datasets.get_rdataset('mtcars')
print(mtcarData.keys())
mtcars = sm.datasets.get_rdataset('mtcars').data
print(mtcars.head(3))
print(mtcars['am'].unique())    #[1 0] 자동 수동
mtcar = mtcars.loc[:,['mpg','hp','am']]
print(mtcar.head(3))

#연비와 마력수에 따른 변속기 분류
#모델작성 방법1 : logit()

import statsmodels.formula.api as smf
fomula = 'am ~ mpg + hp'
result = smf.logit(formula = fomula, data = mtcar).fit()
print(result)
print(result.summary())
# print('예측값: ', result.predict())
pred = result.predict(mtcar[:10])

#print('예측값: ', pred.values)
print('예측값: ', np.around(pred.values))
print('실제값: ', mtcar['am'][:10].values)

print()
conf_tab = result.pred_table()
print('confusion matrix : \n',conf_tab)

#모델의 분류정확도(accuracy)
print('정확도 1:', (16+10)/len(mtcar))
print('정확도 2:', (conf_tab[0][0] + conf_tab[1][1])/len(mtcar))

pred2 = result.predict(mtcar)
print('정확도3: ', accuracy_score(mtcar['am'], np.around(pred2)))

#모델작성 방법2 : glm() : generalized linear model(일반화된 선형모델)
result2 = smf.glm(formula = fomula, data = mtcar, family = sm.families.Binomial()).fit() #이항분포
print(result2.summary())


print('예측값:',np.around(pred2.values))
print('예측값:',np.rint(pred2.values))
print('실제값:',mtcar['am'][:10].values)

pred3 = result2.predict(mtcar)
print('정확도3: ', accuracy_score(mtcar['am'], np.around(pred3)))

print('새로운 연비와 마력수에 대한 분류결과---')
#1. 기존값 일부 수정
newdf = mtcar.iloc[:2].copy()
print(newdf)
newdf['mpg']=[10,30]
newdf['hp']=[100,90]
new_pred = result2.predict(newdf)
print('new_pred : ', new_pred.values)
print('new_pred : ', np.rint(new_pred.values))

print()
#2. 별도 작성
import pandas as pd

newdf2 = pd.DataFrame({'mpg':[10,35,50,5],'hp':[80,100,70,150]})
new_pred2 = result2.predict(newdf2)
print('new_pred : ', np.rint(new_pred2.values))

