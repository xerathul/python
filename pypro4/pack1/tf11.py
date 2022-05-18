# 단순 선형회귀 모델 작성 방법 세가지 경험하기
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers
import numpy as np

# 공부 시간에 따른 성적 데이터
x_data = np.array([1,2,3,4,5], dtype =np.float32)
y_data = np.array([11,32,53,64,70],dtype = np.float32)
print(np.corrcoef(x_data, y_data))

print('모델 작성방법 1: sequential Api : 가장 일반적, 단순한 방법')
model = Sequential()
model.add(Dense(units=2, input_dim = 1, activation = 'linear'))
model.add(Dense(units=1, input_dim = 1, activation = 'linear')) #layer 추가

print(model.summary())
opti = tf.keras.optimizers.Adam(learning_rate = 0.1)
model.compile(optimizer=opti, loss='mse', metrics=['mse'])
history = model.fit(x = x_data, y = y_data, batch_size = 1, epochs= 100, verbose= 0)
loss_metrics = model.evaluate(x_data, y_data)
print('loss_metrics',loss_metrics)

# 설명력
from sklearn.metrics import r2_score
print('설명력:', r2_score(y_data, model.predict(x_data)))
print('실제값:', y_data)
print('pred:', model.predict(x_data).flatten())

new_data = [1.5, 2.3, 5.8]
print('new_pred:', model.predict(new_data).flatten())
'''
# 시각화
import matplotlib.pyplot as plt
plt.rc('font', family ='malgun gothic')

plt.plot(x_data, model.predict(x_data), 'b', x_data, y_data, 'ko')
plt.show()

# plt.plot(history.history['loss'],label = '손실')
# plt.xlabel('학습횟수')
plt.plot(history.history['mse'],label = '평균제곱오차')
plt.xlabel('학습횟수')
plt.legend()
plt.show()

plt.show()
'''

print('모델 작성방법 2: Function Api : 유연한 구조, 입력 데이터로 여러 층을 공유하거나 다양한 종류의 입출력 사용이 가능하다')
from keras.layers import Input
from keras.models import Model

# 각 층은 일종의 함수처럼 처리 함
inputs = Input(shape=(1,))
# outputs = Dense(1, activation='linear')(inputs)
output1 = Dense(2, activation='linear')(inputs)
outputs = Dense(1, activation='linear')(output1)

#ValueError: This model has not yet been built. Build the model first by calling `build()` or by calling the model on a batch of data.
# model2 = Model(outputs)
model2 = Model(inputs,outputs)


# 이하는 방법 1과 동일
print(model2.summary())
opti = tf.keras.optimizers.Adam(learning_rate = 0.1)
model2.compile(optimizer=opti, loss='mse', metrics=['mse'])
history = model2.fit(x = x_data, y = y_data, batch_size = 1, epochs= 100, verbose= 0)
loss_metrics = model2.evaluate(x_data, y_data)
print('loss_metrics',loss_metrics)

# 설명력
from sklearn.metrics import r2_score
print('설명력2:', r2_score(y_data, model2.predict(x_data)))
print('실제값2:', y_data)
print('pred2:', model2.predict(x_data).flatten())

print('모델 작성방법 3: sub classing : 동적인 구조의 네트워크, 고난이도의 작업에서 활용성이 높음')
# 자연어 처리시 유용 좀 어러움
x_data = np.array([[1],[2],[3],[4],[5]], dtype =np.float32)
y_data = np.array([11,32,53,64,70],dtype = np.float32)

class Mymodel(Model):
    def __init__(self):
        super(Mymodel, self).__init__()
        self.d1 = Dense(2, activation= 'linear')
        self.d2 = Dense(1, activation= 'linear')
    
    def call(self, x):
        inputs = self.d1(x)
        return self.d2(inputs)

model3 = Mymodel()

# 이하는 방법 1과 동일
opti = tf.keras.optimizers.Adam(learning_rate = 0.1)
model3.compile(optimizer=opti, loss='mse', metrics=['mse'])
history = model3.fit(x = x_data, y = y_data, batch_size = 1, epochs= 100, verbose= 0)
loss_metrics = model3.evaluate(x_data, y_data)
print('loss_metrics',loss_metrics)

#설명력
print('설명력3:', r2_score(y_data, model3.predict(x_data)))
print('실제값3:', y_data)
print('pred3:', model3.predict(x_data).flatten())

print(model3.summary())

print('모델 작성방법 3-1: custom layer + sub classing : 동적인 구조의 네트워크, 고난이도의 작업에서 활용성이 높음')
from keras.layers import Layer

#custom layer :사용자 정의층 사용
class Linear(Layer):
    # 생성자
    def __init__(self, units =1):
        super(Linear, self).__init__()
        self.units = units
        
    def build(self, input_shape):   #call 호출, 가중치 관련 내용을 적을 수 있다
        #intput_shape[-1] > 너가알아서 크기 결정해 // trainable = True > 역전파 수행
        self.w = self.add_weight(shape = (input_shape[-1], self.units), initializer ='random_normal',
                                 trainable = True )    
        self.b = self.add_weight(shape= (self.units,), initializer = 'zeros', trainable =True)
        
    def call(self, inputs):
        return tf.matmul(inputs, self.w) + self.b   #y = wx + b
    
class MLP(Model):
    def __init__(self):
        super(MLP, self).__init__()
        #self.linear1 = Linear(1)
        self.linear1 = Linear(2)
        self.linear2 = Linear(1)
        
    def call(self, inputs):
        # return self.linear1(inputs)
        x = self.linear1(inputs)
        return self.linear2(x)
    
model4 = MLP()

# 이하는 방법 1과 동일
opti = tf.keras.optimizers.Adam(learning_rate = 0.1)
model4.compile(optimizer=opti, loss='mse', metrics=['mse'])
history = model4.fit(x = x_data, y = y_data, batch_size = 1, epochs= 100, verbose= 0)
loss_metrics = model4.evaluate(x_data, y_data)
print('loss_metrics',loss_metrics)

#설명력
print('설명력3:', r2_score(y_data, model4.predict(x_data)))
print('실제값3:', y_data)
print('pred3:', model4.predict(x_data).flatten())

print(model4.summary())

# tf.keras.utils.plot_model(model, 'abc.png')