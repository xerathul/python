#최소제곱해를 선형 행렬 방정식으로 얻기
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg

x = np.array([0, 1, 2, 3])
y = np.array([-1, 0.2, 0.5, 2.1])

# plt.plot(x, y, 'o', label='Original data', markersize=10)
# plt.grid()
# plt.show()

A = np.vstack([x, np.ones(len(x))]).T
print(A)    #4*2

#최소 자승법(내부적으로 편미분 사용)
w, b = np.linalg.lstsq(A, y)[0]
print(w, b)     #0.9599999999999999 -0.9899999999999995
# 단순 선형 회귀식  y = 0.9599999999999999 * x + -0.9899999999999995

print('에측값 : ', 0.9599999999999999 * 0 + -0.9899999999999995)
print('에측값 : ', 0.9599999999999999 * 1 + -0.9899999999999995)
print('에측값 : ', 0.9599999999999999 * 2 + -0.9899999999999995)
print('에측값 : ', 0.9599999999999999 * 3 + -0.9899999999999995)
print('미지의 에측값 : ', 0.9599999999999999 * 10 + -0.9899999999999995)

plt.plot(x, y, 'o', label='Original data', markersize=10)
plt.plot(x, w*x + b, 'r', label='Fitted line')
plt.grid()
plt.legend()
plt.show()