from django.shortcuts import render
from django.http.response import HttpResponseRedirect

# Create your views here.
def mainFunc(request):
    return render(request, 'index.html')

def setOsFunc(request):
    #print('request GET: ',request.GET)  #get 방식 요청 시 <QueryDict: {}>로 들어옴 
    if "favorite_os" in request.GET:
        print('request GET: ',request.GET['favorite_os'])
        # request.session['세션 키']
        request.session['f_os'] = request.GET['favorite_os']    #f_os라는 key로 세션 생성
        return HttpResponseRedirect('/showos') #redirect 방식 (client 컴을 통해 요청 함)
        
    else:
        return render(request, 'selectos.html')     #forward방식 (server 직접 파일 선택해 client로 전송(push)
    
def showOsFunc(request):
    dict_context={}
    if "f_os" in request.session:
        print('유효시간: ',request.session.get_expiry_age())
        dict_context['select_os']=request.session['f_os']
        dict_context['msg']='선택한 운영체제는 %s 입니다'%request.session['f_os']
    
    else:
        dict_context['select_os']=None
        dict_context['msg']='운영체제를 선택하지 않았어요'
    
    # del request.session['f_os']    세션 삭제
    request.session.set_expiry(5)   #세션 유효시간을 오초로 제한
    return render(request, 'show.html',dict_context)