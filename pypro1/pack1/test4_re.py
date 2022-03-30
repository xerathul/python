# 정규 표현식 : 대량의 문자열에 대해 일정한 패턴을 부여해 원하는 문자열만 취할 수 있다.
import re

ss= '12345 abc가나다funABC_123555_6"Python is fun'
print(ss)
print(re.findall('123', ss))
aa=re.findall(r'123', ss)
print(aa[0])
print(re.findall('가나', ss))
print(re.findall('[12]', ss))
print(re.findall('[0-9]', ss))
print(re.findall('[0-9]+', ss))
print(re.findall('[0-9]?', ss))
print(re.findall('[0-9]*', ss))
print(re.findall('[0-9]{2}', ss))
print(re.findall('[0-9]{2,3}', ss))
print(re.findall('[a-z]', ss))
print(re.findall('[a-zA-Z]', ss))
print(re.findall('[가-힣]', ss))
print(re.findall('[^가-힣]', ss))
print(re.findall('.bc.', ss))
print(re.findall('a..', ss))
print(re.findall('^123', ss))
print(re.findall('fun$', ss))
print(re.findall('12|34', ss))
print(re.findall('(ab)+(c)', ss))
print(re.findall('\d\d', ss))

p=re.compile('abc')
print(re.findall(p, ss))

p=re.compile('the',re.IGNORECASE)
print(p.findall('The DoG the dog'))