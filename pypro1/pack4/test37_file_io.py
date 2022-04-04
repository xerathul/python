# 파일 단위로 읽고 저장
import os

print(os.getcwd()) #파일의 경로 알려주기

try: 
    print('파일 읽기') #mode= r, w, a, +b
    f1 = open(r'C:\Sul_Acorn_java\GItrepo\python\pypro1\pack4\abc.txt',mode='r', encoding='utf-8')
    print(f1)
    print(f1.read())
    f1.close()
    
    print('파일 저장')
    f2 = open('abc2.txt', mode='w', encoding='utf-8')
    f2.write('my friend\n')
    f2.write('tom, 한국인')
    f2.close
    print('저장성공')
    
    print('파일추가')
    f3= open('abc2.txt',mode='a', encoding='utf-8')
    f3.write('\n오공')
    f3.write('\n팔계')
    f3.close()
    print('추가 성공')
    
    print('파일 읽기')
    f4= open('abc2.txt', mode='r', encoding='utf-8')
    print(f4.readline())
    print(f4.read())
    f4.close()
except Exception as e:
    print('에러: ',e)
    
print('파일 처리 계속----with문 사용 ')
try:
    with open('abc3.txt', mode='w', encoding='utf-8') as ff1:
        ff1.write('파이썬으로 문서 저장\n')
        ff1.write('with 문을 사용하면\n')
        ff1.write('명시적으로 close()할 필요 없다\n')
    print('저장 ok')
    
    with open('abc3.txt', mode='w', encoding='utf-8') as ff2:
        print(ff2.read())
    
except Exception as e2:
    print('에러: ',e2)
    
print('파일 처리 계속----pickle모듈 사용 ')
import pickle

try: 
    dicData={'tom':'111-1111','james':'222-2222'}
    listData=['채원','해승']
    tupleData=(dicData,listData)
    
    with open(file='hello.dat',mode='wb') as ff3:
        pickle.dump(tupleData,ff3)
        pickle.dump(listData,ff3)
    
    print('개체를 파일로 저장')
    
    with open(file='hello.dat',mode='wb') as ff4:
        a, b= pickle.load(ff4)
        print(a)
        print(b)
        c= pickle.load(ff4)
        print(c)
        
except Exception as e3:
    print('에러: ',e3) 