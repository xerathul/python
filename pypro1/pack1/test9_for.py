#반복문 for
#웹에서 읽은 자료라 가정 : 단어 수 출력 ex) 도이치:3

ss="""
이명박 전 대통령의 최측근이자 정권 실세인 강만수 전 산업은행장은 지인의 회사를 국책과제 수행업체로 선정해 정부지원금 
66억 원을 부당지원하고, 남상태 전 대우조선해장 사장을 압박해 이 회사에 44억 원을 투자하도록 하는 등 직권남용 권리행사 방해 
및 배임 등의 혐의로 지난 2018년 징역 5년 2개월을 선고받았다.
지난 2011년 3월 산업은행장으로 부임한 강 전 행장은 당시 임기영 대우증권 사장과 고재호 대우조선해양 사장에게도 
뇌물공여를 강요한 것으로 재판을 통해 밝혀졌다.
임 고문은 2004년 이후 도이치증권 부회장과 IBK투자증권, 대우증권 사장을 지낸 증권 통이며 2014년 한라홀딩스 
사장과 부회장, 한라대학교 이사장을 거쳤다. 도이치증권 도이치증권 도이치증권
SM은 임 고문을 감사후보자로 추천하면서 "한라홀딩스 대표이사 부회장 및 대우증권 대표이사 사장을 역임하는 등 경영 전반에 대한 충분한 경험과 지식을 갖추었으며, 고도의 준법이 요구되는 금융산업에서 풍부한 경험과 재무 전문성을 갖추었기에, 
전문성과 독립성을 바탕으로 회사 경영활동 전반을 합리적으로 감독하고 나아가 회사가 사회적 책임을 실천하는 데 기여할 것으로 판단한다"고 밝혔다.
"""

import re

ss2= re.sub(r'[^가-힣\s]', '', ss)
print(ss2)
ss3= ss2.split(sep=' ')
print(ss3)
print(len(ss3))
print(len(set(ss3)))
cou ={} # 단어의 발생 횟수를 dict로 저장
print(cou,'cou')
for i in ss3:
    if i in cou:
        cou[i] += 1
    else:
        cou[i] = 1 # {'키':i} 
print(cou)

print()
for test in['111-1234','일이삼-사오육칠','2222-3333']:
    if re.match(r'^\d{3,4}-\d{4}$', test):
        print(test)
    else:
        print('저나버노 ㅠㅠ')
        
print()
a=1,2,3,4,5,6,7,8,9,10
li=[]
for i in a:
    if i %2 ==0:
        li.append(i)
        
print(li)
print(list(i for i in a if i %2==0))

print()
datas=[1,2,'a',True,3.4]
li= [i for i in datas if type(i)==int]
print(li)

print()
datas={1,1,2,2,3}
se={i*i for i in datas}
print(se)

print()
id_name={1:'tom',2:'james'}
name_id= {value:key for key, value in id_name.items()}
print(name_id)

print()
temp =[1,2,3]
for i in temp:
    print(i, end=' ')
print()
print([i for i in temp])
print({i for i in temp})

print()
# 과일 값 계산
price={'apple':2000,'orange':1000,'mango':3000}
guest={'apple':2,'orange':1}
bill = sum(price[f]*guest[f] for f in guest) # 합을 구하는 내장함수

print(bill)



