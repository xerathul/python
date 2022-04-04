# 에러 발생에 따른 예외처리
#logic error, exception error: 파일, 네트워크, db


def divide(a, b):
    return a/b

print('...')
#c=divide(3,0) #ZeroDivisionError: division by zero

#print(c)

try: 
    c= divide(5,2)
    #c= divide(5,0)
    print(c)
    
    aa=[1,2]
    #print(aa[2])
    print(aa[1])
    
    open('c:/abc.txt')
    
except ZeroDivisionError:
    print('두번째 숫자는 0 안돼!')

except IndexError as er:
    print('참조 범위 오류: ',er)
except Exception as er:
    print('에러처리: ',er)
finally:
    print('에러와 상관없이 반드시 수행')
    
print('종료')