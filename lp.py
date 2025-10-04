'''
 *@author: wr
 *@GitHub:https://github.com/wr0x00/Lsploit
 *@date: 2022.9.9
 *@description: 命令行程序入口
'''

import json

def ip_position(ip):#查询ip归属地api
    import requests as r
    print(r.get("http://ip-api.com/json/"+format(ip)+"?lang=zh-CN").text)

def exit_():
    print("\nbye")
    exit()

with open("libs/configs.json", "r",encoding='utf-8') as jsonFile:
    demo_json = json.load(jsonFile)

from libs.config.config import Config

# if demo_json["first"] == True
if Config().first == True:   #第一次使用该程序
    import os
    os.system("pip install -r requirement.txt -i https://pypi.tuna.tsinghua.edu.cn/simple && pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple && pip install bs4 -i https://pypi.tuna.tsinghua.edu.cn/simple && pip install prettytable -i https://pypi.tuna.tsinghua.edu.cn/simple && pip install httpx[http2] -i https://pypi.tuna.tsinghua.edu.cn/simple")
    import socket

    language=input("choose your local language/选择你的语言(EN|en|CN|cn):")
    demo_json["language"]=language
    Config.change_config_file(Config().fothers,"others","language",language)
  
    #f demo_json["language"]=='cn'or demo_json["language"]=='CN': #中文
    if Config().language=='cn' or Config().language=='CN':
        import requests
        from libs.strings import String_CN as String        
        print('\033[33m')   #黄色标记开始
        print(String.WARNING+"\n")  #警告语
        print(f"{String.LOCALNAME}{socket.gethostname()}")  #本机名
        print(f"{String.LOCALHOST_LAN}{socket.gethostbyname(socket.gethostname())}")    #局域地址
        try:
            info=requests.get('http://myip.ipip.net', timeout=5).text
            print(String.LOCALHOST_WAN+info)    #广域地址
            #ip_position(re.findall("\d+",info))
        except requests.exceptions.ConnectionError:pass
        print('\033[1;37;40m')#黄色标记结束
        #print(String.INSTALL)

    #if demo_json["language"]=='en'or demo_json["language"]=='EN': #英文
    if Config().language=='en' or Config().language=='EN':
        import requests
        from libs.strings import String_EN as String   
        print('\033[33m')   #黄色标记开始
        print(String.WARNING+"\n")  #警告语
        print(f"{String.LOCALHOST_LAN}{socket.gethostname()}")  #本机名
        print(f"{String.LOCALHOST_LAN}{socket.gethostbyname(socket.gethostname())}")    #局域地址
        try:
            info=requests.get('http://myip.ipip.net', timeout=5).text
            print(String.LOCALHOST_WAN+info)    #广域地址
            #ip_position(re.findall("\d+",info))
        except requests.exceptions.ConnectionError:pass
        print('\033[1;37;40m')#黄色标记结束
        #print(String.INSTALL)

    demo_json["first"]=False
    Config.change_config_file(Config().fothers,"others","first",False)

    with open("libs/configs.json", "w") as jsonFile:
        json.dump(demo_json, jsonFile,ensure_ascii=False)

banner="""
\033[32m
  ██╗     ███████╗██████╗ ██╗      ██████╗ ██╗████████╗
  ██║     ██╔════╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝
  ██║     ███████╗██████╔╝██║     ██║   ██║██║   ██║   
  ██║     ╚════██║██╔═══╝ ██║     ██║   ██║██║   ██║   
  ███████╗███████║██║     ███████╗╚██████╔╝██║   ██║   
  ╚══════╝╚══════╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝                                                                                                
\033[1;37;40m                                                                                                                            
"""    #打印装逼标志


from order import *
import json,requests
from io import StringIO
from contextlib import redirect_stdout
import sys

