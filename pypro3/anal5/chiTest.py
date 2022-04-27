#===============================================================================
# * 카이제곱 검정
# 
# 카이제곱 문제1) 부모학력 수준이 자녀의 진학여부와 관련이 있는가?를 가설검정하시오
#   예제파일 : cleanDescriptive.csv
#   칼럼 중 level - 부모의 학력수준, pass - 자녀의 대학 진학여부
#   조건 :  level, pass에 대해 NA가 있는 행은 제외한다.
#===============================================================================
import pandas as pd
import scipy.stats as stats
import pickle
import MySQLdb
data = pd.read_csv('../testdata/cleanDescriptive.csv')
print(data.head(5))
print(data.info())
data.dropna(axis = 0)
print(data.head())
#귀무: 부모학력 수준은 자녀의 진학여부와 관련이 없다.
#대립: 부모학력 수준은 자녀의 진학여부와 관련이 있다.

ctab= pd.crosstab(index = data['level'],columns = data['pass'], dropna = True)
print(ctab)
ctab.index=['대학원졸', '대졸','고졸']
ctab.columns=['합격','불합격']
print(ctab)

chi_result = [ctab.loc['대학원졸'],ctab.loc['대졸'],ctab.loc['고졸']]
print(chi_result)

chi2, p, df, _ = stats.chi2_contingency(chi_result)
print(chi2, p, df, _)
#2.7669512025956684 0.25070568406521365
#해석 : 유의확률(p-value) 0.250705 > 0.05 이므로 귀무가설 채택. 검정에 참여한 데이터는 우연히 발생한 것이다.
# 부모학력 수준이 자녀의 진학여부와 관련이 없다.  독립이다.
print('--------------------')
#===============================================================================
# 카이제곱 문제2) 지금껏 A회사의 직급과 연봉은 관련이 없다. 
# 
# 그렇다면 정말로 jikwon_jik과 jikwon_pay 간의 관련성이 없는지 분석. 가설검정하시오.
#   예제파일 : MariaDB의 jikwon table 
#   jikwon_jik   (이사:1, 부장:2, 과장:3, 대리:4, 사원:5)
#   jikwon_pay (1000 ~2999 :1, 3000 ~4999 :2, 5000 ~6999 :3, 7000 ~ :4)
#   조건 : NA가 있는 행은 제외한다.
#===============================================================================

#귀무: 직원의 직급에 따른 연봉은 관련이 없다.
#대립: 직원의 직급에 따른 연봉은 관련이 있다.

try:
    with open('mydb1.dat', mode='rb') as obj:
        config= pickle.load(obj)
    
except Exception as e:
    print('err: ',e)
try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = '''
        select jikwon_jik, jikwon_pay from jikwon
    '''
    cursor.execute(sql)
    
    df1 = pd.DataFrame(cursor.fetchall(), columns = ['직급','연봉'])
    print(df1.head())
    df1['jikwon_jik']= df1['직급'].apply(lambda c:1 if c =='이사' else 2 if c=='부장' 
                                else 3 if c=='대리' else 4 if c=='과장' else 5)
    df1['jikwon_pay']= df1['연봉'].apply(lambda c:1 if c <3000 and c>= 1000 else 2 if c < 5000 
                                else 3 if c < 7000 else 4)
    print(df1.head())
    df1.dropna()
    ctab1 = pd.crosstab(index = df1['jikwon_pay'], columns= df1['jikwon_jik'])
    print(ctab)
    chi1, p,_,_ =stats.chi2_contingency(ctab1)
    print(chi1, p)
    
    #g해석 : 유의확률 p-value의 값이 0.000192115338이므로 귀무가설 기각
    #검정에 참여한 데이터는 필연적으로 발생한 것이다.
    #따라서 직급과 연봉에는 관계가 있다.
except Exception as e:
    print('err: ',e)
finally:
    cursor.close()
    conn.close()