# zoo dataset : 동물을 7가지로 분류

import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical #one - hot encoding 을 지원

xy = np.loadtxt('../testdata/zoo.csv', delimiter=',')
print(xy[:2], xy.shape) #(101, 17)

x = xy[:,0:-1] #feature
y = xy[:, [-1]] #label
print(x[:2])
print(y[:2], set(y[:,0]))   #0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0}

# train /test 생략
# label one-hot processing

print()

#model
model= Sequential()
model.add(Dense(32, input_shape=(16, ), activation = 'relu'))
model.add(Dense(32, activation = 'relu'))
model.add(Dense(7, activation = 'softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['acc'])
# loss = 'sparse_categorical_crossentropy' 하면 label의 원핫처리를 내부적으로 진행

print(model.summary())

history = model.fit(x, y, epochs=100, batch_size = 32, verbose=0)
print('evaluate : ', model.evaluate(x,y))

# loss, acc 시각화
historyDict= history.history

loss = historyDict['loss']
acc = historyDict['acc']

import matplotlib.pyplot as plt

plt.plot(loss, 'b-', label = 'loss')
plt.plot(acc, 'r-', label= 'acc')
plt.xlabel('epochs')
plt.legend()
plt.show()

print('pred')
predData = x[:1]
print('1 pred:', np.argmax(model.predict(predData)))
print()
predDatas = x[:5]
preds = [np.argmax(i) for i in model.predict(predDatas)]
print('predicts:', preds)
print('reals:', y[:5].flatten())

