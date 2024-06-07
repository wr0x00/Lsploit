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


if demo_json["first"]==True:    #第一次使用该程序
    import os
    os.system("pip install -r requirement.txt -i https://pypi.tuna.tsinghua.edu.cn/simple && pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple && pip install bs4 -i https://pypi.tuna.tsinghua.edu.cn/simple && pip install prettytable -i https://pypi.tuna.tsinghua.edu.cn/simple && pip install httpx[http2] -i https://pypi.tuna.tsinghua.edu.cn/simple")
    import socket

    language=input("choose your local language/选择你的语言(EN|en|CN|cn):")
    demo_json["language"]=language
  
    if demo_json["language"]=='cn'or demo_json["language"]=='CN': #中文
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
        print(String.INSTALL)

    if demo_json["language"]=='en'or demo_json["language"]=='EN': #英文
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
        print(String.INSTALL)

    demo_json["first"]=False
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

if  __name__ == '__main__':
    from order import *
    import json,requests   

    # 读入示例json数据
    j=open("libs/configs.json",encoding='utf-8')
    demo_json = json.loads(j.read())

    if demo_json["language"]=='cn'or demo_json["language"]=='CN':from libs.strings import String_CN as Str #中文
    if demo_json["language"]=='en'or demo_json["language"]=='EN':from libs.strings import String_EN as Str #英文  
    
    print(banner)

    try:cve_info()    
    except requests.exceptions.SSLError: print("无漏洞播报，漏洞站貌似是崩了。。。")
    except requests.exceptions.ConnectionError:pass

    info=requests.get('http://myip.ipip.net',timeout=5).text
    print('\033[91m'+info+'\033[1;37;40m')    #广域地址
    
    while True:
        try:                        order=input("Lsploit>")
        except KeyboardInterrupt:   exit_()
        except IndexError:          continue
        if order == "exit":         exit_()
        if "set" in order:          order_deal_Setting(order)
        else:                       order_deal_Common(order,demo_json["proxy"])              


#end
