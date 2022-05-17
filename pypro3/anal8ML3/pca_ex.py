#PCA(주성분 분석): 원본 데이터의 feature 개수에 비해 작은 주성분으로 원본 데이터의 총 변동성을 대부분 설명 할 수 있는 분석기법
# 원본데이터의 총 변동성(variance)을 대부분 설명할 수 있는 분석기법

import numpy as np
import pandas as pd
from sklearn.preprocessing._data import StandardScaler
from sklearn.metrics._classification import accuracy_score

x1 = [95, 91, 66, 94, 68]
x2 = [56, 27, 25, 1, 9]
x3 = [57, 34, 9, 79, 4]

x = np.stack((x1, x2, x3), axis = 0)
print(x)

print('-------표준화------')
scaler = StandardScaler()
x_std = scaler.fit_transform(x)
print(x_std)
print(scaler.inverse_transform(x_std))

print('\nPCA ---------------')
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
print(pca.fit_transform(x_std))
print(pca.inverse_transform(pca.fit_transform(x_std)))

print(scaler.inverse_transform(pca.inverse_transform(pca.fit_transform(x_std))))

print('--wine dataset으로 분류모델(Randomforest)----------')

from sklearn.ensemble import RandomForestClassifier
import sklearn.metrics
from sklearn.model_selection import train_test_split

datas = pd.read_csv('../testdata/wine.csv', header=None)

print(datas.head())
x = np.array(datas.iloc[:,0:12])
y = np.array(datas.iloc[:,12])

print(x[:5])
print(y[:5], set(y))    #{0, 1}

train_x, test_x, train_y, test_y = train_test_split(x, y, random_state = 1)
model = RandomForestClassifier(n_estimators=100, criterion='entropy').fit(train_x, train_y)
pred = model.predict(test_x)
print('acc:', accuracy_score(test_y, pred))
print('real:', test_y[:10])
print('pred:', pred[:10])

print('주성분 분석 후 feature의 수를 줄여 RandomForest 진행')
pca = PCA(n_components= 5)
print(x[:3])
print(pca.fit_transform(x)[:3])

x_pca = pca.fit_transform(x)
train_x, test_x, train_y, test_y = train_test_split(x_pca, y, random_state = 1)
model2 = RandomForestClassifier(n_estimators=100, criterion='entropy').fit(train_x, train_y)
pred2 = model2.predict(test_x)
print('acc:', accuracy_score(test_y, pred2))
print('real:', test_y[:10])
print('pred:', pred2[:10])