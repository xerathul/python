#묶음 자료형
# 자료형 중에서int, float, bool, complex : 객체 하나를 참조
# 자료형 중에서 str, list, tuple, set, dict : 객체값 여러개를 요소로 참조

# str : 문자열 자료형. 순서o : 인덱싱, 슬라이싱 가능, 수정 x
s= 'sequence'
print('길이: ',len(s))
print(id(s))
print('특정 문자 포함 위치 확인: ', s.count('e'), s.count('b'),s.find('e'))
# 다량의 문자열 관련 함수
s = 'xerathul' #새로운 객체를 치환
print(id(s))

print('\n\nList type--- :순서 o, 수정 o, 요소 값 중복o, 요소들을 []로 감쌈')
a =[1,2, 3, '문자열', 4.5, True,1,2,3]
print(a, type(a),id(a))
b=[a, 100, 200] #중복 리스트
print(b)
a= [2,2]
print(a, id(a))

print()
family=['mom','dad']
print(id(family))
family[0]= 'mommy'
print(id(family))
family.append('me') # 거의 어펜드 사용 중요!
family.insert(1, 'sister')
family.remove('me') #값에 의한 삭제
family.extend(['uncle','aunt'])
family += ['grandparents']
print(family)
del family[0] #순서에 의한 삭제
print(family)
del family #전체 지우기

print('\n\nTuple type--- :리스트와 유사, 수정x, 요소들을 ()로 감쌈')
t=('a',10,'b')
t='a',10,'b'
print(t)
print(t[0])
# t[0]='k' TypeError: 'tuple' object does not support item assignment
a=(1) #<class 'int'>
b=(1,) #<class 'tuple'>
print(type(a), type(b))

# 형변환
aa=[1,2,3]
bb= tuple(aa)
print(type(bb))
aa=list(bb)
print(type(aa))

print('\n\nSet type--- :순서x, 수정x, 중복 불가 요소들을 {}로 감쌈')
a={1,2,3,1}
print(a, type(a))
# print(a[0]) TypeError: 'set' object is not subscriptable'
b={3,4}
print(a.union(b)) #합집합
print(a.intersection(b)) #교집합
print(a - b, a | b, a&b)


b.update({5,6})
b.update([7,8])
b.update((9,10))
print(b)
b.discard(6) #해당 값 없으면 통과
b.remove(7) #해당값 없으면 에러
print(b)

print()
aa= [1,2,2,3,4,4]
print(aa,type(aa))
bb= set(aa)
print(bb)
aa=list(bb)
print(aa, type(aa))

print('\n\ndict type--- :순서x, 수정o, 요소들을 {"key":"value"}로 감쌈')
mydic =dict(k1=1, k2= 'abc', k3= 3.4)
print(mydic, type(mydic))

dic={'python':'snake','java':'coffee','spring':['S','whisky']}
print(dic)
print(dic['python'])
#print(dic[0]) KeyError: 0

dic['oracle']='predictor'
print(dic)
del dic['oracle']
print(dic)
dic['python'] ='language'
print(dic)

a=b=[1,2,3]
a[1]=4
print(b)
a="""
    \    /\\
     )  ( ')
    (  /  )
     \\(__)|
    """
print(a)