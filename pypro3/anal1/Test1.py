import numpy as np
import seaborn as sns
from bs4 import BeautifulSoup
import pandas as pd
import urllib
'''
data = np.array([[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
[13,14,15,16]])

print(np.flip(data)) 
print('------------------')



titanic = sns.load_dataset('titanic')
print(titanic.head())
print(titanic.groupby(['sex'])['survived'].mean())
 
5.  BeautifulSoup의 findAll() 함수를 사용하려 한다.
파싱된 html 문서에서 "a" tag 들 중에서 속성이 target이고 속성값이 '_blank'인 것들만 모두 찾아 주는 
for 문을 작성하는 코드를 작성한다고 할 때 아래 빈칸을 채우시오. (배점:5)


for atag in convert_data.findAll(['a'], { 'target'  :  '_blank' }):
    pass
    
[문항7] 아래의 DataFrame에 대해 "실행결과 1" 이 나오도록 빈칸 ①에 적당한 명령문을 적으시오.
또한 열 삭제를 한 후 새로운 DataFrame type의 frame2를 만드는 명령을 빈칸 ②에 적으시오.
"실행결과 2" 와 같이 결과가 보일 수 있도록 한다. (배점:5)

from pandas import DataFrame
frame = DataFrame({'bun':[1,2,3,4], 'irum':['aa','bb','cc','dd']},
                  index=['a','b', 'c','d'])

print(frame.T)
frame2 = frame.drop('d')
print(frame2)

df = pd.read_csv('ex.csv', names=['a','b','c','d'])

[문항9] DataFrame이 아래와 같은 자료를 가지고 있다고 할 때 juso 칼럼 값 문자열을 잘라 0번째 자료를
Series 타입으로 취하기 위해서 필요한 코드를 작성하시오. (배점:5)
data = {
    'juso':['강남구 역삼동', '중구 신당동', '강남구 대치동'],
    'inwon':[23, 25, 15]
}
df = DataFrame(data)
results = ①_______([x.split()[0] for x in ②__________.juso])


df = pd.DataFrame(data)
print(df)
from pandas import Series
results = Series([x.split()[0] for x in df.juso])
print(results, type(results))

[문항10] sqlite DB를 사용하여 DataFrame의 자료를 db에 저장하려 한다. 아래의 빈칸에 알맞은 코드를 적으시오.

조건 : index는 저장에서 제외한다.
(배점:5)
data = {
    'product':['아메리카노','카페라떼','카페모카'],
    'maker':['스벅','이디아','엔젤리너스'],
    'price':[5000,5500,6000]
}

df = pd.DataFrame(data)
df.①__________('test', conn, if_exists='append', ②________________)

df.to_sql('test', conn,  if_exists= 'append', index= False)

[문항11] 크기가 다른 두 배열(numpy)을 작성하시오.

x 변수에는 1차원 배열의 요소로 1 2 3 4 5를, y 변수에는 2차원 배열(3행 1열)의 요소로 1 2 3을 저장한다. y변수는 reshape 함수를 사용한다.
두 배열 간 더하기(+) 연산을 하면 아래와 같은 결과가 나오는데 그 이유도 간단히 적으시오. (배점:10)
연산결과
[[2 3 4 5 6]
[3 4 5 6 7]
[4 5 6 7 8]]

x = np.arange(1,6)

y = np.arange(1,4).reshape(3,1)

print(x+y)

[문항12] 네이버 사이트가 제공하는 실시간 인기 검색어 자료를 읽어, 사람들에게 관심 있는 주제는 무엇인지 알아보려 한다.
title을 얻기 위해 ol tag 내의 li tag 값을 얻기 위한 코드를 아래와 같이 작성하였다.
프로그램이 제대로 수행될 수 있도록 아래의 빈 칸을 채우시오. (배점:10)
try:
      url = "http://www.naver.com"
      page = urllib.request.urlopen(url)
           
      soup = BeautifulSoup(page.read(), "1)___________") 
      title = soup.2)_____.find_all('li')
      for i in range(0, 10):
              print(str(i + 1) + ") " + title[i].a['title'])
3)_________ Exception as e:
      print('에러:', e)

try:
      url = "http://www.naver.com"
      page = urllib.request.urlopen(url)
           
      soup = BeautifulSoup(page.read(), "lxml") 
      title = soup.ol.find_all('li')
      for i in range(0, 10):
              print(str(i + 1) + ") " + title[i].a['title'])
except Exception as e:
      print('에러:', e)
      
[문항13] pandas 모듈을 이용하여 DataFrame 객체타입의 데이터를 test.csv 파일로 저장하려 한다.
index와 header는 저장작업에서 제외한다.
아래의 소스 코드를 순서대로 완성하시오. (배점:10)
data = DataFrame(items)
data.to_csv(                )

items = {
    'product':['아메리카노','카페라떼','카페모카'],
    'maker':['스벅','이디아','엔젤리너스'],
    'price':[5000,5500,6000]
}
data = pd.DataFrame(items)

data.to_csv('test.csv', header= False, index=False)

[문항14] "www.kyochon.com" 사이트에 접속해 상품을 읽은 후 가격에 대한 평균과 표준편차를 출력하시오.
조건 : BeautifulSoup 모듈을 사용하여 자료를 가공한 후 DataFrame에 상품명과 가격을 저장한다.
소스 코드와 가격에 대한 평균과 표준편차만 출력한다. (배점:10)
참고 : DataFrame의 내용은 아래와 같다. DataFrame의 내용은 출력하지 마시오.

            상품명      가격
0        발사믹치킨    18500
1        교촌오리지날  16000

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
url = "http://www.kyochon.com/menu/chicken.asp"
# 이하 소스 코드와 결과만 제출하시오.
'''
from bs4 import BeautifulSoup
import urllib.request 
import pandas as pd
url = "http://www.kyochon.com/menu/chicken.asp"