def IO(noninteractive=False):
    # 读入示例json数据
    j=open("libs/configs.json",encoding='utf-8')
    demo_json = json.loads(j.read())
    '''
    if demo_json["language"]=='cn'or demo_json["language"]=='CN':from libs.strings import String_CN as Str #中文
    if demo_json["language"]=='en'or demo_json["language"]=='EN':from libs.strings import String_EN as Str #英文 
    '''
    if Config().language=='cn' or Config().language=='CN':from libs.strings import String_CN as Str #中文
    if Config().language=='en' or Config().language=='EN':from libs.strings import String_EN as Str #英文  
    
    #if demo_json["first"]==False:       print(Str.WELCOME)
    if Config().first == False:     print(Str.WELCOME)
    print(banner)

    try:cve_info()    
    except requests.exceptions.SSLError: print("无漏洞播报，漏洞站貌似是崩了。。。")
    except requests.exceptions.ConnectionError:pass

    info=requests.get('http://myip.ipip.net',timeout=5).text
    print('\033[91m'+info+'\033[1;37;40m')    #广域地址

    # 如果以非交互方式运行（用于捕获输出），直接返回，避免进入交互循环阻塞
    if noninteractive:
        return
    
    while True:
        try:                        order=input("Lsploit>")
        except KeyboardInterrupt:
            exit_()
            return 1
        except IndexError:          continue
        if order == "exit":         
            exit_()
            return 1
        if "set" in order:          order_deal_Setting(order)
        else:                       order_deal_Common(order,demo_json["proxy"])   

'''
def capture_stdout(func, *args, tee=False, **kwargs):
    buf = StringIO()
    if tee:
        class Tee:
            def __init__(self, *streams): self.streams = streams
            def write(self, s):
                for st in self.streams: st.write(s)
            def flush(self):
                for st in self.streams:
                    try: st.flush()
                    except: pass
        out_stream = Tee(sys.stdout, buf)
    else:
        out_stream = buf

    with redirect_stdout(out_stream):
        result = func(*args, **kwargs)
    return result, buf.getvalue()
'''

def capture_interactive(func, *args, tee=True, **kwargs):
    """在后台线程运行交互式函数，同时捕获 stdout（可 tee 到终端）并记录 input() 的输入。

    返回一个字典，包含：
      - thread: 正在运行的线程对象
      - buffer: StringIO 对象，可随时用 .getvalue() 读取当前捕获的输出
      - inputs: 列表，记录了 (prompt, value) 的历史输入
      - stop(): 一个函数，恢复被替换的 input 并等待线程结束

    注意：该函数不会主动结束被运行的交互函数（除非函数本身退出，例如用户输入 exit），stop() 会等待线程结束。
    """
    import threading, builtins

    buf = StringIO()
    inputs = []

    # 记录并转发真实输入
    original_input = builtins.input

    def logged_input(prompt=''):
        val = original_input(prompt)
        try:
            inputs.append((prompt, val))
        except Exception:
            pass
        return val

    builtins.input = logged_input

    if tee:
        class Tee:
            def __init__(self, *streams): self.streams = streams
            def write(self, s):
                for st in self.streams: st.write(s)
            def flush(self):
                for st in self.streams:
                    try: st.flush()
                    except: pass
        out_stream = Tee(sys.stdout, buf)
    else:
        out_stream = buf

    def target():
        # 在线程内重定向 stdout 到 out_stream
        with redirect_stdout(out_stream):
            try:
                func(*args, **kwargs)
            finally:
                # 当交互函数结束后，恢复 input
                try: builtins.input = original_input
                except: pass

    thread = threading.Thread(target=target, daemon=True)
    thread.start()

    def stop():
        # 恢复 input 并等待线程结束
        try: builtins.input = original_input
        except: pass
        thread.join()

    return {
        'thread': thread,
        'buffer': buf,
        'inputs': inputs,
        'stop': stop,
    }
'''
try:
    s = capture_interactive(IO, tee=True)
    s['stop']()
except KeyboardInterrupt:
    
    print("记录:", repr(s['buffer'].getvalue()))
finally:
    print("记录:", repr(s['buffer'].getvalue()))
    '''
if __name__ == "__main__":
    IO()
#end
