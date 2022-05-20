# 다중선 선형회귀 : 주식 데이터로 회귀 모델 작성. 하루 전 데이터로 다음날 종가 예특
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

xy = np.loadtxt("../testdata/stockdaily.csv", delimiter= ',', skiprows = 1)
print(xy[:2], len(xy))  #numpy.ndarray

scaler = MinMaxScaler(feature_range=(0,1))  #정규화
xy = scaler.fit_transform(xy)
print(xy[:2], len(xy))  


x = xy[:,0:-1]  #open, High, Low, Volume: feature
y = xy[:,[-1]]
print(x[:2])
print(y[:2])
print(x[0], y[0])
print(x[1],y[1])
print()
x = np.delete(x, -1, 0) #마지막행 지우기
y = np.delete(y, 0)     #0번째 행 삭제
print(x[0], y[0])

print('---------')
model = Sequential()
model.add(Dense(units = 1, input_dim = 4, activation = 'linear'))

model.compile(optimizer = 'sgd', loss = 'mse', metrics = ['mse'])
model.fit(x, y, epochs=100, verbose = 0)
print('evaluate', model.evaluate(x, y))

print(x[10])
test = x[10].reshape(-1,4)
print('실제값:', y[10])
print('예측값:', model.predict(test).flatten())
print()
pred = model.predict(x)

from sklearn.metrics import r2_score
print('r2_score:', r2_score(y, pred))   #0.98503 과적합? 의심

# plt.plot(y, 'b')
# plt.plot(pred, 'r--')
# plt.show()

print('\n과적합 방지를 목적으로 train/ test로 분리 -----')
# train test split 을 쓰지않는이유? shuffle 시계열 데이터는 섞이면 안됨(순서가 있는 데이터)
from sklearn.model_selection import train_test_split
a,b,c,d, = train_test_split(x, y, shuffle = False)
print(a.shape, b.shape)     #(548, 4) (183, 4)

#수동으로 하는방법
train_size = int(len(x)*0.7)
test_size =len(x)- train_size
print(train_size, test_size)    #551 220
x_train, x_test = x[0:train_size], x[train_size:len(x)]
print(x[:2])
print(x_train[:2], x_train.shape, x_test[:2], x_test.shape)
print()
y_train, y_test = y[0:train_size], y[train_size:len(y)]
print(y[:2])
print(y_train[:2], y_train.shape, y_test[:2], y_test.shape)

print('------------------------------------------------------')
model2 = Sequential()
model2.add(Dense(units = 1, input_dim = 4, activation = 'linear'))

model2.compile(optimizer = 'sgd', loss = 'mse', metrics = ['mse'])
model2.fit(x_train, y_train, epochs=100, verbose = 0)
print('evaluate', model2.evaluate(x_test, y_test))

print(x_test[10])
test = x_test[10].reshape(-1,4)
print('실제값:', y_test[10])
print('예측값:', model2.predict(test).flatten())
print()
pred2 = model2.predict(x_test)


print('after split - r2_score:', r2_score(y_test, pred2))   # 0.62470 과적합 의심 해제

print('-----------------------------------------------')
# fit (학습) 도중에 검증도 함께 하고자 할 경우, train data를 다시 분리해 validation data 를 운영할 수 있다.
# 과적합 방지 목적

model3 = Sequential()
model3.add(Dense(units= 1, input_dim = 4, activation= 'linear'))

model3.compile(optimizer = 'sgd', loss='mse', metrics=['mse'])
model3.fit(x_train, y_train, epochs= 100, validation_split= 0.15, verbose= 0)  # 학습은 train
print('evaluate: ', model3.evaluate(x_test, y_test))
pred3 = model3.predict(x_test)
print('after validation_split - r2_score: ', r2_score(y_test, pred3))

plt.plot(y_test, 'b')
plt.plot(pred3, 'r--')
plt.show()
