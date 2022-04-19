#pandas 문제 3)  타이타닉 승객 데이터를 사용하여 아래의 물음에 답하시오.
'''
 titanic_data.csv 파일을 다운로드 후
   df = pd.read_csv('파일명',  header=None,,,)  

 1) 데이터프레임의 자료로 나이대(소년, 청년, 장년, 노년)에 대한 생존자수를 계산한다.
     cut() 함수 사용
     bins = [1, 20, 35, 60, 150]
     labels = ["소년", "청년", "장년", "노년"]
'''
import pandas as pd
import numpy as np
df= pd.read_csv('../testdata/titanic_data.csv')
#print(df)
bins = [1, 20, 35, 60, 150]
labels = ["소년", "청년", "장년", "노년"]
df['age_class']= pd.cut(df['Age'], bins, labels = ["소년", "청년", "장년", "노년"])
#print(df[['Age','Survived','age_class']])
result= df.pivot_table(values=['Survived'],index=['age_class'], aggfunc= np.sum )
print(result)
'''
 2) 성별 및 선실에 대한 자료를 이용해서 생존여부(Survived)에 대한 생존율을 피봇테이블 형태로 작성한다. 
      df.pivot_table()
     index에는 성별(Sex)를 사용하고, column에는 선실(Pclass) 인덱스를 사용한다. 
'''
result2= df.pivot_table(values=['Survived'], index=['Sex'], columns=['Pclass'])

print(result2)

#pandas 문제 4)
'''
 1) human.csv 파일을 읽어 아래와 같이 처리하시오.
     - Group이 NA인 행은 삭제
     - Career, Score 칼럼을 추출하여 데이터프레임을 작성
     - Career, Score 칼럼의 평균계산
'''
human= pd.read_csv('../testdata/human.csv')

human_df = human.rename(columns=lambda x: x.strip())
human_df['Group'] = human_df['Group'].str.strip()
human_df = human_df[human_df['Group']!='NA']
print(human_df.head(5),"\n")
human_df2= human_df[['Career', 'Score']]
print(human_df2)
print(human_df2.mean())
'''
2) tips.csv 파일을 읽어 아래와 같이 처리하시오.
     - 파일 정보 확인
     - 앞에서 3개의 행만 출력
     - 요약 통계량 보기
     - 흡연자, 비흡연자 수를 계산  : value_counts()
     - 요일을 가진 칼럼의 유일한 값 출력  : unique()
          결과 : ['Sun' 'Sat' 'Thur' 'Fri']
'''
tip= pd.read_csv('../testdata/tips.csv')
print(tip)
print(tip.info())
print(tip.head(3))
print(tip.describe())
print(tip.value_counts(['smoker']))
print(np.unique(tip['day']))