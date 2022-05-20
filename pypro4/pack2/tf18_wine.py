# wine dataset: red and white wine classification
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping, ModelCheckpoint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.layers.reshaping.flatten import Flatten

wdf= pd.read_csv('../testdata/wine.csv', header=None)
print(wdf.head(2))
print(wdf.info())
print(wdf.iloc[:,12].unique())          #[1 0]
print(len(wdf[wdf.iloc[:, 12] == 0]))   #4898
print(len(wdf[wdf.iloc[:, 12] == 1]))   #1599

dataset = wdf.values
x = dataset[:, 0:12]
y = dataset[:, -1]
print(x[:1])
print(y[:1])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state=12)

#model
model = Sequential()
#model.add(Flatten())
model.add(Dense(32, input_dim=12, activation ='relu'))
model.add(Dense(16, activation = 'relu'))
model.add(Dense(8, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))

model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics=['accuracy'])
print(model.summary())


#fit() 전에 모델 정확도 확인
loss, acc = model.evaluate(x_train, y_train)
print('훈련 전 모델 성능: {:5.2f}%'.format(acc * 100))

print()
early_stop = EarlyStopping(monitor='loss', patience=5)

# 학습 중 model 저장
import os
MODEL_DIR = './wine_model/'
if not os.path.exists(MODEL_DIR):
    os.mkdir(MODEL_DIR) 

# modelpath = MODEL_DIR + '{epoch: 02}_{loss:.3f}.hdf5'
modelpath = MODEL_DIR+'wine_model.hdf5'     # best model saving
chkPoint = ModelCheckpoint(filepath=modelpath, monitor='loss', save_best_only=True)

history = model.fit(x_train, y_train, epochs=1000, batch_size = 64, callbacks = [early_stop, chkPoint],
                    validation_split=0.2, verbose=2)
#callback - tensorboard, earlyStopping, ModelCheckpoint(file 저장)

# fit() 후 모델 정확도 확인
loss, acc = model.evaluate(x_train, y_train)    #98.57%
print('훈련 후 모델 성능: {:5.2f}%'.format(acc * 100))

# 내가 직접 성능 좋은 모델을 판단해 저장한다면 model.save('파일명.htf5') - 그러나 ModelCheckpoint가 있다.

vloss = history.history['val_loss']
print('vloss:', vloss, len(vloss))
loss = history.history['loss']
print('loss:', loss, len(loss))
acc = history.history['accuracy']
print('acc:', acc, len(acc))
vacc = history.history['val_accuracy']
print('vacc:', vacc, len(vacc))

# 시각화
epoch_len = np.arange(len(acc))
plt.plot(epoch_len, vloss, c='red',label = 'val_loss')
plt.plot(epoch_len, loss, c='blue',label = 'loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend()
plt.show()


plt.plot(epoch_len, vacc, c='red',label = 'val_acc')
plt.plot(epoch_len, acc, c='blue',label = 'acc')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend()
plt.show()

# 예측
# 베스트 모델이 저장 되었으므로 더이상의 학습은 진행 x
# 베스트 모델을 읽어 새로운 데이터 분류
from keras.models import load_model
myModel = load_model(filepath='wine_model/wine_model.hdf5')
new_data = x_test[:5, :]
print(new_data)
pred = myModel.predict(new_data)
print('분류 결과:', np.where(pred > 0.5, 1, 0).flatten())



