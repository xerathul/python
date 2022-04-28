# 두 집단 평균 또는 비율 차이 검정
# 두 집단의 가설검정 – 실습 시 분산을 알지 못하는 것으로 한정하겠다.
# 선행조건: 정규성, 등분산성

# * 서로 독립인 두 집단의 평균 차이 검정(independent samples t-test)
# 남녀의 성적, A반과 B반의 키, 경기도와 충청도의 소득 따위의 서로 독립인 두 집단에서 얻은 표본을 독립표본(two sample)이라고 한다.

# 실습) 남녀 두 집단 간 파이썬 시험의 평균 차이 검정
#귀무: 남녀 간의 파이썬 시험의 편균에 차이가 없다.
#대립: 남녀 간의 파이썬 시험의 편균에 차이가 있다.
import numpy as np
import scipy.stats as stats
import pandas as pd

male = [75, 85, 100, 72.5, 86.5]
female = [63.2, 76, 52, 100, 70]

df = pd.DataFrame([male,female])
df= df.T
df.columns=['male','female']
print(df)
print(df.male.mean())   #83.8
print(df.female.mean()) #27.24

#정규성, 등분산성 생략
two_sample = stats.ttest_ind(df.male, df.female)    #두 개의 표본에 대해 독립표본 t검정 실시
print(two_sample)
#Ttest_indResult(statistic=1.233193127514512, pvalue=0.2525076844853278)
#해석 : pvalue=0.252507 > 0.05 이므로 우연적으로 발생된 데이터다. (귀무채택)

print('-------------'*5)
#실습) 두 가지 교육방법에 따른 평균시험 점수에 대한 검정 수행 two_sample.csv
data=pd.read_csv('../testdata/two_sample.csv')
print(data.head())

ms = data[['method', 'score']]

print(ms)
m1 =ms[ms['method']==1] #방법1
m2 =ms[ms['method']==2] #방법2

score1 = m1['score']
score2 = m2['score']
# print(score1)

#df.isnull().sum >>널 확인

# sco1 = score1.fillna(0)     #nan을 0 으로 채우기
sco1 = score1.fillna(score1.mean())
sco2 = score2.fillna(score2.mean())

#등분산성 확인: 0.05이상이면 등분산성 만족
print(stats.levene(sco1, sco2))     #거의 이거씀
print(stats.fligner(sco1, sco2))    #데이터의 개수가 많을 때
print(stats.bartlett(sco1, sco2))   #데이터의 개수가 작을 때

#정규성
print(stats.shapiro(sco1))      #pvalue=0.3679
print(stats.shapiro(sco2))      #pvalue=0.671418
# LeveneResult(statistic=0.5626824030182838, pvalue=0.4568427112977609)
# FlignerResult(statistic=0.5878870391441374, pvalue=0.44323735267062647)
# BartlettResult(statistic=1.2274825627365802, pvalue=0.26789717886602216)
#정규성 시각화
import seaborn as sns
import matplotlib.pyplot as plt
sns.histplot(sco1, kde =True)
sns.histplot(sco2, kde =True)
plt.show()
# FlignerResult(statistic=0.5878870391441374, pvalue=0.44323735267062647)
# BartlettResult(statistic=1.2274825627365802, pvalue=0.26789717886602216)    비모수 검정

result = stats.ttest_ind(sco1, sco2, equal_var=True)    #등분산성 만족시
# result = stats.ttest_ind(sco1, sco2, equal_var=False)    #등분산성 불만족시
print('검정통계량t :%.5f, p-value:%.5f'%result)  #검정통계량t :-0.19649, p-value:0.84505
#해석 : p-value:0.84505 > 0.05 귀무 채택 
print(sco1.mean(), sco2.mean())     #5.199999999999999 5.246666666666667

#참고로 정규성 만족 못한경우
stats.mannwhitneyu(sco1, sco2)  #표본의 크기가 다를 때    
stats.wilcoxon(sco1, sco2)      #표본의 크기가 같을 때   
