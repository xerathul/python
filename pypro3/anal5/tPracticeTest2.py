# [two-sample t 검정 : 문제3]
#
# DB에 저장된 jikwon 테이블에서 총무부, 영업부 직원의 연봉의 평균에 차이가 존재하는지 검정하시오.
# 연봉이 없는 직원은 해당 부서의 평균연봉으로 채워준다.


import numpy as np
import scipy.stats as stats
import pandas as pd
import MySQLdb
import pickle

try:
    with open('mydb1.dat', mode='rb') as obj:
        config= pickle.load(obj)
    
except Exception as e:
    print('err: ',e)
try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = '''
        select buser_name, jikwon_pay
        from jikwon 
        inner join buser on buser_no = buser_num
    '''
    cursor.execute(sql)
    
    df = pd.DataFrame(cursor.fetchall(), columns=['부서','연봉'])
    #print(df)
    chong = df[df['부서']=='총무부'] #5414.285714
    sales = df[df['부서']=='영업부'] #4908.333333
    print(chong.연봉.mean())
    print(sales.연봉.mean())
    print('------------')
    #print(chong.isnull().sum(), sales.isnull().sum())   #결측치 없음
    
    
    #등분산성    pvalue=0.91504 > 0.05 => 등분산성 만족
    print(stats.levene(chong.연봉, sales.연봉))
    #LeveneResult(statistic=0.011723736898379184, pvalue=0.915044305043978)
    
    #정규성 불만족
    print(stats.shapiro(chong.연봉))  #pvalue=0.02604
    print(stats.shapiro(sales.연봉))  #pvalue=0.02560
    print(len(chong.연봉), len(sales.연봉)) #7 12
    #t-test
    result  = stats.mannwhitneyu(chong.연봉, sales.연봉)
    print(result)
    #pvalue=0.47213346 > 0.05 이므로 귀무채택
    #결론: 총무부, 영업부 직원의 연봉의 평균에 차이가 없다.
except Exception as e:
    print('err: ',e)
finally:
    cursor.close()
    conn.close()
