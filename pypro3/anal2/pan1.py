#Pandas : 고수준의 자료 구조(Series, DataFrame)을 지원.
#데이터 분석용 자료 관리를 위한 다양한 함수 제공
#축약 연산, SQL처리, 시계열 데이터 처리, 시각화 ...

import pandas as pd
from pandas import Series
import numpy as np

#Series : 일련의 데이터를 담을 수 있는 1차원 배열과 비슷한 자료구조를 가지며, 색인을 지원]

obj = Series([3, 7, -5, 4])
# list, tuple type 가능. TypeError:'set' type is unordered
obj2 = Series([3, 7, -5, 4], index=['a', 'b', 'c', 'd'])
# 생성 시 색인을 지정
print(obj, type(obj))
print(obj2)
print(obj2.sum(),np.sum(obj2), sum(obj2))
print(obj2.values)  #[ 3  7 -5  4] 값만 볼 수 있음
print(obj2.index)   #Index(['a', 'b', 'c', 'd'], dtype='object')

#인덱싱과 슬라이싱
print(obj2[1])
print(obj2['a'])
print(obj2[['a']])

print(obj2[['a','b']])
print(obj2['a':'b'])

print(obj[2])
print(obj2[1:4])
print(obj2[[2,1]])
print(obj2>1)
print('a' in obj2)

print('-----------------')
# dict type으로 Series객체 생성
names={'mouse':5000,'keyboard':25000,'monitor':550000}
print(names)
obj3= Series(names)
print(obj3)
obj3.index=['마우스','키보드','모니터']
print(obj3)
print(obj3['마우스'])
print()
obj3.name = '상품가격'
print(obj3)

print('\n---------DataFrame-------------')
#DataFrame : 표 모양의(2차원) 자료구조로 여러 개의 칼럼(열)을 갖는다.
from pandas import DataFrame
df = DataFrame(obj3)
print(df, type(df))

data = {
'irum':['홍길동', '한국인', '신기해', '공기밥', '한가해'],
'juso':('역삼동', '신당동', '역삼동', '역삼동', '신사동'),
'nai':[23, 25, 33, 30, 35],
}
print(data, type(data))

frame= DataFrame(data)
print(frame, type(frame))

#데이터를 얻을 수 있는 곳: Local, Database, File, Web(Sns, homepage...)

print(frame['irum'], type(frame['irum'])) # 시리즈가 모이면 DataFrame 이 됨
print(frame.irum)
print()
print(DataFrame(data, columns=['juso','irum','nai']))
print()
frame2 = DataFrame(data, columns=['irum','nai','juso','tel'],index = ['a','b','c','d','e'])
#frame2.columns= ['irum','nai','juso','tel']
#frame2.index=  ['a','b','c','d','e']

print(frame2)
frame2['tel']='111-1111'    #모든 행에 적용
print(frame2)

val = Series(['222-2222','333-3333','444-4444'],index = ['b','c','d'])
print(val)
frame2['tel']=val
print(frame2)

print(frame2.T)     #전치

print(frame2.values)
print(frame2.values[0,1])
print(frame2.values[0:2])

print()
frame3 = frame2.drop('d') #행 삭제
frame3 = frame2.drop('d',axis=0)    #axis=0 : 행 삭제
print(frame3)

frame4 = frame2.drop('tel',axis=1)
print(frame4)

print()
print(frame2)
print(frame2.sort_index(axis=0, ascending =False))      #행단위
print(frame2.sort_index(axis=1, ascending =False))      #열단위
print(frame2.rank(axis = 0))

print()
print(frame2['juso'].value_counts())

print()
data = {
    'juso':['강남구 역삼동','중구 신당동','강남구 대치동'],
    'inwon':[23,25,15]  
}
fr = DataFrame(data)
print(fr)

result1 =Series([a.split()[0] for a in fr.juso])
print(result1.values)
print()
result2 =Series([a.split()[1] for a in fr.juso])
print(result2.values)
print(result2.value_counts())