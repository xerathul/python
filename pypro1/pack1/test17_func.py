#함수 장식자 (function decorator) : meta기능이 있음
# 장식자는 또 다른 함수를 감싼 함수 이다.

def make2(fn):
    return lambda:'hi '+fn()

def make1(fn):
    return lambda:'nice to meet you '+fn()

def hello():
    return 'Tom'

hi= make2(make1(hello))

print(hi())

print()

@make2
@make1
def hello2():
    return 'Tom2'

print(hello2())

print()
hi2= hello2()
print(hi2)
hi3= hello2
print(hi3())

import time
print(time.localtime().tm_year)