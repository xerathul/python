# 인공 신경망 : 단층 신경망(뉴런 또는 노드 1개) - Perceptron
# input data * 가중치 의 합에 대해 임계값(활성화 함수)을 기준으로  이항 분류 가능

import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

feature = np.array([[0,0],[0,1],[1,0],[1,1]])
print(feature)

# label = np.array([0,0,0,1]) and
# label = np.array([0,1,1,1])     #or
label = np.array([0,1,1,0])     #xor    0.5

ml = Perceptron(max_iter = 10, eta0 = 0.1).fit(feature, label)    #max_iter = 1 최대 학습수, eta > runningdata
pred = ml.predict(feature)
print('pred:', pred)
print('label:', label)
print('acc:', accuracy_score(label, pred))  #0.75(학습수 1번) 1.0(학습수 10번)
