# 함수: 실인수(매개변수)와 가인수의 매핑
#매개변수의 유형
#위치 매개변수, 기본값, 키워드, 가변 매개변수

def showGugu(start, end=5):
    for dan in range(start, end=5):
        print(dan,'단')


print()
def func1(*ar):
    print(ar)
    
func1('김밥')
func1('kim','bab','tuna')
print('------------')
def func2(a,*ar):
    print(a)
    for i in ar:
        print('배고프면',i)
func2('김밥')
func2('kim','bab','tuna')

print()
def process(choice, *ar):
    
    if choice == 'sum':
        res = 0
        for i in ar:
            res +=i
    elif choice == 'mul':
        res = 1
        for i in ar:
            res *=i
    return res
        
print(process('sum',1,2,3,4,5))
print(process('mul',1,2,3,4,5))

print()
def func3(w, h, **other):
    print('몸무게:{}, 키: {}'.format(w ,h))
    print(other)

func3(66, 177)
print()
func3(66, 177, irum='지구인', nai=22)

print()
def func4(a, b, *v1,**v2):
    print(a,b)
    print(v1)
    print(v2)
    
func4(1,2)
func4(1,2,3,4,5,m=6,n=7)