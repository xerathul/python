#문1) 2~9 단 모두 출력


for i in range(2,10):
    for ii in range(1,10):
        print('{0}*{1}={2}'.format(i,ii,i*ii))
        
#문2) 1~100 사이의 정수중 3의 배수이면서 5의 배수의 합 출력
hap=0
for i in range (1,101):
    if i%3==0 and i%5==0:
        print(i)
        hap+=i
print('합:',hap)

#문 3) 주사위를 2번 던져서 나온 숫자들의 합이 4의 배수가 되는 경우만 출력
# 예) 1,3
iii=0
for i in range(1,7):
    for ii in range(1,7):
        #print(i,ii)
        iii=i+ii
        if iii % 4==0:
            print(i,ii,iii)
 