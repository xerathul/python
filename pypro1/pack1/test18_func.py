# 재귀함수 (recursive function): 함수가 자기자신을 호출

def countDown(n):
    if n ==0:
        print('완료')
    else:
        print(n, end = ' ')
        countDown(n-1) #자신을 호출

countDown(5)

print('종료')

print()

def tot(n):
    if n==1:
        print('escape')
        return True
    return n + tot(n-1)

res= tot(10)
print(res)

print()
# factorial : 1부터 정수 n까지의 값을 모두 곱한 것. n!

def facfunc(a):
    if a==1: return 1
    print(a)
    return a * facfunc(a-1)


print(facfunc(5))
