#교차분석(카이제곱, 카이 스퀘어) 가설 검정
#범주형 자료를 대상으로 교차 빈도에 대한 기술 통계량(검정 통계량)을 제공해 줄 뿐 아니라, 
# 교차 빈도에 대한 통계적 유의성을 검증 해주는 추론통계 분석 기법

import numpy as np
import pandas as pd
data = pd.read_csv('../testdata/pass_cross.csv', encoding='euc-kr')
print(data.head())

#귀무가설(H0): 벼락치기 공부하는 것과 합격 여부는 관계가 없다
#대립가설(H1): 벼락치기 공부하는 것과 합격 여부는 관계가 있다
#귀무가설 설정: ...같다. 다르지 않다. 차이가 없다. 효과가 없다. 보수적으로 선언
#대립 설정: 귀무가설과 반대로 설정

#print(data.shape)    (50, 4)

print(data[(data['공부함']== 1) & (data['합격'] == 1)].shape[0])     #18
print(data[(data['공부함']== 1) & (data['불합격'] == 1)].shape[0])    #7

print('빈도표 ----------')

#ctab=pd.crosstab(index = data['공부함'],columns=data['합격'], margins=True)
ctab=pd.crosstab(index = data['공부안함'],columns=data['불합격'], margins=True)
ctab.columns=['합격','불합격','합']
ctab.index=['공부함','공부안함','합']

print(ctab)

#교차분석 연습1: 수식을 사용 
#관찰 값: 수집된 데이터 값
#기대 값: 어떤 확률을 가진 사건을 무한히 반복했을 때 얻을 수 있는 값이 평균
# 검정통계량 카이제곱 = 합(관측값 - 기대값)제곱 / 기대값 : x축의 임의 지점 값을 구함. 임계치를 기준으로 가설을 판단할 때 사용.
# 기대도수 = 빈도표의 (각 행의 주변합) *  (각 열의 주변합) / 총합

chi2 = (18 -15 ) **2 /15 +(7 -10) ** 2/ 10 +(12 - 15) ** 2/15+(13-10)**2/10
print('카이제곱 값:', chi2)
print('자유도 : ',2-1) #(행의 개수 -1) * (열의 개수 -1 )

#카이 제곱표를 통해 임계치 얻기: df:1, 알파 값 :0.05 이므로  임계치 3.84
#결론 : 카이제곱 값 3.0 < 임계치 < 3.84 이므로 chi2 값은 귀무 채택 역 내에 있어 귀무가설을 채택한다.
#그러므로 벼락치기 공부하는 것과 합격여부는 관계가 없다. 는 주장을 유지한다.

print()

#교차 분석 연습2: 모듈이 제공하는 p-value를 사용
import scipy.stats as stats

chi2, p, _, _=stats.chi2_contingency(ctab)
print('chi2:{}, p-value:{}'.format(chi2, p))

#결론 : 유의수준(α) 0.05 < p-value:0.557825이므로 귀무가설 채택
# 검정에 사용된 데이터는 우연히 발생된 데이터다.

