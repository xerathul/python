# 단순 선형회귀 모델 : Keras 모듈 

import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers
import numpy as np

x_data = [1.,2.,3.,4.,5.]
y_data = [1.2,2.0,3.0,3.5,5.5]
print(np.corrcoef(x_data, y_data))  #0.97494

model = Sequential()
model.add(Dense(units=1, input_dim = 1, activation = 'linear'))

model.compile(optimizer='sgd', loss='mse', metrics=['mse'])     #mse 평균제곱 오차
model.fit(x_data, y_data, batch_size = 1, epochs= 300, verbose=2)
print(model.evaluate(x_data, y_data))

pred = model.predict(x_data)
print('pred:',pred.flatten())
print('real:', y_data)
from sklearn.metrics import r2_score
print('설명력:', r2_score(y_data, pred))   #설명력: 0.946710

print()
new_x =[3.5,9.0]
print('새로운 예측결과:',model.predict(new_x).flatten())

import matplotlib.pyplot as plt
plt.plot(x_data, y_data, 'ro', label='real')
plt.plot(x_data, pred, 'b-', label='pred')
plt.legend()
plt.show()
