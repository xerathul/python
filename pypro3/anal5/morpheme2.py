# 인터넷에서 특정 단어로 검색된 문서를 읽어 형태소 분석 후 명사만 추출해 워드클라우드 실행

#pip install pygame  
#pip install simplejson
#pip install pytagcloud

from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
'''
keyword= input('검색어 입력:')
print(keyword)
print(quote(keyword))
'''

keyword = quote('마스크')

# 신문사 검색 기능 이용

url = 'https://www.donga.com/news/search?query='+keyword
#print(url)
source= urllib.request.urlopen(url)
soup=BeautifulSoup(source,'lxml', from_encoding='utf-8')

msg=''
for title in soup.find_all('p','tit'):
    title_link = title.select('a')
    #print(title_link)
    article_url = title_link[0]['href']
    #print(article_url)  #https://www.donga.com/news/article/all/20220426/113080623/1
    try:
        source_article = urllib.request.urlopen(article_url)    #각 타이틀에 있는 기사 내용 읽기
        soup = BeautifulSoup(source_article,'lxml', from_encoding='utf-8')
        contents = soup.select('div.article_txt')
        #print(contents)
        for imsi in contents:
            item = str(imsi.find_all(text=True))
            #print(item)
            msg = msg + item
        
    except Exception as e:
        pass
#print(msg)

from konlpy.tag import Okt
from collections import Counter #단어 개수 
okt =Okt()
nouns = okt.nouns(msg)  #문서 중 명사만 얻기

#print(nouns)    #['손아섭', '삼진', '콜', '당한', '후', '포수'....

result = []     #두 글자 이상의 단어만 저장
for imsi in nouns:
    if len(imsi) >1:
        result.append(imsi)
        
#print(result)   #['손아섭', '삼진', '당한', '포수', '장성우...
count= Counter(result)
tag = count.most_common(100)     # 상위 50 개만 작업에 참여
#print(tag)  [('마스크', 86), ('실외', 47), ('코로나', 44),

import pytagcloud   #워드 클라우드 만들기
taglist = pytagcloud.make_tags(tag, maxsize=100)
print('taglist:',taglist)

pytagcloud.create_tag_image(taglist, output='word.png', size=(1000,600), background=(0,0,0),
                            fontname="korean", rectangular=False)

#이미지 읽기
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#%matplotlib inline -> jupiter에서 선언하면 show() 안해도 됨

img = mpimg.imread('word.png')
plt.imshow(img)
plt.show()
