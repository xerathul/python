# KNN : 데이터로부터 거리가 가까운 k개의 다른 데이터의 레이블을 참조하여 분류를 진행
from sklearn.model_selection._split import train_test_split

train = [
    [5,3,2],
    [1,3,5],
    [4,5,7]
]
label =[0,1,1]

# import matplotlib.pyplot as plt
# plt.xlim([-1, 3])
# plt.ylim([0,10])
# plt.plot(train, 'o')
# plt.show()

from sklearn.neighbors import KNeighborsClassifier

kmodel = KNeighborsClassifier(n_neighbors = 3, weights = 'distance')
kmodel.fit(train, label)
pred = kmodel.predict(train)
print('pred', pred)

print('----------------')
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
plt.rc('font', family = 'malgun gothic')

cancer= load_breast_cancer()
x_train, x_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state = 66,
                                                    stratify = cancer.target) #class 비율 유지, 치우침 방지
print(x_train.shape, x_test.shape)  #(426, 30) (143, 30)

train_acc = []
test_acc = []
neighbors_set = range (1, 15)

for n_nei in neighbors_set:
    clf = KNeighborsClassifier(n_neighbors = n_nei)
    clf.fit(x_train, y_train)
    train_acc.append(clf.score(x_train, y_train))
    test_acc.append(clf.score(x_test, y_test))
    
import numpy as np
print(train_acc)
print(test_acc)
print('train 분류 평균 정확도: ', np.mean(train_acc))
print('test 분류 평균 정확도: ',np.mean(test_acc))

plt.plot(neighbors_set, train_acc, label ='훈련정확도')
plt.plot(neighbors_set, test_acc, label = '검증정확도')
plt.xlabel('k값')
plt.ylabel('정확도')
plt.legend()
plt.show()