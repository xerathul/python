# 완전 연결층(Dense)으로 이미지 분휴
# MNIST dataset : 흑백손글씨 이미지 7만장과 라벨 7만개
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from keras.layers.regularization.dropout import Dropout

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
print(x_train.shape, y_train.shape,x_test.shape, y_test.shape)     #(60000, 28, 28) (60000,) (10000, 28, 28) (10000,)
print(x_train[0])   
print(y_train[0])   #5

# 그림 확인해보기
# import sys
# for i in x_train[2]:
#     for j in i:
#         sys.stdout.write('%s  '%j)
#     sys.stdout.write('\n')


# plt.imshow(x_train[0], cmap='gray')
# plt.show()


'''
# model 
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(units=128, input_shape = (784,), activation = 'relu'))
# model.add(Dense(Flatten(input_shape =(28,28))))
model.add(Dropout(0.2))
model.add(Dense(units=128, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(units=10, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
print(model.summary())

history = model.fit(x_train, y_train, epochs=10, batch_size = 128,
                     validation_data=(x_val,y_val), verbose=2)

print('loss:',history.history['loss'])
print('val loss:',history.history['val_loss'])
print('acc:',history.history['acc'])
print('val acc:', history.history['val_acc'])

# 시각화

plt.plot(history.history['loss'], label = 'loss')
plt.plot(history.history['val_loss'], label ='val_loss')
plt.xlabel('epochs')
plt.legend()
plt.show()

plt.plot(history.history['acc'], label = 'acc')
plt.plot(history.history['val_acc'], label ='val_acc')
plt.xlabel('epochs')
plt.legend()
plt.show()

# model evaluate
print(x_test.shape, y_test.shape)   #(10000, 784) (10000,)
score= model.evaluate(x_test, y_test, batch_size=128, verbose=0)
print('test loss:', score[0])
print('test acc:', score[1])

# model saving
model.save('tf25.hdf5')
del model
'''
# model loading
mymodel = tf.keras.models.load_model('tf25.hdf5')
'''
plt.imshow(x_test[:1].reshape(28,28), cmap='gray')
plt.show()
# print(x_test[:1], x_test[:1].shape)

pred = mymodel.predict(x_test[:1])
print('pred:',np.around(pred))
print('pred:', np.argmax(pred,1))
print('real:', y_test[:1])
print('real:', np.argmax(y_test[:1]))
'''

# 내가 그린 손글씨 이미지 분류 결과 보기
from PIL import Image
import matplotlib.pyplot as plt

im = Image.open('num7.png')
img = np.array(im.resize((28,28), Image.ANTIALIAS).convert('L'))     # 끝부분 부드럽게 처리 'L' 흑백
print(img.shape)    #(28, 28)

plt.imshow(img, cmap='gray')
plt.show()

data = img.reshape([1, 784])
# print(data)
data = data / 255.0
print(data)

# predict
pred = mymodel.predict(data)
print('my pic pred:',np.around(pred))
print('pred:', np.argmax(pred,1))

