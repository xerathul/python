from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

def mainFunc(request):
    return render(request, "index.html")

class CallView(TemplateView):
    template_name= 'callget.html'
'''   
def insertFunc(request):
    return render(request, "insert.html")
 

def insertedFunc(request):
    #name= request.GET.get('name')
    name= request.GET['name']
    print(name)
    return render(request, "inserted.html", {'name':name})
    '''
#더 효율적으로 짜는 방법(한 함수로)

def insertFunc(request):
    if request.method=='GET':
        print('Get method requested')
        return render(request, "insert.html")
        
    elif request.method=='POST':
        print('Post method requested')
        name= request.POST.get('name')
        return render(request, "inserted.html", {'name':name})
    else:
        print('요청 에러')