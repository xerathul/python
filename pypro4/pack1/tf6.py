''' Created on 2022. 5. 18. 1교시 ~ '''
''' Created on 2022.05.18 1교시 ~ '''
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Activation

# XOR 게이트 논리 모델을 생성 후 처리
# 1. 데이터 셋 생성
x = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0,1,1,0])
print(x)        # feature
print(y)        # label(class)

# model = Sequential([
#         Dense(input_dim = 2, units=1),    # node 1개
#         Activation('sigmoid')
# ])
# 위도 되고 아래도 된다!
# model = Sequential()
# model.add(Dense(units=5, input_dim=2))
# model.add(Activation('relu'))                # relu
# model.add(Dense(units=1))    # 출력 node를 5개로 늘린다! 
# model.add(Activation('sigmoid'))

# 위의 5줄을 아래의 3줄로 줄일 수도 있음

model = Sequential()
model.add(Dense(units=5, input_dim=2, activation='relu'))
# 레이어가 추가로 필요하면 input_dim 없이 위의 코드를 추가하면 된다
model.add(Dense(units=5, activation='relu'))
model.add(Dense(units=5, activation='relu'))
# Dense에 units를 몇 개 줄지 고민되면.. tensorflow playground를 사용할 수 있다!
model.add(Dense(units=1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(x, y, epochs=100, batch_size=1, verbose=2)
loss_metrics=model.evaluate(x, y)
print('loss_metrics : ', loss_metrics)

pred = (model.predict(x) > 0.5).astype('int32')
# print('예측결과 : ', pred)
print('예측결과 : ', pred.flatten())
# 예측결과가 잘 안 나와서 epochs를 100으로 늘리고 verbose는 2로 둬서 콘솔창 깔끔하게 출력.
# 그래도 손실률이 크게 떨어지지 않으면 adam을 클래스로 주고 learning rate를 써도 된다.
# 입력 노드 2 * 출력 노드 5 의 행렬곱은 Dense가 해준다!

print('history : ', history)
print('loss : ', history.history['loss'])
print('acc : ', history.history['accuracy'])

# # 학습 진행 중 loss, acc를 시각화
# import matplotlib.pyplot as plt
# plt.plot(history.history['loss'], label='train loss')
# plt.plot(history.history['accuracy'], label='train accuracy')
# plt.xlabel('epochs')
# plt.legend(loc='best')
# plt.show()

print('- - - - - - - ')
print(model.layers)
print(model.summary())  # 이게 가장 단순하고 보기 편함.

print()
print(model.weights)    # 가중치와 bias 확인 가능

