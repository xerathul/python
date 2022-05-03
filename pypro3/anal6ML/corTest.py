#
# 상관관계 문제)
# https://github.com/pykwon/python 에 있는 Advertising.csv 파일을 읽어 
#tv,radio,newspaper 간의 상관관계를 파악하시오. 
# 그리고 이들의 관계를 heatmap 그래프로 표현하시오.
import seaborn as sns
import json
import matplotlib.pyplot as plt
import pandas as pd
plt.rc('font', family='malgun gothic')

data = pd.read_csv('../testdata/Advertising.csv')
data = data.set_index('no')
data= data.iloc[:,:3]
print(data.head())

#공분산
print(data.cov())

#상관계수
print(data.corr())

#시각화
sns.heatmap(data.corr())
plt.show()
