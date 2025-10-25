
from django.http import HttpResponse
from django.shortcuts import render
from libs.strings import String_CN as Str
from django.views.decorators.csrf import csrf_exempt

from order import *
import sys

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
    print(request.POST.get("command_str"))
    return render(request, 'sw.html', context)

@csrf_exempt 
def sw_do(requests):
    import time
    from libs.web_sniff import httpx_dirscan
    import lp
    

    context={}
    if requests.method == 'POST':
        #处理提交数据
        command_str = requests.POST.get('command_str',None)
        #context['results'] = httpx_dirscan(command_str)
        #context['goback'] = Str.GO_BACK
        s = lp.capture_interactive(orderweb=command_str,tee=True)
        s['stop']()
        if "set" in command_str:           order_deal_Setting(command_str)
        else:                           order_deal_Common(command_str)   
        data={'results':repr(s['buffer'].getvalue()),}
    #return render(requests, 'results.html', context)
    return render(requests, 'sw.html', data)

# 在your_app/views.py文件中
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt 
def console(request):
    return render(request, 'console.html')

# 如果你的前端请求暂时不包含CSRF token，可以先使用此装饰器绕过检查（开发测试阶段）
@csrf_exempt 
def console_command(request):
    """
    处理发送到 /sw/do 的POST请求，执行命令并返回结果。
    """
    if request.method == 'POST':
        try:
            # 1. 获取前端发送的命令字符串
            # 方式一：如果前端以表单形式（application/x-www-form-urlencoded）发送数据
            #command_str = request.POST.get('command', '') 
            
            # 方式二：如果前端以JSON格式（application/json）发送数据
            json_data = json.loads(request.body)
            command_str = json_data.get('command', '')

            if not command_str:
                return JsonResponse({'error': '服务器未接收到命令'}, status=400)
            print(command_str)
            # 2. 这里是你的核心处理逻辑
            # 例如，将命令发送给后端处理器并等待结果
            result_string = your_backend_command_processor(command_str) # 你需要实现这个函数
            #result_string=command_str
            # 3. 将结果返回给前端
            # 返回纯文本字符串
            return HttpResponse(result_string, content_type='text/plain; charset=utf-8')
            # 或者返回JSON格式
            # return JsonResponse({'output': result_string})

        except json.JSONDecodeError:
            return JsonResponse({'error': '无效的JSON数据'}, status=400)
        except Exception as e:
            # 记录异常日志
            # logger.error(f"处理命令时发生错误: {str(e)}")
            
            return JsonResponse({'error': '服务器内部处理错误'}, status=500)
    else:
        # 如果不是POST请求，返回错误
        return JsonResponse({'error': '仅支持POST请求'}, status=405)
    
@csrf_exempt 
def your_backend_command_processor(command_str):
    """
    根据你的实际业务需要，在此处实现具体的命令处理逻辑。
    例如：
    - 调用子进程执行系统命令（需极其注意安全性！）
    - 与你的其他后端服务通信
    - 进行复杂的计算或数据库操作
    - 等等
    """
    # 示例：简单回显，实际应用中替换为你的处理逻辑
 
    import lp
    s = lp.capture_interactive(orderweb=command_str,tee=True)
    s['stop']()
    #if "set" in command_str:           order_deal_Setting(command_str)
    #else:                           order_deal_Common(command_str)   

    return  repr(s['buffer'].getvalue())
