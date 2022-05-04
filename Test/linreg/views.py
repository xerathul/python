from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.preprocessing._data import PolynomialFeatures
from sklearn.linear_model._base import LinearRegression
from sklearn.metrics._regression import r2_score
import matplotlib.pyplot as plt
from linreg.models import Jikwon
import datetime
import json
plt.rc('font', family ='malgun gothic')

# 원격 DB의 jikwon 테이블에서 근무년수에 대한 연봉을 이용하여 회귀분석 모델을 작성하시오.
# 장고로 작성한 웹에서 근무년수를 입력하면 예상 연봉이 나올 수 있도록 프로그래밍 하시오.
# LinearRegression 사용. Ajax 처리!!!
# Create your views here.

def main(request):
    return render(request, 'main.html')
def linreg(year):
    jikwons = Jikwon.objects.all().values()
    #print(jikwons)
    df = pd.DataFrame.from_records(data = jikwons)
    df.columns=['사번','직원명','부서','직급','연봉','입사','성별','평점']
    # print(df.head(3))
    df = df.loc[:,['입사','연봉','직급']]
    print(df.head(3))
    df['입사']=pd.to_datetime(df['입사'])
    df['입사'] =df['입사'].dt.year
    df['workYear']=2022 - df['입사']
    print(df.head(3))
    
    x= df[['workYear']].values
    y= df['연봉'].values
    #회귀분석
    model = LinearRegression()
    model.fit(x, y)
    x_fit = np.arange(x.min(), x.max(),1)[:, np.newaxis]
    y_lin_fit = model.predict(x_fit)
    model_r2 = r2_score(y, model.predict(x))
    print(model_r2)     #0.8457975498306587
    
    y_pred= model.predict(np.asmatrix(year))
    print(np.round(y_pred[0],0))
    payResult=np.round(y_pred[0],0)
    
    #직급별 연봉 평균 구하기
    jg= df['연봉'].groupby(df['직급']).mean()
    jgdf = pd.DataFrame(jg)
    print(jg, type(jg))
    
    Rjson= {'payResult':payResult,'model_r2':model_r2*100,'year':year,'jg':jgdf.to_html()}
    return Rjson
    
def insert(request):
    if request.method =="POST":
        # #print(request.POST.get('year'))
        year = request.POST.get('year')
        print(linreg(year))
        return render(request, 'result.html', linreg(year))