from django.shortcuts import render
from dbapp.models import Article

# Create your views here.
def Main(request):
    return render(request, 'main.html')

def DBshow(request):
    datas= Article.objects.all()    #DJANGO ORM 사용 select * from article
    print(datas, type(datas))    #<class 'django.db.models.query.QuerySet'>
    print(datas[0].name)

    return render(request, 'list.html',{'articles': datas})