kyo = urllib.request.urlopen(url)
#print(kyo.read())

soup = BeautifulSoup(kyo, 'lxml')

pname = soup.select('dl.txt > dt')
names = list()
for i in pname:
    names.append(i.string)

price = soup.select('p.money > strong')

prices = list()
for i in price:
    a = i.string
    b= a.replace(',','')
    prices.append(int(b))

df = pd.DataFrame({'상품명': names, '가격': prices})

print(df['가격'].mean())#19709.677419354837
print(df['가격'].std())#2926.2438766798728


import MySQLdb
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

with open('mydb.dat', mode = 'rb') as obj:
    config = pickle.load(obj)
    
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
    select buser_name, jikwon_gen, jikwon_pay
    from jikwon inner join buser on buser_no=buser_num
    """
    cursor.execute(sql)
    
   
# 제시1) "buser_name, jikwon_gen, jikwon_pay" column을 읽어 DataFrame을 작성한 후 처음 2행만 출력하시오.
# 출력 결과
#    부서 성별    연봉
# 0  총무부  남  9900
# 1  영업부  여  8800
    df = pd.DataFrame(cursor.fetchall(),columns=['부서명','성별','연봉'])
    print(df.head(2))

# 제시2) pivot_table을 사용해 성별 연봉의 평균을 출력한다.
# 출력 결과
#      연봉
#성별     
#남  5980
#여  4630
    df.columns=['부서명','성별','연봉']
    pivot = df.pivot_table(['연봉'],index = '성별', aggfunc=np.mean)
    print(pivot)
# 제시3) 성별(남, 여) 연봉의 평균으로 시각화를 한다.
    plt.rc('font', family= 'malgun gothic')
   
    data= df.groupby(['성별'])['연봉'].mean()
    plt.bar(range(len(data)),data, color=['black','red'] )
    plt.xticks(range(len(data)), labels=['Male', 'Female'])
    plt.xlabel('gender')
    plt.ylabel('pay')
    plt.show()

# 제시4) 부서명, 성별로 교차 테이블을 작성한다.
# 출력 결과
#성별  남  여
#부서     
#관리부  2  2
#영업부  4  8
#전산부  3  4
#총무부  6  1
    ctab = pd.crosstab(df['부서명'], df['성별'])
    print(ctab)
