'''
Created on 2022. 3. 29.

@author: u
'''
#문1) 1 ~ 100 사이의 숫자 중 3의 배수이나 2의 배수가 아닌 수를 출력하고, 합을 출력
i=0; hap=0
while i<101:
    if i % 3 ==0 and not i%2==0:
        print(i)
        hap+=i
    i+=1
print(hap)
print()

#문2) 2 ~ 5 까지의 구구단 출력
i=2 
while i<=5:
    j=1
    while j<=9:
        i*j
        print(str(i)+' * '+str(j)+' = '+str(i*j))
        j+=1
    i+=1

print()

#문3) -1, 3, -5, 7, -9, 11 ~ 99 까지의 합을 출력
i=-1; j=3; hap=0
while i>-100:
    hap+=i+j
    i-=4
    j+=4
print(hap)
    
    