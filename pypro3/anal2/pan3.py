#함수
from pandas import Series, DataFrame
import numpy as np

df= DataFrame([[1.4,np.nan],[7, 4.5],[np.NaN,np.NAN],[0.5,-1]])
df.columns= ['one','two']
print(df)
print(df.drop(1))   #특정 행 삭제
print(df.isnull())  #NaN 탐지
print(df.notnull())  #NaN 탐지
print(df.dropna())  # NaN이 있는 특정행 삭제
print(df.dropna(how='any')) # NaN이 하나라도 열에 있는 특정행 삭제
print(df.dropna(how='all')) #모든 열 값이 NaN일 때 행 삭제
print(df.dropna(subset=['one'])) #특정 열 값 중 Nan 인 경우 행 삭제
print()
print(df.dropna(axis='rows'))   #NaN 이 포함된 행 삭제
print(df.dropna(axis='columns')) #NaN 이 포함된 열 삭제

print(df.fillna(0)) #NaN을 0 으로 채우기 , 평균 또는 대표값으로 채울 수도 있다.

print('-----------')
print(df)
print(df.sum(axis=0))   #열의 합
print(df.sum(axis=1))
print(df.mean(axis=1))  #행의 평균

print()
print(df.idxmax())
print(df.max())
print()
print(df.describe())    #요약 통계량
print(df.info())

words= Series(['봄','여름','봄'])
print(words.describe())
#words.info()    'Series' object has no attribute 'info'
