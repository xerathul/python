#네이버 제공 영화 랭킹 읽기


from bs4 import BeautifulSoup

#방법1 : urllib.request
import urllib.request
url= "https://movie.naver.com/movie/sdb/rank/rmovie.naver"

data= urllib.request.urlopen(url)
soup = BeautifulSoup(data, 'lxml')

#print(soup.select("div.tit3"))
#print(soup.select("div[class= tit3]"))
#print(soup.find_all("div",{'class':'tit3'}))
print(soup.findAll("div",{'class':'tit3'}))

for tag in soup.findAll("div",{'class':'tit3'}):
    print(tag.text.strip())
print('------------------------')
#방법2: requests
import requests
data = requests.get(url).text
soup2 = BeautifulSoup(data, 'lxml')
m_list =soup.find_all('div','tit3')

#print(m_list)
count =1
for i in m_list:
    title=i.find('a')
    print(count, '위:',title.string)
    count +=1