#ROC curve (모델 성능파악)
# ROC(Receiver Operating Characteristic) curve는 다양한 threshold에 대한 이진분류기의 성능을 한번에 표시한 것이다.
# 이진 분류의 성능은 True Positive Rate와 False Positive Rate 두 가지를 이용해서 표현하게 된다.
# ROC curve를 한 마디로 이야기하자면 ROC 커브는 좌상단에 붙어있는 커브가 더 좋은 분류기를 의미한다고 생각할 수 있다.
from sklearn.datasets._samples_generator import make_classification
from sklearn.linear_model._logistic import LogisticRegression
import numpy as np
import pandas as pd

#분류 연습용 샘플데이터 작성

x, y = make_classification(100, n_features=2, n_redundant = 0,random_state = 123)
print(x[:3])
print(y[:3])

model = LogisticRegression().fit(x,y)
y_hat = model.predict(x)
print('y_hat : ', y_hat[:3])

import matplotlib.pyplot as plt
# plt.scatter(x[:,0],x[:,1])
# plt.show()

print()
f_value = model.decision_function(x)    #결정합수(판별함수): 불확성 추정함수 - 판별 경계선 설정을 위함
print(f_value[:5])
df = pd.DataFrame(np.vstack([f_value, y_hat, y]).T, columns = ['f','y_hat','y'])
print(df.head())

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y, y_hat))
acc = (44 + 44)/100         #TP + TN / ALL 정확도
recall = 44 /( 44+ 4)       # TP / TP +FN 재현도, 민감도
specificity = 44 / (8+ 44)  #TN / FP + TN 특이도
fallout = 8/ ( 8 + 44 )     #FP / (FP + TN)    #위양성률

print('acc(정확도):', acc)
print('recall(재현도, 민감도):', recall)  #TPR : 전체 양성 샘플 중에 양성으로 에측된 비율
print('specificity(특이도):',specificity)
print('fallout(위양성률):', fallout)    #FPR(1-특이도) : 전체 음성 샘플 중에 양성으로 잘못 예측된 것의 비율
# TPR은 1에 가까울수록 좋고, FPR은 0에 가까울 수록 좋다.
print()

from sklearn import metrics
ac_sco = metrics.accuracy_score(y, y_hat)
print('ac_sco:', ac_sco)
cl_rep = metrics.classification_report(y, y_hat)
print('cl_rep\n:',cl_rep)

print()
fpr, tpr, thresholds = metrics.roc_curve(y, model.decision_function(x))
print('fpr',fpr)
print('tpr',tpr)
print('thresholds',thresholds)  #분류 결정 임계값

# ROC curve 시각화
plt.plot(fpr, tpr, 'o-', label = "LogisticRegression")
plt.xlabel('fpr')
plt.ylabel('tpr')
plt.title('ROC curve')
plt.plot([0,1],[0,1],'k--', label = 'random classifier line(AUC: 0.5)')
plt.plot([fallout],[recall],'r+', ms = 20)
plt.legend()

plt.show()

#AUC(Area Under the ROC Curve) 는 ROC의 curve 밑면적을 말한다.
#성능 평가에 있어 수치적인 기준이 될 수 있는 값으로 1에 가까울수록 그래프 가 좌상단에 근접하게 되므로 좋은 모델이라고 할 수 있다.\
print('AUC:', metrics.auc(fpr, tpr))    #AUC: 0.954727

# 해석 : ...
