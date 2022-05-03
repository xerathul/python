# 회귀분석 문제 1) scipy.stats.linregress() <= 꼭 하기 
# : 심심하면 해보기 => statsmodels ols(), LinearRegression 사용
# 나이에 따라서 지상파와 종편 프로를 좋아하는 사람들의 하루 평균 시청 시간과 운동량 대한 데이터는 아래와 같다.
#  - 지상파 시청 시간을 입력하면 어느 정도의 운동 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.
#  - 지상파 시청 시간을 입력하면 어느 정도의 종편 시청 시간을 갖게 되는지 회귀분석 모델을 작성한 후에 예측하시오.
#     참고로 결측치는 해당 칼럼의 평균 값을 사용하기로 한다. 이상치가 있는 행은 제거. 10시간 초과는 이상치로 한다.
from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = pd.DataFrame([[1,0.9,0.7,4.2],[2,1.2,1.0,3.8],[3,1.2,1.3,3.5],[4,1.9,2.0,4.0],
                    [5,3.3,3.9,2.5],[6,4.1,3.9,2.0],[7,5.8,4.1,1.3],[8,2.8,2.1,2.4],[9,3.8,3.1,1.3],
                    [10,4.8,3.1,35.0],[11,np.NaN,3.5,4.0],[12,0.9,0.7,4.2],[13,3.0,2.0,1.8],
                    [14,2.2,1.5,3.5],[5,2.0,2.0,3.5]], columns = ['구분','지상파','종편','운동'])

data=data.fillna(data.지상파.mean())
data=data.drop(index = 9)
#print(data)

#1) scipy.stats.linregress()

x = data.지상파
y = data.운동

#상관계수 확인
#print(data.corr())  #-0.865535



#선형회귀 분석
model = stats.linregress(x, y)
#print(model)    #slope=-0.6684550167105405, intercept=4.709676019780582 pvalue=6.347578533142504e-05

tvTime= int(input('지상파 시청 시간을 입력:'))
print('예상 운동시간:', model.slope * tvTime + model.intercept)

#시각화
plt.scatter(x, y)
plt.plot(x, model.slope * x + model.intercept, 'r', label='Fitted line')
plt.show()