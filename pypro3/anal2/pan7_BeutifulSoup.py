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
print(soup2.find(attrs={'class':'our'}).string)
print(soup2.find(attrs={'id':'title'}).string)

