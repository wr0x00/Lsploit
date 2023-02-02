from django.http import HttpResponse
from django.shortcuts import render
from libs.strings import String_CN as Str
from django.views.decorators.csrf import csrf_exempt

def hello(request):
    return HttpResponse("Hello world !")
    
@csrf_exempt 
def index(request):
    context={}
    context['tittle']=Str.TITTEL
    context['welcome']=Str.WELCOME
    context['issue']=Str.ISSUE
    return render(request, 'index.html', context)

@csrf_exempt
def sw(request):        #扫描目录页
    context={}
    context['tittle']=Str.TITTEL
    context['welcome']=Str.WELCOME
    context['issue']=Str.ISSUE
    context['url']=Str.URL
    context['do']=Str.DO
    print(request.POST.get("f_url"))
    return render(request, 'sw.html', context)

@csrf_exempt  
def sw_do(requests):
    import time
    from libs.web_sniff import httpx_dirscan
    context={}
    if requests.method == 'POST':
        #处理提交数据
        f_url = requests.POST.get('f_url')
        context['results'] = httpx_dirscan(f_url)
        context['goback'] = Str.GO_BACK
        time.sleep(10)
    return render(requests, 'results.html', context)