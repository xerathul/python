# 주 성분 분석(PCA) : 데이터 차원 축소
# 원래 데이터 분산을 최대한 보존하는 새로운 축을 찾고, 그 축에 데이터를 사영시키는 방법

# iris dataset을 사용해서 차원축소

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
plt.rc('font', family = 'malgun gothic')
from sklearn.datasets import load_iris

iris = load_iris()
print(iris.data[:2])
n = 10 
x = iris.data[:n, :2]
print('차원축소 전:\n', x, x.shape, type(x))
print(x.T)
'''
# 시각화
plt.plot(x.T, 'o:')
plt.xticks(range(2), ['꽃받침 길이','꽃받침 폭'])
plt.xlabel('특성의 종류')
plt.ylabel('특성값')
plt.title('iris feature')
plt.legend(['표본{}'.format(i + 1) for i in range(n)])
plt.grid()
plt.show()


# x축에는 꽃받침 길이, y 축에는 꽃받침 폭으로 산점도 출력
df = pd.DataFrame(x)
print(df.head())
ax = sns.scatterplot(df[0],df[1], data =df, s= 100, marker='s',color=['b'])
for i in range(n):
    ax.text(x[i, 0] - 0.05, x[i, 1] +0.03 , '표본{}'.format(i+1))
plt.xlabel('꽃받침 길이')
plt.ylabel('꽃받침 폭')
plt.title('iris feature(2d)')
plt.axis('equal')
plt.show()

# 두 개의 열의 값 패턴이 매우 유사함을 알 수 있다. 그러므로 차원축소가 가능하다. ==> PCA
pcal = PCA(n_components =1) # 변환 차원 수
x_low = pcal.fit_transform(x)   # 비지도 학습이라 x 값만 들어감. 특징행렬을 낮은 차원의 근사 행렬로 변환
print(x.T)
print('x_low\n', x_low.T, ' ', x_low.shape) # 두개의 열을 하나의 열로 축소

#차원 축소 값 원복
x2 = pcal.inverse_transform(x_low)
print('원복 값\n', x2.T, ' ', x2.shape)    #5.1 4.9 --> 5.06676112 4.7240094  근사행렬로 변환 똑같은 값으로 변하지 않음

print('원래 값:',x[0, :])
print('주성분 값:',x_low[0])
print('원복 값: ',x2[0,:])

# x축에는 꽃받침 길이, y 축에는 꽃받침 폭으로 산점도 출력
df = pd.DataFrame(x)
print(df.head())
ax = sns.scatterplot(df[0],df[1], data =df, s= 100, marker='s',color=['b'])
for i in range(n):
    ax.text(x[i, 0] - 0.05, x[i, 1] +0.03 , '표본{}'.format(i+1))
    plt.plot([x[i, 0], x2[i, 0]], [x[i,1], x2[i,1]],'k--')
    
plt.plot(x2[:, 0], x2[:,1], 'o-', color ='y', markersize = 10)
plt.plot(x[:, 0].mean(), x2[:,1].mean(), 'D', color ='r', markersize = 10)

plt.xlabel('꽃받침 길이')
plt.ylabel('꽃받침 폭')
plt.title('iris feature(2d)')
plt.axis('equal')
plt.show()

'''

# iris data 4개의 열을 2개로 축소
x = iris.data
print(x[:2])
pca2 = PCA(n_components=2)
x_low2 = pca2.fit_transform(x)
print('x_low2', x_low2[0])
print(pca2.explained_variance_ratio_)   #[0.92461872 0.05306648] [근사율 , 1-근사율]
x_trans = pca2.inverse_transform(x_low2)
print('원래 값:',x[0, :])
print('주성분 값:',x_low2[0])   #근사행렬로 변환했을 떼 원본 값의 92.46% 설명함
print('원복 값: ', x_trans[0,:])
# print('원복 값: ',x[0,:])

iris1 = pd.DataFrame(x, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_with'])
print(iris1.head())
print()
iris2 = pd.DataFrame(x_low2, columns=['var1', 'var2'])
print(iris2.head())