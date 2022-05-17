# 밀도 기반 클러스터링 (DBSCAN): K-means 로 군집화 하기 힘든 데이터 분포인 경우(비선형)에 적당
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from sklearn.datasets import make_moons
from sklearn.cluster import KMeans, DBSCAN

x, y = make_moons(n_samples=200, noise = 0.07, random_state = 1)
print(x[:10])
print('실제 군집 id : ', y[:10])

# plt.scatter(x[:,0], x[:,1])
# plt.show()    # 데이터가 비선형

# KMeans로 군집화
km = KMeans(n_clusters = 2, random_state = 0)
pred1 = km.fit_predict(x)
print('예측군집 id :', pred1[:10])

def plot(x, pr):
    plt.scatter(x[pr == 0, 0], x[pr == 0, 1], c='blue', marker = 'o', s = 40, label ='cluster1')
    plt.scatter(x[pr == 1, 0], x[pr == 1, 1], c='red', marker = 'o', s = 40, label ='cluster2')
    plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1], c = 'black', s = 50, marker='+'
                , label = 'centroid')
    plt.legend()
    plt.title('result')
    plt.show()

plot(x, pred1)
print()
# KMeans 로 원하는 군집을 얻지 못한 경우 DBSCAN을 수행한다.
dm = DBSCAN(eps=0.2, min_samples = 5, metric ='euclidean')
pred2 = dm.fit_predict(x)

print('실제 군집 id : ', y[:10])
print('예측군집 id :', pred2[:10])
plot(x, pred2)