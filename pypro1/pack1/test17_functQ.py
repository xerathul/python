#https://cafe.daum.net/flowlife/RUrO/40
#키보드를 통해 직원 자료를 입력받아 가공 후 출력하기
datas=[]

import time
def inputfunc():
    count=0
    while True:
        inputList=input().split(',')
        print(inputList)
        print('계속하시겠습니까? (y/n)')
        isContinue=input() 
        datas.append(inputList)
        
        if isContinue=='y':
            count+=1
        elif isContinue=='n':
            return processfunc(datas)
        
    
#print('result',inputfunc())


def processfunc(datas):
    print('사번', '이름', '기본급', '근무년수','근속수당', '공제액', '수령액')
    
    for data in datas:
        #print(data)
        sal=int(data[2])
        year= time.localtime().tm_year-int(data[3])
        data[3]=year
        sudang=0
        gong=0
        resultSal=0
        
        if year<=3:
            sudang=150000
        elif year<=8:
            sudang=450000
        elif year>=9:
            sudang=1000000
        data.append(sudang)
        
        if sal+sudang>=3000000:
            gong= (sal+sudang)*0.5
        elif sal+sudang>=2000000:
            gong= (sal+sudang)*0.3
        elif sal+sudang<2000000:
            gong= (sal+sudang)*0.15
        data.append(gong)
        resultSal= sal+sudang-gong
        data.append(resultSal)
        for i in data:
            print(i, end=" ")
        
        
   
 
inputfunc()
