'''
 *@author: wr
 *@GitHub:https://github.com/wr0x00/Lsploit
 *@date: 2022.8.2
 *@description: django下嗅探功能
'''
# coding=utf-8
import sys
import time
import queue
import socket
from tokenize import String
from weakref import proxy
import requests
import httpx as hp
from signal import SIGINT, SIGTERM

import threading
import asyncio

#设置语言
if not __name__ == '__main__':
	try:
		import json
		# 读入示例json数据
		j= open('libs/configs.json', encoding='utf-8')
		demo_json = json.loads(j.read())

		if demo_json["language"]=='cn'or demo_json["language"]=='CN': #中文
			from .strings import String_CN as Str
		
		if demo_json["language"]=='en'or demo_json["language"]=='EN': #英文
			from .strings import String_EN as Str

	except Exception as e:
		from .strings import String_EN as Str
		print(e)


class httpx_dirscan():#携程扫描目录
    def __init__(self, Scan_URL, Scan_DICT="libs/dict.txt",Asyncio_Num=60,Scan_OUTPUT=0) -> None:
        import asyncio

        from datetime import datetime
        t1 = datetime.now()

        self.Asyncio_Num = Asyncio_Num#设置携程数

        print (Str.LOADING+Scan_URL)
        self.Scan_URL = Scan_URL if Scan_URL.find('://') != -1 else 'http://%s' % Scan_URL  #处理懒癌患者
        print (Str.TARGET+self.Scan_URL)
        
        self.Scan_DICT = Scan_DICT#字典路径
        self._loadDict(self.Scan_DICT)#加载字典

        '''创建日志'''
        self.Scan_OUTPUT = Scan_URL.rstrip('/').replace('https://', '').replace('http://', '')+'_webdir.txt' if Scan_OUTPUT == 0 else Scan_OUTPUT #写文件名 
        truncate = open(str(self.Scan_OUTPUT),'w')
        truncate.close()
        
        self._loadHeaders()#请求头
        self._analysis404()#404界面标例
        self.STOP_ME = False

        loop = asyncio.get_event_loop()
        results=loop.run_until_complete(self.run())

        results.append(Str.SUCCESS_WRITTEN+self.Scan_OUTPUT)
        results.append(Str.SUCCESS_SCAN+','+Str.TIME_TOTAL+format(datetime.now() - t1))
        return results
    def _loadDict(self, dict_list):
        self.q = queue.Queue()

        with open(dict_list,encoding='utf-8') as f:#读取字典txt
            for line in f:
                if line[0:1] != '#':
                    self.q.put(line.strip())#依次推入self.p链表

        if self.q.qsize() > 0:          #有
            print (Str.DICT_TOTAL+format(self.q.qsize()))
        else:                   #空
            print (Str.ERROT_DICT)
            quit()

    def _loadHeaders(self):
        self.headers = {
            'Accept': '*/*',
            'Referer': 'http://www.baidu.com',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; CIBA;',
            'Cache-Control': 'no-cache',
        }

    def _analysis404(self):
        notFoundPage = hp.get(self.Scan_URL + '/songgeshigedashuaibi/hello.html',proxies=proxy)
        self.notFoundPageText = notFoundPage.text.replace('/songgeshigedashuaibi/hello.html', '')

    def _writeOutput(self, result):
        #self.lock.acquire()# results = await asyncio.gather(*tasks)
        with open(self.Scan_OUTPUT, 'a+') as f:
            f.write(result + '\n')
        #self.lock.release()

    async def scan(self, url):
        html_result = 0
        try:
            #print(Str.NOW_TRYING+self.q.get())
            html_result = hp.get(url, headers=self.headers,timeout=2)
        except hp.ConnectTimeout:#防止被封锁
            # print 'Request Timeout:%s' % url
            #await asyncio.sleep(2)
            pass
        finally:
            if html_result != 0:
                if html_result.status_code == 200 and html_result.text != self.notFoundPageText:
                    
                    self._writeOutput('[%i]%s' % (html_result.status_code, html_result.url))#扫描一个写一个
                    return ('[%i]%s' % (html_result.status_code, html_result.url))
                    
    async def run(self):
        try:
            tasks = []
            for i2 in range(1,int(self.q.qsize())//self.Asyncio_Num):
                for i in range(1, self.Asyncio_Num):
                    ScanING_URL = self.Scan_URL + self.q.get()
                    tasks.append(asyncio.create_task(self.scan(ScanING_URL)))
            done,undone = await asyncio.wait(*tasks,timeout=10)
            
            return done
            '''
            if int(self.q.qsize())%self.Asyncio_Num>0:#如果有余数，将剩下的也扫完
                while not self.q.empty():
                    ScanING_URL = self.Scan_URL + self.q.get()
                    self.scan(ScanING_URL)
            results = await asyncio.gather(*tasks)
            for result in results:
            print(f"{result}")
            '''
        except KeyboardInterrupt:
            print(Str.STOPING)