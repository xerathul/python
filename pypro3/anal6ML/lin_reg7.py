# Linear Regression - 선형회귀의 평가 지표 score 정리 : MAE, MSE, RMSE, R_Squared
# r2_score, explained_variance_score, mean_squared_error를 사용
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model._base import LinearRegression #OLS Regression Results 를 지원하지 않음
from sklearn.metrics._regression import r2_score, explained_variance_score, mean_squared_error
from sklearn.preprocessing._data import MinMaxScaler #데이터를 0~1 사이의 범위로 표준화

#편차가 큰 표본데이터 작성
sample_size = 100
np.random.seed(1)

x = np.random.normal(0, 10, sample_size)
y = np.random.normal(0, 10, sample_size) +x*30

print(x[:5])
print(y[:5])
print('상관계수:',np.corrcoef(x,y))

# 독립변수 (x) 에 대한 표준화
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x.reshape(-1, 1))   #matrix 형태 (2차원)으로 표준화 진행
print(x_scaled[:5], x_scaled.shape) #[0.87492405] ... (100, 1)

#시각화
# plt.scatter(x_scaled, y)
# plt.show()

model = LinearRegression().fit(x_scaled,y)
#print(model.summary())     'LinearRegression' object has no attribute 'summary'

y_pred = model.predict(x_scaled)
print(y_pred[:5])
print(y[:5])

print()
#모델 성능 파악
def regScore(y_true, y_pred):
    print('r2_score(결정계수):{}'.format(r2_score(y_true, y_pred)))
    print('explained_variance_score(설명분산점수):{}'.format(explained_variance_score(y_true, y_pred)))
    print('mean_squared_error(평균 제곱근 오차):{}'.format(mean_squared_error(y_true, y_pred)))
    # mean_squared_error : 잔차의 제곱의 합을 표본수로 나눈 값. 분산분석의 SSE와 같음

regScore(y, y_pred)
# r2_score(결정계수):0.9987875127274646
# explained_variance_score(설명분산점수):0.9987875127274646 r2_score와 이값이 다르면 에러에 편향이 있음. 모델 학습이 잘못되었다는 뜻
# mean_squared_error(평균 제곱근 오차):86.14795101998743

print()
#분산이 큰 표본데이터 작성
x = np.random.normal(0, 1, sample_size)
y = np.random.normal(0, 500, sample_size) +x*30

print(x[:5])
print(y[:5])
print('상관계수:',np.corrcoef(x,y))

# 독립변수 (x) 에 대한 표준화
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x.reshape(-1, 1))   #matrix 형태 (2차원)으로 표준화 진행
print(x_scaled[:5], x_scaled.shape) #[0.87492405] ... (100, 1)

model = LinearRegression().fit(x_scaled,y)
y_pred = model.predict(x_scaled)

regScore(y, y_pred)
# r2_score(결정계수):1.6093526521765433e-05
# explained_variance_score(설명분산점수):1.6093526521765433e-05
# mean_squared_error(평균 제곱근 오차):282457.9703485092
