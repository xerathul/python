#BeautifulSoup 객체의 find(), select() 연습

from bs4 import BeautifulSoup
html_page ='''
<html>
<body>
<h1> 제목태그 </h1>
<p>웹문서 읽기</p>
<p>파이썬 라이브러리 사용</p>
</body>
</html>
''' 

print(html_page, type(html_page))   # <class 'str'>

soup= BeautifulSoup(html_page,'html.parser')    #Beutifulsoup 객체 생성
print(soup, type(soup))     # <class 'bs4.BeautifulSoup'>

print()
h1 = soup.html.body.h1
print(h1)
print('h1:',h1.string)
print('h1:',h1.text)

print()
p1 = soup.html.body.p
print(p1)
print('p1:',p1.text)

print()
p2 = p1.next_sibling.next_sibling
print(p2)

print('\nfind() 사용-----')
html_page2 ='''
        <html>
        <body>
        <h1 id="title"> 제목태그 </h1>
        <p>웹문서 읽기</p>
        <p id="my" class="our">파이썬 라이브러리 사용</p>
        </body>
        <a target="_blank" href="https://www.naver.com">naver</a>
        </html>
''' 

soup2= BeautifulSoup(html_page2,'lxml')    #Beutifulsoup 객체 생성
print(soup2.p,' ',soup2.p.string)   #직접 최초 p태그 선택
print(soup2.find('p').string)
print(soup2.find('p', id='my').string)
#print(soup2.find(['p','h1']))
print()
print(soup2.find(id='my').string)
print(soup2.find(id='title').string)
print(soup2.find(class_='our').string)
print('**********************')
print(soup2.findAll(['a'],{ 'target'  :  '_blank' }))
print(soup2.find(attrs={'class':'our'}).string)
print(soup2.find(attrs={'id':'title'}).string)
print('\nfindall() 사용----------')
html_page3 ='''
        <html>
        <body>
        <h1 id="title"> 제목태그 </h1>
        <p>웹문서 읽기</p>
        <p id="my" class="our">파이썬 라이브러리 사용</p>
        <div>
            <a href="https://www.naver.com">네이버</a>
            <a href="https://www.daum.com">다음</a>
        </div>
        </body>
        </html>
''' 
soup3= BeautifulSoup(html_page3, 'lxml')
print(soup3.find_all(['a']))
print(soup3.find_all(['a','p']))
print(soup3.findAll(['a','p']))
print(soup3.find_all('a'))

links= soup3.find_all('a')
for i in links:
    href = i.attrs['href']
    text= i.string
    print(href, ' ', text)
    
print()
import re
links2 = soup3.find_all(href=re.compile(r'^https'))     # 정규표현식
print(links2)

print('\n selector(css의 selector)--------')

html_page4 ='''
        <html>
        <body>
        <div>
           first div
        </div>
        <div id="hello">
            <a href="https://www.kbs.com">kbs</a>
            <a href="https://www.mbc.com">mbc</a>
            <span>
                <a href="https://www.tvn.com">tvn</a>
            </span>
        </div>
        <span>
            <a href="https://www.mbc.com">mbc</a>
        </span>
        <ul class="world">
            <li>안녕</li>
            <li>hello</li>
        </ul>
        <div id="hello" class="good">
            last div
        </div>
        </body>
        </html>
''' 
soup4= BeautifulSoup(html_page4, 'lxml')
aa= soup4.select_one("div")
print(aa)
print()
bb= soup4.select_one('div#hello')
print(bb)
print('^^^')
cc= soup4.select_one('div#hello > a')
print(cc)
print(cc.string)

print('~~~~~~~~~~~~~~~~')
dd = soup4.select("div#hello > a")  #복수선택(자식태그)
print(dd)
ee = soup4.select("div#hello  a")  #복수선택(자손태그)
print(ee)
ff= soup4.select('ul.world > li')
for k in ff:
    print('li: ', k.string)
    
print()
msg=list()  #msg=[]
for k in ff:
    msg.append(k.string)
    
import pandas as pd
df= pd.DataFrame(msg, columns=['자료'])
print(df)

