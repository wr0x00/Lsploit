from django.http import HttpResponse
from django.shortcuts import render
from .import strIng as Str
def hello(request):
    return HttpResponse("Hello world !")

def index(request):
    context={}
    context['tittle']=Str.String_CN.TITTEL
    context['welcome']=Str.String_CN.WELCOME
    context['issue']=Str.String_CN.ISSUE
    return render(request, 'index.html', context)
