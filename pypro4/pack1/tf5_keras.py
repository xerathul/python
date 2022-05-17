# Keras : 텐서플로 기반의 DeepLearning 라이브러리(모듈)
# 일관성 있는 API 지원
# ML(인굥신경망) 모델을 매우 쉽게 작성할 수 있다.

import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Activation

# OR 게이트 논리 모델을 생성
# 1. 데이터 셋 생성
x = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0,1,1,1])

print(x)
print(y)

#2. 모델 구성
# model = Sequential([
#     Dense(input_dim = 2, units=1),
#     Activation('sigmoid')
# ])
model = Sequential()
model.add(Dense(units=1, input_dim=2))
model.add(Activation('sigmoid'))

# 3. 모델 학습과정 설정(컴파일)    #optimizer='sgd' 확률적 경사하강법
# model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])    
# model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
# model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
# model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate =0.5, momentum=0.9),
#                loss='binary_crossentropy', metrics=['accuracy'])
# model.compile(optimizer=tf.keras.optimizers.RMSProp(learning_rate =0.1),
#                loss='binary_crossentropy', metrics=['accuracy'])
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate =0.01),
               loss='binary_crossentropy', metrics=['accuracy'])




# 4. model 학습시키기
model.fit(x, y, epochs = 10, batch_size = 1, verbose=0)     #verbose = 1 진행과정을 보여줌

# 5. model 평가
loss_metrics = model.evaluate(x, y)
print('loss_metrics:', loss_metrics)

# 모델을 사용해 예측하기
pred = model.predict(x)
# print('예측결과:\n', (pred > 0.5).astype('int32').T)
print('예측결과:\n', np.around(pred).T)

# 모델 성능이 우수하다고 판단 되면 모델을 저장
model.save('test.hdf5')

# del model

# 저장된 모델 읽기
from keras.models import load_model
model2 = load_model('test.hdf5')
print('예측결과:', (model2.predict(x)>0.5).astype('int32'))
