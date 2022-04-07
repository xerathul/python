from django.shortcuts import render

# Create your views here.
def indexFunc(request):
    return render(request, "index.html")

def resultFunc(request):
    gen= request.GET.get('gen')
    msg= request.GET.get('msg')
    return render(request, "result.html", {'gen':gen,'msg':msg})