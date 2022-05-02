# [ANOVA 예제 2]
#
# DB에 저장된 buser와 jikwon 테이블을 이용하여 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 
#있는지 검정하시오.
# 만약에 연봉이 없는 직원이 있다면 작업에서 제외한다.

import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.formula.api import ols
import statsmodels.api as sm
from matplotlib import pyplot as plt
import pickle
import MySQLdb
from statsmodels.stats.anova import anova_lm

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
        from jikwon, buser
        where buser_num=buser_no
    '''
    cursor.execute(sql)
    df = pd.DataFrame(cursor.fetchall(), columns = ['부서','연봉'])
    print(df.head())
    print(df.부서.unique())
    g1 = df[df['부서']=='총무부']
    g2 = df[df['부서']=='영업부']
    g3 = df[df['부서']=='전산부']
    g4 = df[df['부서']=='관리부']
    print(g1.연봉.mean())     #5414.2857
    print(g2.연봉.mean())     #4908.3333
    print(g3.연봉.mean())#5328.5714
    print(g4.연봉.mean())     #6262.5
    
    #정규성
    print(stats.shapiro(g1.연봉)) #x
    print(stats.shapiro(g2.연봉)) #x
    print(stats.shapiro(g3.연봉)) 
    print(stats.shapiro(g4.연봉))
    p1=g1.연봉
    p2=g2.연봉
    p3=g3.연봉
    p4=g4.연봉
    
    #등분산성 만족
    print(stats.bartlett(p1,p2,p3,p4))  #pvalue=0.629095
    
    #일원분산분석
    print(stats.f_oneway(p1,p2,p3,p4))
    #pvalue=0.745442 > 0.05 귀무가설 채택. 부서에 따른 연봉에 차이가 없다.
    lmodel = ols('연봉 ~ C(부서)', data = df).fit()
    print(anova_lm(lmodel, typ=1))#0.745442
    #일원분산분석
    
    #사후검정
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    turkey_result = pairwise_tukeyhsd(endog =df.연봉, groups = df.부서)
    print(turkey_result)
    
    turkey_result.plot_simultaneous(xlabel ='mean', ylabel='group')
    plt.show()
except Exception as e:
    print('err: ',e)
finally:
    cursor.close()
    conn.close()