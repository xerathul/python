#백준
from _ast import If


#두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
"""
a, b= map(int, input().split())
if a>b:
    print('>')
elif a<b:
    print('<')
elif a==b:
    print('==')
"""

#시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
'''
score=int(input())

if score>=90 and score<=100:
    print('A')
elif score>=80:
    print('B')
elif score>=70:
    print('C')
elif score >=60:
    print('D')
else:
    print('F')
'''

#연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
'''
year=int(input())
if year%4==0 and not year%100==0 or year%400==0:
    print(1)
else:
    print(0)
'''
#점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 작성하시오. 단, x좌표와 y좌표는 모두 양수나 음수라고 가정한다.d

    
    