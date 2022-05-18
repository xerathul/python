#   실습 환경은 tensorflow 2.x   
# ex1) 단순선형회귀 - 경사하강법 함수 사용 1.x 
# 0 37.7017 [-0.49608618]
# 1 16.8007 [-0.03689262]
# 2 7.49591 [ 0.2697657]
# 3 3.35345 [ 0.47464877]
# ...
# 27 0.021242 [ 0.90224415]
# 28 0.0209367 [ 0.9029572]
# 29 0.0206358 [ 0.90366244]
#
# 실습 소스)

import tensorflow.compat.v1 as tf   # tensorflow 1.x 소스 실행 시
tf.disable_v2_behavior()            # tensorflow 1.x 소스 실행 시

import matplotlib.pyplot as plt

x_data = [1.,2.,3.,4.,5.]
y_data = [1.2,2.0,3.0,3.5,5.5]

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
w = tf.Variable(tf.random_normal([1]))
b = tf.Variable(tf.random_normal([1]))

hypothesis = x * w + b
cost = tf.reduce_mean(tf.square(hypothesis - y))

print('\n경사하강법 메소드 사용------------')
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

sess = tf.Session()   # Launch the graph in a session.
sess.run(tf.global_variables_initializer())

w_val = []
cost_val = []

for i in range(501):
    _, curr_cost, curr_w, curr_b = sess.run([train, cost, w, b], {x:x_data, y:y_data})
    w_val.append(curr_w)
    cost_val.append(curr_cost)

    if i  % 10 == 0:
        print(str(i) + ' cost:' + str(curr_cost) + ' weight:' + str(curr_w) +' b:' + str(curr_b))

plt.plot(w_val, cost_val)
plt.xlabel('w')
plt.ylabel('cost')
plt.show()

print('--회귀분석 모델로 Y 값 예측------------------')
print(sess.run(hypothesis, feed_dict={x:[5]}))        # [5.0563836]
print(sess.run(hypothesis, feed_dict={x:[2.5]}))      # [2.5046895]
print(sess.run(hypothesis, feed_dict={x:[1.5, 3.3]})) # [1.4840119 3.3212316]