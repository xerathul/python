#MLP : 다층 신경망 (노드의 개수를 2개 이상)- 선형 / 비선형 예측 모델이 가능

import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier

feature = np.array([[0,0],[0,1],[1,0],[1,1]])
print(feature)

# label = np.array([0,0,0,1]) and
# label = np.array([0,1,1,1])     #or
label = np.array([0,1,1,0])     #xor    0.5

# ml = MLPClassifier(hidden_layer_sizes=10, activation='relu',solver = 'adam', learning_rate_init = 0.01)
ml = MLPClassifier(hidden_layer_sizes=(10,10,10), activation='relu',solver = 'adam', learning_rate_init = 0.01)
ml.fit(feature, label)
pred = ml.predict(feature)
print('pred',pred)
print('real',label)
print('acc',accuracy_score(label, pred))