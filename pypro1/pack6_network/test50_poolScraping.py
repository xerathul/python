'''Created on 2022. 4. 5.'''
# 멀티 프로세싱을 위한 스크래핑

# 멀티 프로세싱 없이 해볼게...
# https://beomi.github.io/beomi.github.io_old/ 사이트의 컨텐츠를 scraping

import requests #웹에 접근할 때 쓰는 모..모듈?
from bs4 import BeautifulSoup as bs #웹에서 데이터를 깔끔하게 가져올 때 쓴다.
import time

def get_link():     # 제목 a tag 읽기
    data = requests.get("https://beomi.github.io/beomi.github.io_old/").text
    soup = bs(data, 'html.parser') #requests와 parser는 나중에 배울 것
    # 사이트에서 a tag는 h3의 자식 요쇼.
    my_titles = soup.select(
        'h3 > a' # a 는 h3의 직계 자손이라는 표현
    )
    
    data = []
    
    for title in my_titles:
        data.append(title.get('href'))
        
    return data

def get_content(link):
    #print(link)
    abs_link = 'https://beomi.github.io' + link
    #print(abs_link)
    data = requests.get(abs_link).text
    soup = bs(data, 'html.parser')
    print(soup.select('h1')[0].text)
    
if __name__ == '__main__':
    startTime = time.time()
    #print(get_link())
    #print(len(get_link()))
    for link in get_link():
        get_content(link)
    
    print('---%s 초 ---'%(time.time()-startTime)) #긁어오는데 걸린 시간
    




