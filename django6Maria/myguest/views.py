from django.shortcuts import render
from myguest.models import Guest
from datetime import datetime
from django.http.response import HttpResponseRedirect
#from django.utils import timezone

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')

def ListFunc(request):
    print(Guest.objects.filter(title__contains = '오늘')) #[(T,F) 와 내용] list 
    print(Guest.objects.filter(id=1))
    print(Guest.objects.filter(title = '문안인사'))
    print(Guest.objects.get(id= 1))
    
    gdatas = Guest.objects.all()
    #gdatas = Guest.objects.all().order_by('title')    #ascending sort
    #gdatas = Guest.objects.all().order_by('-title')    #descending sort
    #gdatas = Guest.objects.all().order_by('-id','title')[0:2]    # id: ascending title: ascending sort
    return render(request, 'list.html',{'gdatas':gdatas})

def insert(request):
    return render(request, 'insert.html')

def insertOk(request):
    if request.method == "POST":
        #print(request.POST.get('title'))
        #print(request.POST['title'])
        Guest(
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            regdate = datetime.now()    #timezone.now()
        ).save() #insert into ...
        
    
    return HttpResponseRedirect('/guest')   #추가 후 목록 보기 redirect방식 : 클라이언트를 통해 자료 요청


''' 수정 할 때
gtab = Guest.objects.get(id = 해당 아이디)
gtab.title = '수정제목'
gtab.content = '수정내용'
gtab.svae()    'update table set...'
'''
''' 삭제
 gtab = Guest.objects.get(id = 해당 아이디)
 gtab.delete()     'delete from table...
'''
    