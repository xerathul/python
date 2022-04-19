from pandas import Series, DataFrame
import numpy as np
data =Series([1,3,2], index = (1,4,2))
print(data)

data2 = data.reindex((1,2,4))   #행 순서 재배치
print(data2)

print()
data3 = data2.reindex([0,1,2,3,4,5])    #대응 값이 없는 인덱스는 결측 값이 됨
print(data3)
print()
data3 = data2.reindex([0,1,2,3,4,5],fill_value = 777)#대응 값이 없는 인덱스는 777
print(data3)
print()
print(data2.reindex([0,1,2,3,4,5],method = 'ffill')) #Nan 앞 값으로 현재 Nan을 대체
print(data2.reindex([0,1,2,3,4,5],method = 'pad'))
print()
print(data2.reindex([0,1,2,3,4,5],method = 'bfill'))
print(data2.reindex([0,1,2,3,4,5],method = 'backfill'))

print('----------------------------')
df = DataFrame(np.arange(12).reshape(4,3), index = ['1월','2월','3월','4월'], columns = ['강남','강북','서초'])
print(df)
print(df['강남'])
print(df['강남'] >3)
print(df[df['강남']>3])
print()
df[df <3]=0
print(df)

print('슬라이싱 관련 메소드 : loc()-라벨지원, iloc()-숫자지원 ------')
print(df['강남'])
#복수 인덱싱
#loc = 라벨사용
print(df.loc['3월'])
print(df.loc['3월',])
print(df.loc['3월', :])
print()
print(df.loc[:'3월'])    #3월 이하 행 모든 열 출력
print(df.loc[:'3월',['서초']])  
print()
#iloc 숫자 사용
print(df.iloc[2])   #2 행 출력
print(df.iloc[2, :]) #2 행 출력
print(df.iloc[:3])  #3미만 행 출력
print(df.iloc[:3,2])    #3행 미만 행, 2열 출력
print(df.iloc[1:3,1:3]) 

print('--------연산--------')
s1= Series([1,2,3], index= ['a','b','c'])
s2= Series([4,5,6,7], index= ['a','b','d','c'])

print(s1)
print(s2)
print(s1 + s2) # 인덱스 명 끼리 연산 -,*,/
print(s1.add(s2)) # 인덱스 명 끼리 연산 sub, mul. div

print()
df1 = DataFrame(np.arange(9).reshape(3,3),columns = list('kbs'), index=['seoul','daejun','busan'])
df2 = DataFrame(np.arange(12).reshape(4,3),columns = list('kbs'), index=['seoul','daejun','jeju','guangju'])
print(df1)
print(df2)
print()
print(df1 + df2)
print(df1.add(df2, fill_value = 0))     #nan은 0 으로 채움







