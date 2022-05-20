from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Adam, RMSprop, SGD


x_data = [[1,2],[2,3],[3,4],[4,3],[3,2],[2,1]]
y_data = [[0],[0],[0],[1],[1],[1]]

#Sequntial api
# model = Sequential([
#     Dense(units=1, input_dim = 2),  #input_shape =(2,)
#     Activation('sigmoid')
# ])

model = Sequential()
model.add(Dense(units=1, input_dim=2, activation = 'sigmoid'))
model.compile(optimizer=Adam(learning_rate=0.1),loss = 'binary_crossentropy', metrics = ['accuracy'])
print(model.summary())

model.fit(x=x_data, y=y_data, epochs = 100, batch_size = 1, verbose=1)
m_eval = model.evaluate(x_data, y_data, batch_size=1, verbose=1)
print(m_eval)

# 새로운 값으로 결과 얻기
import numpy as np
new_data = [[1,2],[10,7]]
pred = model.predict(new_data, batch_size=1, verbose=1)
print('pred:\n',pred)
print('pred:\n', np.around(pred).flatten())

# function api ----
from keras.layers import Input
from keras.models import Model

inputs= Input(shape=(2,))
outputs = Dense(units=1, activation='sigmoid')(inputs)
model2 = Model(inputs, outputs )

model2.compile(optimizer=Adam(learning_rate=0.1),loss = 'binary_crossentropy', metrics = ['accuracy'])

model2.fit(x=x_data, y=y_data, epochs = 100, batch_size = 1, verbose=1)
m_eval2 = model2.evaluate(x_data, y_data, batch_size=1, verbose=1)
print(m_eval2)

# 새로운 값으로 결과 얻기

new_data = [[1,2],[10,7]]
pred2 = model2.predict(new_data, batch_size=1, verbose=1)
print('pred:\n',pred2)
print('pred:\n', np.around(pred2).flatten())