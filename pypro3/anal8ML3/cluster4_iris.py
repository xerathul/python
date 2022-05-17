# iris dataset 으로 분류 모델 작성 : 지도학습(K-NN), 비지도 학습(K-means)

from sklearn.datasets import load_iris
from sklearn.model_selection._split import train_test_split
from daal4py.sklearn.neighbors._classification import KNeighborsClassifier
from sklearn.metrics._classification import accuracy_score

iris = load_iris()

train_x, test_x, train_y, test_y = train_test_split(iris.data, iris.target, random_state = 42)

print(train_x[:2])
print(train_y[:2])

print('지도학습:K 최근접 이웃 알고리즘')

knnModel = KNeighborsClassifier(n_neighbors=3)  #홀수가 짝수보다 더 좋다
knnModel.fit(train_x, train_y)  #feature, label> 지도학습

pred = knnModel.predict(test_x)
print('pred:',pred[:3])
print('real:', test_y[:3])
print('acc :', accuracy_score(test_y, pred))

print()
print('비지도 학습: K평균 군집 알고리즘')
from sklearn.cluster import KMeans
KMeansModel = KMeans(n_clusters=3, init='k-means++', random_state = 0)
KMeansModel.fit(train_x)    #label이 없음> 비지도 학습

print(KMeansModel.labels_)
print('0 cluster :', train_y[KMeansModel.labels_ == 0])
print('1 cluster :', train_y[KMeansModel.labels_ == 1])
print('2 cluster :', train_y[KMeansModel.labels_ == 2])

print()
import numpy as np

new_input = np.array([[1.1,2.3,4.5,1.5]])
clu_pred = KMeansModel.predict(new_input)
print(clu_pred)