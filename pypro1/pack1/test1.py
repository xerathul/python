'''
Created on 2022. 3. 28.
여러줄 주석
@author: u
'''
# 한줄 주석

print('hello python')
a= '안녕'
a='hello'
print(a*2)
a=10; b=20.5
c=b 
print(a,b,c)
print(a==b)


print(b==c)
a=10
b=10
print(a==b, a is b) # == 값 비교 연산자, is 주소 비교 연산자
aa=[10]
bb=[10]
print(a==b, aa is bb)

print()
import keyword
print(keyword.kwlist)
print('자료형 확인')
print(3, type(3))
print(3.4, type(3.4))
print(True, type(True))
print('bac',type('bac'))

print((1,), type((1,)))
print([1],type([1]))
print({1},type({1}))
print({'key':1},type({'key':1}))
