# 이항분류는 다항 분류로도 처리가능
# diabets dataset

import numpy as np
from keras.models import Sequential
from keras.layers import Dense

dataset = np.loadtxt('../testdata/diabetes.csv', delimiter=',')
print(dataset.shape)
print(dataset[:1])
print(set(dataset[:, -1]))

# 이항분류 : sigmoid

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(dataset[:,0:8], dataset[:, -1],
                                                    test_size = 0.3, random_state = 123)
print(x_train.shape, x_test.shape)  #(531, 8) (228, 8)

# model
model = Sequential()
model.add(Dense(64, input_dim=8, activation ='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
model.fit(x_train, y_train, epochs=100, batch_size = 32, verbose=0, validation_split=0.2)
scores = model.evaluate(x_test, y_test)
print('이항분류 모델 성능: %s: %.2f%%'%(model.metrics_names[1], scores[1]*100))    #0번재: loss, 1번째: acc
print('이항분류 모델 성능: %s: %.2f'%(model.metrics_names[0], scores[0])) 

#predict
pred = model.predict([[-0.294, 0.487, 0.180,-0.292, 0. ,  0.00149, -0.53, -0.0333]])
print('pred:', pred, np.where(pred>0.5, 1,0))

print('------'*10)

# 위의 내용을 다항 분류로 처리
from keras.utils import to_categorical #one - hot encoding 을 지원

# label one-hot setting
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
print('y_train:', set(y_train[0]))  #y_train: {0.0, 1.0}

# model
model = Sequential()
model.add(Dense(64, input_dim=8, activation ='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(2, activation='softmax'))   #확률값으로 나가기
    
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
model.fit(x_train, y_train, epochs=100, batch_size = 32, verbose=0, validation_split=0.2)
scores = model.evaluate(x_test, y_test)
print('이항분류 모델 성능: %s: %.2f%%'%(model.metrics_names[1], scores[1]*100))    #0번재: loss, 1번째: acc
print('이항분류 모델 성능: %s: %.2f'%(model.metrics_names[0], scores[0])) 

#predict
pred = model.predict([[-0.294, 0.487, 0.180,-0.292, 0. ,  0.00149, -0.53, -0.0333]])
print('pred:', pred, np.argmax(pred))