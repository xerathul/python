# 다항 분류: 출력값이 softmax 함수를 통해 확률 값으로 여러개가 출력
# 이중에서 확률값이 가장 큰 인덱스를 분류의 결과로 얻음

from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical #one - hot encoding 을 지원
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from keras.callbacks import EarlyStopping

np.random.seed(1)
# tf.random.set_seed(1)

x = np.random.random((1000, 12))    #시험점수
y = np.random.randint(5, size = (1000,1))   # 범주 5개, 시험과목 0:국 ~ 4:체육 이라고 가정
print(x[:2])
print(y[:2])    #[[2][0]] 학습시 label(y)은 원핫 처리 후 학습에 참여
y = to_categorical(y, num_classes=5)
print(y[:2])
print([np.argmax(i) for i in y[:2]])

#early_stop
print()
early_stop = EarlyStopping(monitor='loss', patience=50)

# model
model = Sequential()
model.add(Dense(units=32, input_shape=(12,), activation = 'relu'))
model.add(Dense(units=16, activation = 'relu'))
model.add(Dense(units=5,  activation = 'softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
print(model.summary())
history= model.fit(x, y, epochs=10000, batch_size=32, verbose=2, shuffle=True, callbacks = [early_stop])   #shuffle=True 비복원 추출

model_eval = model.evaluate(x, y)
print('model_eval :', model_eval)

# 시각화
plt.plot(history.history['loss'], label = 'loss')
plt.xlabel('epochs')
plt.legend()
plt.show()

plt.plot(history.history['accuracy'], label = 'accuracy')
plt.xlabel('epochs')
plt.legend()
plt.show()

# 예측
print('pred:', model.predict(x[:5]))
print('pred:', [np.argmax(i) for i in model.predict(x[:5])])
print('real:', y[:5])
print('real:',[np.argmax(i) for i in y[:5]])

# 새로운 값으로 예측
xNew = np.random.random((2, 12))    #시험점수
print(xNew)
newPred = model.predict(xNew)
print('new_pred', newPred)
print('sum of newPred:', np.sum(newPred))
print('new_pred:',[np.argmax(i) for i in newPred])

CLASSES = np.array(['국어','영어','수학','과학','체육'])
print('분류결과1:', CLASSES[np.argmax(newPred[0])])
print('분류결과2:', CLASSES[np.argmax(newPred[1])])
