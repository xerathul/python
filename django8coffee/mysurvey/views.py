from django.shortcuts import render, redirect
from mysurvey.models import Survey
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
plt.rc('font',family= 'malgun gothic')


# Create your views here.
def surveyMain(requset):
    return render(requset,'main.html')

def surveyView(request):
    return render(request,'survey.html')

def surveyProcess(request):
    insertData(request)     #설문조사 결과를 DB에 저장
    return redirect('/coffee/surveyshow')   #분석결과 보기 요청
    
def insertData(request):
    if request.method == 'POST':
        # print(request.POST.get('gender'))
        # print(request.POST.get('age'))
        # print(request.POST.get('co_survey'))
        Survey(
            gender = request.POST.get('gender'),
            age = request.POST.get('age'),
            co_survey = request.POST.get('co_survey'),
            ).save()
        

def dataAnalycis(request):
    rdata= list(Survey.objects.all().values())
    df = pd.DataFrame(rdata)
    df.dropna()
    ctab = pd.crosstab(index=df['gender'], columns=df['co_survey'])
    print(ctab)
    
    #카이제곱 검정
    chi, pv, _, _ =stats.chi2_contingency(observed=ctab)
    print(chi, pv)
    
    if pv > 0.05:
        result = 'p값이 {0} > 0.05 이므로 성별과 커피 브랜드 선호도는 관련이 없다.(귀무채택)'.format(pv)
    else:
        result = 'p값이 {0} < 0.05 이므로 성별과 커피 브랜드 선호도는 관련이 있다.(귀무기각)'.format(pv)
        
    count = len(df)
    
    #시각화: 세로막대
    #dummy 변수 추가
    df['co_num']= df['co_survey'].apply(lambda c:1 if c =='스타벅스' else 2 if c =='이디야'
                                        else 3 if c == '커피빈' else 4)
    print(df)
    
    fig = plt.gcf()
    gender_group =df['co_survey'].groupby(df['co_num']).count()
    gender_group.index = ['스타벅스','이디야','커피빈','탐앤탐스']
    gender_group.plot.bar(subplots= True, width=0.5)
    plt.xlabel('커피브랜드명')
    plt.ylabel('커피브랜드별 선호 건수')
    plt.grid()
    print(df['co_survey'].groupby(df['co_num']))
    fig.savefig('django8coffee/mysurvey/static/images/coffeebar.png')
    
    
    return render(request, 'list.html',
                  {'ctab':ctab.to_html(),'result':result,'count':count})


