#두 집단 이하의 평균 또는 비율차이 검정
#t 분포는 표본 평균을 이용해 정규분포의 평균을 해석할 때 사용한다,
#독립변수 : 범주형, 종속변수: 연속형

#단일 모집단의 평균에 대한 가설검정(one samples t-test)
#하나의 집단에 대한 표본 평균이 예측된 평균(모집단의 평균)
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#연습 1 ) 어느 남성 집단의 평균 키는 177이다. 남성 집단의 표본 데이터를 추출해 평균차이 검정
#귀무 : 남성 집단의 평균 키는 177이다.
#대립 : 남성 집단의 평균 키는 177이 아니다.(양측검정)//177보다 크다(작다)-> (단측검정)

one_sample = [167.0, 182.7, 169.6, 176.8, 185.0]
print(np.array(one_sample).mean())  #177.21997 vs 177
#데이터의 정규성 확인
print(stats.shapiro(one_sample))    #pvalue=0.54005 > 0.05 이므로 정규성 만족

#검정 수행
result = stats.ttest_1samp(one_sample, popmean=177)
print('t값: %.3f, p-value:%.3f'%result)  #t값: -0.221, p-value:0.836
#해석 :  p-value:0.836 > 0.05 이므로 귀무가설 채택.

result2 = stats.ttest_1samp(one_sample, popmean=165)
print('t값: %.3f, p-value:%.3f'%result2) #t값: 3.185, p-value:0.033
#해석 :  p-value:0.033 > 0.05 이므로 귀무가설 기각.

print('-------------------------')
#실습 예제 1)
#A중학교 1학년 1반 학생들의 시험결과가 담긴 파일을 읽어 처리 (국어 점수 평균검정) student.csv
#A중학교 1학년 1반 학생들의 국어 시험결과는 늘 80 이라고 알려져 있다.

#귀무: A중학교 1학년 1반 학생들의 국어 시험결과는 늘 80 이라고 알려져 있다.
#대립: A중학교 1학년 1반 학생들의 국어 시험결과의 평균은 80이 아니다.
data = pd.read_csv('../testdata/student.csv')
print(data.head())
print(data['국어'].mean(), len(data))
print(stats.shapiro(data.국어))   #pvalue=0.01295970 < 0.05 정규성 만족 x
      
result = stats.ttest_1samp(data.국어, popmean= 80)
print('t값: %.3f, p-value:%.3f'%result)  #t값: -1.332, p-value:0.199
#해석 :  p-value:0.199 > 0.05 이므로 귀무가설 채택. 수집된 데이터는 우연히 발생된 자료이다.

print('+++++++++++++++++++++++++++++++++++++++')
#===============================================================================
# 실습 예제 2)
# 여아 신생아 몸무게의 평균 검정 수행 babyboom.csv
# 여아 신생아의 몸무게는 평균이 2800(g)으로 알려져 왔으나 이보다 더 크다는 주장이 나왔다.
# 표본으로 여아 18명을 뽑아 체중을 측정하였다고 할 때 새로운 주장이 맞는지 검정해 보자
#===============================================================================

#귀무:여아 신생아의 몸무게는 평균이 2800(g) 이다.
#대립:여아 신생아의 몸무게는 평균이 2800(g)이 아니다.

data2 = pd.read_csv('../testdata/babyboom.csv')
print(data2.head())

fdata = data2[data2.gender ==1] #여아데이터만
print(fdata.mean())             #3132 vs 2800
print(fdata.head(), len(fdata))

#정규성 확인
print(stats.shapiro(fdata.iloc[:,2]))   #pvalue=0.01798494 > 0.05 정규성 만족 x
print(stats.shapiro(fdata.weight))      

#시각화
sns.displot(fdata.iloc[:,2],kde = True)
plt.show()

stats.probplot(fdata.iloc[:,2], plot = plt)     #Q-Q plot 
plt.show()

result2 = stats.ttest_1samp(fdata.weight, popmean= 2800)
print('t값: %.3f, p-value:%.5f'%result2)  #t값: 2.233, p-value:0.03927
#해석 :  p-value:0.03927 < 0.05 이므로 귀무가설 기각. 수집된 데이터는 필연히 발생된 자료이다.
