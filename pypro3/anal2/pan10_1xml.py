'''Created on 2022. 4. 20. 4교시~ '''
# BeautifulSoup으로 XML 문서 처리
from bs4 import BeautifulSoup
import pandas as pd

with open('../testdata/my.xml', mode='r', encoding='UTF-8') as f:
    xmlfile=f.read()

print(xmlfile, type(xmlfile)) #<class 'str'>

soup = BeautifulSoup(xmlfile, 'lxml')
print(soup, type(soup)) #<class 'bs4.BeautifulSoup'>

# print(soup.prettify)
itemTag = soup.findAll('item')
print(itemTag[0])
print()

nameTag = soup.findAll('name')
print(nameTag[0]['id'])
print()
for i in nameTag:
    print(i['id'])

print('--------------')
for i in itemTag:
    nameTag = i.findAll('name')
    for j in nameTag:
        print('id:' + j['id'] + ', name:' + j.string)
    tel = i.find('tel')
    print('tel:' + tel.string)
    for j in i.find_all('exam'):
        print('kor:' + j['kor'] + ', eng:' + j['eng'])


print('--- 기상청 제공 날씨 정보 읽기--------------')
try: 
    import urllib.request as req
    url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
    plainText = req.urlopen(url).read().decode('UTF-8')
    # print(plainText)
    
    soup = BeautifulSoup(plainText, 'lxml')
    # print(soup)
    title = soup.find('title').string
    print(title)
    
    #wf = soup.find('wf')
    #print(wf)
    city = soup.find_all('city')
    #print(city)
    cityDatas = []
    for c in city:
        cityDatas.append(c.string)
    df = pd.DataFrame()
    df['city'] = cityDatas
    #print(df)
    tempMins = soup.select("location > province + city + data > tmn")
    # '>':직계자식 / '+':형제아래방향, '-':형제 위방향
    #print(tempMins)
    tempDatas = []
    for t in tempMins:
        tempDatas.append(t.string)
    df['temp_min'] = tempDatas
    df.columns = ['지역', '최저기온']
    print(df.head(3))
    print(df.tail(3))
    
    #df를 파일로 저장
    df.to_csv("날씨.csv", index=False)
    #print(pd.read_csv("날씨.csv"))
    
    print('-----')
    print(df[0:2])
    print(df[-2:len(df)])
    
    print()
    print(df.iloc[0], type(df.iloc[0])) #Series
    
    print()
    print(df.iloc[0:2, :])
    print(df.iloc[0:2, 0:1])
    print(df.iloc[0:2, 0:2])
    
    print()
    print(df.loc[1:3]) #1행부터 3행까지 출력
    print(df.loc[[1,3]]) #1행, 3행만 출력
    
    print()
    print(df.loc[1:3, ['최저기온', '지역']]) #칼럼명 설정
    
    print()
    print(df['최저기온'].mean())
    print(df['최저기온'].describe())
    
    print()
    df = df.astype({'최저기온':int})
    print(df.loc[df['최저기온'] >= 10])
    print(df.loc[(df['최저기온'] >= 10) & (df['최저기온'] <= 12)])
    
    print()
    print(df.sort_values(['최저기온'], ascending=True))
    
    
    
except Exception as e:
    print('err : ', e)
        
        
        