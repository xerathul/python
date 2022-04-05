# 우편번호 data 파일 사용
# 키보드로 동이름을 입력해서 해당 동이름의 자료만 읽기

try: 
    dong = input('동 이름 입력 :')
    #dong='위례'
    #print(dong)
    
    with open(r'zipcode.txt','r',encoding='euc-kr') as f:
        line= f.readline()
        #print(line)
        
        while line:
            #lines=line.split('\t') #tap
            lines=line.split(chr(9)) #아스키 코드 값으로 분리 위 명령과 동일
            # print(lines)
            
            if lines[3].startswith(dong):
                print('['+lines[0]+'] '+lines[1]+' '+\
                      lines[2]+' '+lines[3]+' '+lines[4])
            line= f.readline()
except Exception as e:
    print('err: ', e)