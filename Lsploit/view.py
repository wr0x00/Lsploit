from django.http import HttpResponse
from django.shortcuts import render
from libs.strings import String_CN as Str
def hello(request):
    return HttpResponse("Hello world !")

def index(request):
    context={}
    context['tittle']=Str.TITTEL
    context['welcome']=Str.WELCOME
    context['issue']=Str.ISSUE
    return render(request, 'index.html', context)

def sw(request):        #扫描目录页
    context={}
    context['tittle']=Str.TITTEL
    context['welcome']=Str.WELCOME
    context['issue']=Str.ISSUE
    context['url']=Str.URL
    context['get']=Str.GET
    print(request.POST.get("f_url"))
    return render(request, 'sw.html', context)
    
def sw_ajax(requests):
    n1=str(requests.POST.get('n1'))
    return HttpResponse(n1)