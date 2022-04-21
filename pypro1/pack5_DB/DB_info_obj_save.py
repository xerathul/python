#DB연결 정보를 객체로 저장
import pickle

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3307,
    'charset':'utf8',
    'use_unicode':True
}

with open('mydb1.dat','wb') as obj:
    pickle.dump(config, obj)