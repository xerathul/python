'''
pandas 문제 5)

 MariaDB에 저장된 jikwon, buser, gogek 테이블을 이용하여 아래의 문제에 답하시오.
     - 사번 이름 부서명 연봉, 직급을 읽어 DataFrame을 작성
     - DataFrame의 자료를 파일로 저장
     - 부서명별 연봉의 합, 연봉의 최대/최소값을 출력
     - 부서명, 직급으로 교차테이블을 작성(crosstab)
     - 직원별 담당 고객자료(고객번호, 고객명, 고객전화)를 출력. 담당 고객이 없으면 "담당 고객  X"으로 표시
     - 부서명별 연봉의 평균으로 가로 막대 그래프를 작성
'''
import MySQLdb
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
from h11 import _connection
plt.rc('font', family= 'malgun gothic')

try:
    with open('mydb1.dat', mode= 'rb') as obj:
        config = pickle.load(obj)
        
except Exception as e:
    print('err: ',e)

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    #사번 이름 부서명 연봉, 직급을 읽어 DataFrame을 작성
    sql= '''
        select jikwon_no, jikwon_name, buser_name, jikwon_jik
        from jikwon inner join buser
        on buser_num= buser_no
    '''
    cursor.execute(sql)
    
    df= pd.DataFrame(cursor.fetchall(),columns=['jikwon_no', 'jikwon_name', 'buser_name', 'jikwon_jik'])
    print(df)
    #DataFrame의 자료를 파일로 저장
    '''
    with open('jik_data2.csv', mode='w', encoding="UTF-8") as fobj:
        writer = csv.writer(fobj)
        for r in cursor:
            writer.writerow(r)
    '''
    #부서명별 연봉의 합, 연봉의 최대/최소값을 출력
    
    sql2= '''
        select jikwon_no, jikwon_name, buser_name, jikwon_jik, jikwon_gen, jikwon_pay
        from jikwon inner join buser
        on buser_num=buser_no
    '''
    cursor.execute(sql2)
    
    df2= pd.read_sql(sql2, conn)
    #print(df2.head())
    #print(df2.info())
    print('부서별 연봉의 합:', df2.groupby(['buser_name'])['jikwon_pay'].sum())
    print('연봉의 최대 값', df2.groupby(['buser_name'])['jikwon_pay'].max())
    print('연봉의 최소 값', df2.groupby(['buser_name'])['jikwon_pay'].min())
    
    print()
    #부서명, 직급으로 교차테이블을 작성(crosstab)
    
    ctab= pd.crosstab(df2['buser_name'], df['jikwon_jik'], margins=True)
    print(ctab)
    
    print()
    #직원별 담당 고객자료(고객번호, 고객명, 고객전화)를 출력. 담당 고객이 없으면 "담당 고객  X"으로 표시
    print('df.index :', len(df.index))
    for i in range(1, 30):
        sql3='''
            select gogek_no, gogek_name, gogek_tel
            from gogek inner join jikwon
            on gogek_damsano = jikwon_no
            where jikwon_no=%d
        '''%i
        cursor.execute(sql3)
        result= cursor.fetchone()
        #print(result)
        if result == None:
            print(df2['jikwon_name'][i],'담당고객 x')
        else:
            print(df2['jikwon_name'][i],'직원 담당 고객')
            df3= pd.read_sql(sql3, conn)
            df3.columns=['고객번호', '고객명', '고객전화']
            df3.set_index('고객번호', inplace = True)
            print(df3)
        

       
    #부서명별 연봉의 평균으로 가로 막대 그래프를 작성
    print(df2.groupby(['buser_name'])['jikwon_pay'].mean())
    
    plt.barh(range(4),df2.groupby(['buser_name'])['jikwon_pay'].mean())
    plt.show()
   
except Exception as e:
    print('err: ',e)
finally:
    cursor.close()
    conn.close()