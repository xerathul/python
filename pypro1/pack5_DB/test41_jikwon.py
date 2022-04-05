# 키보드로 부서번호를 입력 하여 해당 부서의 jikwon 자료 출력

import MySQLdb
"""
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}
"""
import pickle
with open('mydb.dat','rb') as obj:
    config= pickle.load(obj)
def chulbal():
    try:
        conn= MySQLdb.connect(**config)
        cursor = conn.cursor()
        
        buser_no= input('부서번호 입력: ')
        sql="""
            select jikwon_no, jikwon_name, buser_num, jikwon_pay
            from jikwon
            where buser_num={}
        """.format(buser_no)
        #print(sql)
        
        cursor.execute(sql)
        datas= cursor.fetchall()
        #print(datas)
        #print(len(datas))
        
        if len(datas)==0:
            print(buser_no,'번 부서는 없어요')
            return
        
        for jikwon_no, jikwon_name, buser_num, jikwon_pay in datas:
            print(jikwon_no, jikwon_name, buser_num, jikwon_pay)
            
        print('인원수: ',len(datas))
        
        
    except Exception as e:
        print('err: ',e)
    finally:
        cursor.close()
        conn.close()
        
if __name__=='__main__':
    chulbal()