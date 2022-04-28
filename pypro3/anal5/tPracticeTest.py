#===============================================================================
# [one-sample t 검정 : 문제1]  
# 
# 영사기에 사용되는 구형 백열전구의 수명은 250시간이라고 알려졌다. 
# 한국연구소에서 수명이 50시간 더 긴 새로운 백열전구를 개발하였다고 발표하였다. 
# 연구소의 발표결과가 맞는지 새로 개발된 백열전구를 임의로 수집하여 수명시간을 수집하여 다음의 자료를 얻었다. 
# 한국연구소의 발표가 맞는지 새로운 백열전구의 수명을 분석하라.
#===============================================================================
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


data = [305, 280, 296, 313, 287, 240, 259, 266, 318, 280, 325, 295, 315, 278]
print(np.array(data).mean())    #289.7857142857143

#데이터의 정규성 확인
print(stats.shapiro(data))  #pvalue=0.8208622 > 0.05 이므로 정규성 만족

#검정 수행
result = stats.ttest_1samp(data, popmean=250)
print('t값: %.3f, p-value:%.5f'%result)  #t값: 6.062, p-value:0.00004
#해석 :  p-value:0.00004 < 0.05 이므로 귀무가설 기각.

result = stats.ttest_1samp(data, popmean=300)
print('t값: %.3f, p-value:%.5f'%result)  #t값: -1.556, p-value:0.14361
#결론 :  p-value:0.14361 > 0.05 이므로 50시간 더 긴 수명인 한국연구소의 발표가 맞았다.
print('==============================================')
#===============================================================================
# [one-sample t 검정 : 문제2] 
# 
# 국내에서 생산된 대다수의 노트북 평균 사용 시간이 5.2 시간으로 파악되었다. A회사에서 생산된 노트북 평균시간과 차이가
# 있는지를 검정하기 위해서 A회사 노트북 150대를 랜덤하게 선정하여 검정을 실시한다.
# 실습 파일 : one_sample.csv
# 참고 : time에 공백을 제거할 땐 ***.time.replace("     ", "")
#===============================================================================

one_sample= pd.read_csv('../testdata/one_sample.csv')
print(one_sample.head())
one_sample=one_sample.replace("     ", "")
one_sample.time=pd.to_numeric(one_sample.time)
one_sample=one_sample.dropna(how='all',axis=0)
one_sample=one_sample.dropna(axis=0)
print(one_sample.time.mean())   #5.5568807339449515

#검정 수행
result = stats.ttest_1samp(one_sample.time, popmean=5.2)
print('t값: %.3f, p-value:%.5f'%result)  #t값: 3.946, p-value:0.00014
#해석 :  p-value:0.00014 < 0.05 이므로 귀무가설 기각.
#===============================================================================
# [one-sample t 검정 : 문제3] 
# 
# https://www.price.go.kr/tprice/portal/main/main.do 에서 
# 메뉴 중  가격동향 -> 개인서비스요금 -> 조회유형:지역별, 품목:미용 자료를 파일로 받아 미용 요금을 얻도록 하자. 
# 정부에서는 전국 평균 미용 요금이 15000원이라고 발표하였다. 이 발표가 맞는지 검정하시오.
#===============================================================================

price = pd.read_csv('../testdata/price.csv')
price=price.T
print(price)
price= price.iloc[3:,:]
print(price)
price.columns=['가격']
print(price)
print(price.가격.mean())  #16743.5625
price=price.dropna(subset=['가격'])
priceresult= stats.ttest_1samp(price.가격, popmean = 15000)
print('t값: %.3f, p-value:%.5f'%priceresult)  #t값: 3.990, p-value:0.00118
#해석 :  p-value:0.00118 < 0.05 이므로 귀무가설 기각.