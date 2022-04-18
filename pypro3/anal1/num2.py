#numpy 기본 이해

import numpy as np


print(np.__version__)

s = 'tom'
print(type(s))

ss=['tom','james','oscar']
print(ss,type(ss))

ss2 = np.array(ss)
print(ss2,type(ss2))

print('list/ndarray 기억 상태 구분')
li =list(range(1,10))
print(li)
#list 멤버 하나당 하나의 id가 부여되므로 속도가 느리고 데이터 용량이 큼
print(id(li[0]), id(li[1]))
print(li * 10)
print('-'* 10)

for i in li:
    print(i * 10, end = ' ')
print()
print([i * 10 for i in li])

print()
num_arr= np.array(li)
print(num_arr)
print(num_arr)
print(id(num_arr[0]), id(num_arr[1]))
# list 당 한 개의 아이디 부여
print(num_arr* 10)

print()
#a = np.array([1,2,'3.2']) # 데이터는 상위 타입을 따름 int> float> complex > str
a= np.array([1,2,3])
print(a,type(a),a.dtype, a.shape, a.ndim, a.size)

print(a[0], a[1:3], a[-1])      #a[-1] c차집합 아님

print()
b = np.array([[1,2,3],[4,5,6]])
print(b,type(b),b.dtype, b.shape, b.ndim, b.size)

print(b[0,], b[1:3,], b[-1,])      #a[-1] c차집합 아님
print(b[0,0],b[1,1])
print(b[[0]])

print('---------------')
c = np.zeros((2,2))
print(c)

d= np.ones((1,2))
print(d)

e= np.full((2,2),fill_value = 7 )
print(e)

f= np.eye(3)
print(f)

print()
print(np.random.rand(5), np.mean(np.random.rand(500)))    #균등분포
print(np.random.randn(5),np.mean(np.random.randn(500)))   #정규분포 

np.random.seed(1)
print(np.random.randn(2,3))

print(np.random.randint(10, size = 6))  #1차원
print(np.random.randint(10, size = (3,4)))  #2차원
print(np.random.randint(10, size = (3,4,5)))    #3차원

print()
print(list(range(0,10)))
print(np.arange(10))

print('------------인덱싱, 슬라이싱--------------')
a = np.array([1,2,3,4,5])
print(a[1:5:2])

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a[:])
print(a[1:])
print(a[-1,]) #뒤에서부터 카운팅
print(a[0],a[0][0],a[[0]])
print(a[1:,0:2])

print()
b = a[:2,1:3]   #서브 배열
print(b)
print(b[0,0])
print(a[0,1])

b[0,0]= 88
print(b)
print()
print(a)

print()
c= a[:2, 1:3].copy() #배열 사본 복사
print(c)
c[0,0] = 99
print(c)
print()
print(a)

print('------------------')
a = np.array([[1,2,3],[4,5,6],(7,8,9)])  #tuple or list 가능 set 은 안됨(순서가 있어야 함)
print(a.shape)
r1 = a[1, :]
r2 = a[1:2, :]
print(r1, r1.shape)
print(r2, r2.shape)
print()

a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])  #tuple or list 가능 set 은 안됨(순서가 있어야 함)
print(a.shape)
print()
b =np.array([1,2,0,1])  #a 배열 인덱싱용 배열
print(b,b.shape)
print()
print(np.arange(4))
print(a[np.arange(4),b])

print()
bool_idx = (a > 10)
print(bool_idx)

print(a[bool_idx])
print(a[a>10])
