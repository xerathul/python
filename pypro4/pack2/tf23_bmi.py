# bmi dataset으로 분류
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout
import tensorflow as tf

bmi = pd.read_csv('bmi.csv')
print(bmi.head(2), bmi.shape)   #(50000, 3)

# 정규화 안하면 정확도 떨어짐
bmi['height'] /= 200
bmi['weight'] /= 100
print(bmi.head(2))

x = bmi[['height','weight']].values     #metrics 화

print(x[:2])

# label은 one-hot Encoding
bclass = {'thin':[1,0,0],'normal':[0,1,0],'fat':[0,0,1]}
y = np.empty((50000, 3))
print(y[:2])

for i , v in enumerate(bmi['label']):
    y[i] = bclass[v]
    
print(y[:5])

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 12, test_size = 0.3)
print(x_train.shape, x_test.shape)  #(35000, 2) (15000, 2)

print()
#model 
model = Sequential()
model.add(Dense(128, input_shape = (2,), activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(3,activation = 'softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
print(model.summary())

from keras.callbacks import EarlyStopping
es = EarlyStopping(monitor='loss', mode='auto', baseline=0.05, patience = 10)

model.fit(x_train, y_train, batch_size = 64, epochs = 10000, validation_split=0.2,
           verbose=2, callbacks = [es])

# evaluate
m_score = model.evaluate(x_test, y_test)
print('loss', m_score[0])
print('acc', m_score[1])

# predict
print('pred:', np.argmax(model.predict(x_test[:1]), axis = 1))
print('real:', np.argmax(y_test[:1]))

# new data 
print('pred:', np.argmax(model.predict(np.array([[187/200, 55/100]])), axis = 1))
print('pred:', np.argmax(model.predict(np.array([[157/200, 75/100]])), axis = 1))




