# 단순 선형회귀 모델 생성
import tensorflow as tf
import numpy as np

opti = tf.keras.optimizers.SGD()    # RMSProp, Adam > 코스트를 미니마이즈 해주는 모듈들
w = tf.Variable(tf.random.normal((1, )))  # 정규분포를 떠르는 랜덤 값
b = tf.Variable(tf.random.normal((1,)))
print(w.numpy())
print(b.numpy())

@tf.function
def train_step(x, y): 
    with tf.GradientTape() as tape: #GradientTape 자동으로 미분 계산 해줌
        hypo = tf.add(tf.multiply(w, x), b)
        loss = tf.reduce_mean(tf.square(tf.subtract(hypo, y)))
    
    #미분 해주기
    grad = tape.gradient(loss, [w,b])   #편미분 수행 
    opti.apply_gradients(zip(grad,[w,b]))
    return loss

x = [1.,2.,3.,4.,5.]
y = [1.2,2.0,3.0,3.5,5.5]
print(np.corrcoef(x, y))    #0.9749

w_val = []  
cost_val = []
for i in range(101):    #100번 돌리는것 > epoch
    loss_val = train_step(x, y)
    cost_val.append(loss_val.numpy())
    w_val.append(w.numpy())
    if i % 10  == 0:
        print(loss_val)

print(cost_val)
print(w_val)

import matplotlib.pyplot as plt
plt.plot(w_val, cost_val, 'o')
plt.xlabel('w')
plt.ylabel('cost')
plt.show()

print('cost가 최소 일 때 w :',w.numpy())
print('cost가 최소 일 때 b :',b.numpy())

y_pred = tf.multiply(x, w) + b  # y = wx + b
print('예측값:',np.around(y_pred.numpy(),1))
print('실제값:',y)

plt.plot(x,y, 'ro', label = 'real')
plt.plot(x,y_pred, 'b', label = 'pred')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

print()
# 미지의 새로운 값으로 y를 예측
new_x =[3.5, 9.0]
new_pred = tf.multiply(new_x, w)+b
print('새로운 값으로 y를 예측:', new_pred.numpy())


