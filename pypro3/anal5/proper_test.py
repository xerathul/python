# 추론통계 분석 중 비율검정
# - 비율검정 특징
# : 집단의 비율이 어떤 특정한 값과 같은지를 검증.
# : 비율 차이 검정 통계량을 바탕으로 귀무가설의 기각여부를 결정.
import numpy as np
from statsmodels.stats.proportion import proportions_ztest
# # one-sample
# A회사에는 100명 중에 45명이 흡연을 한다. 국가 통계를 보니 국민 흡연율은 35%라고 한다.
# 비율이 같냐?

#귀무 :A회사의 흡연율과 국민 흡연율은 비율이 같다.
count = np.array([45])
nobs = np.array([100])
val = 0.35

z, p = proportions_ztest(count=count, nobs=nobs, value= val)
print(z,p)  #[2.01007563] [0.04442318]
#p : 0.04442318< 0.05 귀무기각. A회사의 흡연율과 국민 흡연율은 비율이 다르다.



# # two-sample
# A회사 사람들 300명 중 100명이 커피를 마시고, B회사 사람들 400명 중 170명이 커피를 마셨다.
# 비율이 같냐?
#귀무 : 두회사의 커피 마시는 사람들의 비율은 같다.
#대립 : 두회사의 커피 마시는 사람들의 비율은 다르다.
count = np.array([100,170])
nobs = np.array([300,400])

z, p = proportions_ztest(count=count, nobs=nobs, value= 0)  #비율이 제시되지 않았기 때문에 value= 0
print(z,p)  #-2.4656701201792273 0.013675721698622408
#p : 0.01367572 < 0.05 귀무기각. 두회사의 커피 마시는 사람들의 비율은 다르다.