# while: continue, break

a=0
while a<10:
#while True:
#while 1:
     a +=1
     if a ==5:continue
     if a ==7:break
     print(a)
else:
    print('while의 정상 처리')
print('while 수행 후 a : %d'%a)

# 난수(패턴이 없는 수)
import random
# random.seed(1)
print(random.random()) #0-1사이의 무작위 실수
print(random.randint(1, 10))

# 임의의 숫자 알아내기
num= random.randint(1,10)
while True:
    print('1 - 10사이의 컴이 가진 예상 숫자 입력')
    guess= int(input())
    print('guess',guess)
    if guess ==num:
        print('success'*5)
        break
    elif guess <num:
        print('insert bigger num')
    elif guess > num:
        print('insert less num')