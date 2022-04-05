"""
    사번과 이름을 입력하여 로그인에 성공하면 buser, jikwon: join
    사번, 직원명, 부서명, 부서전화, 연봉, 성별 출력
    1, 홍길동, 영업부, 123-1234, 12345, 남
"""
import pickle
import MySQLdb
with open('mydb.dat','rb') as obj:
    config= pickle.load(obj)
    
def login():
    try:
        conn= MySQLdb.connect(**config)
        cursor = conn.cursor()
        
        jikwon_no=input('사번입력: ')
        jikwon_name=input('이름입력: ')
        
        sql="""
            select jikwon_no, jikwon_name, buser_name, buser_tel, jikwon_pay, jikwon_gen 
            from jikwon inner join buser on buser_num=buser_no
            where jikwon_no={} and jikwon_name='{}'
        """.format(jikwon_no,jikwon_name)
        #print(sql)
        
        cursor.execute(sql)
        datas=cursor.fetchall()
        
        
        if len(datas)==0:
            print('로그인에 실패되었습니다')
        else:
            print('buser, jikwon: join')
            for i in datas:
                for ii in i:
                    print(ii,end=", ")
                
    except Exception as e:
        print('err: ',e)
    finally:
        cursor.close()
        conn.close()
        
if __name__=='__main__':
    login()