# weather dataset 으로 비 유무 처리용 나이브 베이즈 분류 모델
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn import metrics

df = pd.read_csv('../testdata/weather.csv')
print(df.head())
print(df.info())

x = df[['MinTemp','MaxTemp','Rainfall']]
print(x.head())
label = df['RainTomorrow'].map({'Yes':1,'No':0})
print(label.head())

#train /test

trainX, testX, trainY, testY = train_test_split(x, label, random_state = 0)

gmodel = GaussianNB()
gmodel.fit(trainX, trainY)
pred = gmodel.predict(testX)
print('pred', pred[:10])
print('real', testY[:10].values)

print('acc', accuracy_score(testY, pred))
print('report: \n', metrics.classification_report(testY, pred))