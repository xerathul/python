# BMI 식을 이용해 dataset을 작성 후 SVM 분류 모델 생성
# BMI 식 = 몸무게 (kg) / (키(m))^2

print(69/ (1.77*1.77))

# BMI 식을 이용해 무작위 자료 작성
import random
'''
def calc(h, w):
    bmi  = w /(h /100) ** 2 
    if bmi < 18.5: return 'thin'
    if bmi < 25.0: return 'normal'
    return 'fat'   

print(calc(177,69))

fp = open('bmi.csv', 'w')
fp.write('height,weight,label\n')
cnt ={'thin':0, 'normal':0, 'fat':0}
random.seed(12)

for i in range(50000):
    h = random.randint(150, 200)
    w = random.randint(35, 100)
    label = calc(h, w)
    cnt[label]+=1
    fp.write('{0},{1},{2}\n'.format(h, w, label))
fp.close()
'''

# SVM 분류 모델을 적용
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

tbl = pd.read_csv('bmi.csv')
print(tbl.head())

label = tbl['label']

# weight, height 는 정규화
w = tbl['weight'] / 100
print(w[:3])
h = tbl['height'] / 200
print(h[:3])
wh = pd.concat([w, h], axis = 1)
print(wh.head(), wh.shape)
print(label[:3], label.shape)
#더미화
label = label.map({'thin':0, 'normal':1, 'fat':2})
print(label[:3])

data_train, data_test, label_train, label_test = train_test_split(wh, label,random_state =1)
print(data_train.shape, data_test.shape)    #(37500, 2) (12500, 2)

# model = svm.SVC(C = 1).fit(data_train, label_train)
model = svm.LinearSVC(C=1).fit(data_train, label_train)

pred = model.predict(data_test)
print('실제값:', label_test[:10].values)
print('예측값:', pred[:10])

print('acc:', metrics.accuracy_score(label_test, pred)) #acc: 0.93784
print( metrics.classification_report(label_test, pred))

tbl2 = pd.read_csv('bmi.csv', index_col = 2)
print(tbl2.head(2))
def scatter_func(lbl, color):
    b = tbl2.loc[lbl]
    plt.scatter(b['weight'], b['height'], c = color, label = lbl)
    
scatter_func('fat', 'red')
scatter_func('normal', 'yellow')
scatter_func('thin', 'blue')
plt.legend()
plt.show()
