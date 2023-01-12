'''
 *@author: wr
 *@GitHub:https://github.com/wr0x00/Lsploit
 *@date: 2022.8.2
 *@description: 嗅探功能
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
import threading
from .strings import MessageSign as Sign

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

proxy=None
def set_agent(p,socks):#设置代理
    global proxy
    proxy=p
    socket.socket = socks.socksocket

def whois_sniff(URL)->None:
    '''
    功能：whois查询
    参数：URL网站地址    
    '''
    import whois
    print(whois.whois(URL))
def shodan_search(str)->None:
    '''
    功能：傻蛋批量搜索
    参数：str关键字
    '''
    import shodan
    SHODAN_API_KEY = "PSKINdQe1GyxGgecYz2191H2JoS9qvgD"#可以用自己的
    api = shodan.Shodan(SHODAN_API_KEY)
    try:
        results = api.search(str)
        for result in results['matches']:         
                print ("\033[0;32;40m%s\033[0m:\033[0;31m%s\033[1;37;40m|%s|%s"%(result['ip_str'],result['port'],result['location']['country_name'],result['hostnames']))
        print(Str.RESULTS_TOTAL+format(results['total']))
    except shodan.APIError as e:
        print (Str.ERROR_CONNECT+":"+e)

def start_dirscan(URL,Dict,thread=60):     #启动Dirscan类
    scan = Dirscan(URL, Dict, 0, thread)
    for i in range(thread):
        t = threading.Thread(target=scan.run)
        t.setDaemon(True)
        t.start()

    while True:
        if threading.activeCount() <= 1 :
            break
        else:
            try:
                time.sleep(0.1)
            except KeyboardInterrupt as e:
                print (f'\n{Sign.STR}{Str.STOPING},{Str.THREAD_EXIT},{Str.THREAD_TOTAL}{format(threading.activeCount())}')
                scan.STOP_ME = True

    print (Str.SUCCESS_SCAN)
class Dirscan(object):
    '''
    功能：扫描目录
    参数：scanSite网站地址,
         scanDict目录字典,      
         scanOutput输出文件名称,
         threadNum线程，        
    '''
    def __init__(self, scanSite, scanDict, scanOutput=0,threadNum=60):
        print (Str.LOADING+scanDict)
        self.scanSite = scanSite if scanSite.find('://') != -1 else 'http://%s' % scanSite
        print (Str.TARGET+self.scanSite)
        self.scanDict = scanDict
        self.scanOutput = scanSite.rstrip('/').replace('https://', '').replace('http://', '')+'_webdir.txt' if scanOutput == 0 else scanOutput
        truncate = open(self.scanOutput,'w')
        truncate.close()
        self.threadNum = threadNum
        self.lock = threading.Lock()
        self._loadHeaders()
        self._loadDict(self.scanDict)
        self._analysis404()
        self.STOP_ME = False

    def _loadDict(self, dict_list):
        self.q = queue.Queue()
        with open(dict_list,encoding='utf-8') as f:
            for line in f:
                if line[0:1] != '#':
                    self.q.put(line.strip())
        if self.q.qsize() > 0:
            print (Str.DICT_TOTAL+format(self.q.qsize()))
        else:
            print (Str.ERROT_DICT)
            quit()

    def _loadHeaders(self):
        self.headers = {
            'Accept': '*/*',
            'Referer': 'http://www.baidu.com',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; ',
            'Cache-Control': 'no-cache',
        }
    def _analysis404(self):
        notFoundPage = hp.get(self.scanSite + '/songgeshigedashuaibi/hello.html',proxies=proxy)
        self.notFoundPageText = notFoundPage.text.replace('/songgeshigedashuaibi/hello.html', '')

    def _writeOutput(self, result):
        self.lock.acquire()
        with open(self.scanOutput, 'a+') as f:
            f.write(result + '\n')
        self.lock.release()

    def _scan(self, url):
        html_result = 0
        try:
            html_result = hp.get(url, headers=self.headers,proxies=proxy,timeout=30)
        except hp.ConnectTimeout:
            # print 'Request Timeout:%s' % url
            pass
        finally:
            if html_result != 0:
                if html_result.status_code == 200 and html_result.text != self.notFoundPageText:
                    print ('[%i]%s' % (html_result.status_code, html_result.url))
                    self._writeOutput('[%i]%s' % (html_result.status_code, html_result.url))

    def run(self):
        while not self.q.empty() and self.STOP_ME == False:
            url = self.scanSite + self.q.get()
            self._scan(url)

def isIP(ip)->bool:
   #IP地址是否正确
  ip_addr = ip.split('.')
  if len(ip_addr) != 4:
   return False
  for ipnum in ip_addr:
   if not (0 <= int(ipnum) < 255):
     return False
  else:
   return True

def isurl(url)->bool:
    #判断网址是否可正常访问
    header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
    import requests as r
    re=r.get(url,headers=header,proxies=proxy)
    if re.status_code==200:
        return True
    if re.status_code==404:
        return False

class ScanPort:
    # 端口扫描工具
    def __init__(self,ip,maxport:int=65535):# 注意这个调用需要缀上.start()才能启动
        self.ip = ip
        self.maxport=maxport
 
    def scan_port(self, port):
        try:
            info=""
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            res = s.connect_ex((self.ip, port))
            portwd=open(r'modules/ports.txt','rb')
            if res == 0:  # 端口开启
                content=portwd.readlines()
                for c in content:   #从ports.txt中查找端口对应的服务        
                    if str(port)+Str.PORT in c.decode(encoding='UTF-8'):
                        info=c.decode(encoding='UTF-8').strip(str(port)+"端口：")
                        break
                    else:
                        continue
                print(f'地址:{format(self.ip)}\033[0;32;40m{Str.PORT}:{str(port)} \033[0m\t{info}')
                with open(self.ip+"_port",'a+',encoding="utf-8") as f:
                    f.write(str(port) +"\t"+info+'\n')
        except KeyboardInterrupt:
            s.close()
            pass
        finally:
            s.close()
 
    def start(self):
        try:
            from datetime import datetime
            from multiprocessing.dummy import Pool as ThreadPool
            ports = [i for i in range(0,self.maxport)]
            socket.setdefaulttimeout(0.5)
            truncate = open(self.ip+"_port",'w')
            truncate.close()
            print(Str.LOADING)
            # 开始时间
            t1 = datetime.now()
            
            # 设置多进程
            pool = ThreadPool(processes=100)
            pool.map(self.scan_port, ports)
            pool.close()
            pool.join()
            print(Str.SUCCESS_SCAN+','+Str.TIME_TOTAL+format(datetime.now() - t1))

        except KeyboardInterrupt:
            pass

class ScanPort_:
    # 模块化端口扫描工具
    # 由exp调用，后返回列表给exp
    def __init__(self,ip):# 注意这个调用需要缀上.start()才能启动
        self.ip = ip
        self.ports=[]
    def scan_port(self, port):
            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            res = s.connect_ex((self.ip, port))
            if res == 0:  # 端口开启
                print(f"{Str.FOUND}{Str.PORT}:{port}")
                self.ports.append(port)

    def start(self)->list:
        from multiprocessing.dummy import Pool as ThreadPool
        ports = [i for i in range(0, 65535)]
        socket.setdefaulttimeout(0.5)
        # 设置多进程
        try:
            pool = ThreadPool(processes=60)
            pool.map(self.scan_port,ports)
            pool.close()
            pool.join()
            return self.ports
        except KeyboardInterrupt:#守护线程池
            pool.terminate()

class httpx_dirscan():#携程扫描目录
    def __init__(self, Scan_URL, Scan_DICT, Scan_OUTPUT=0,Asyncio_Num=60) -> None:
        import asyncio
        self.Asyncio_Num = Asyncio_Num#设置携程数

        print (Str.LOADING+Scan_URL)
        self.Scan_URL = Scan_URL if Scan_URL.find('://') != -1 else 'http://%s' % Scan_URL  #处理懒癌患者
        print (Str.TARGET+self.Scan_URL)
        
        self.Scan_DICT = Scan_DICT#字典路径
        self._loadDict(self.Scan_DICT)#加载字典

        '''创建日志'''
        self.Scan_OUTPUT = Scan_URL.rstrip('/').replace('https://', '').replace('http://', '')+'_webdir.txt' if Scan_OUTPUT == 0 else Scan_OUTPUT#写文件名
        truncate = open(self.Scan_OUTPUT,'w')
        truncate.close()
        
        self._loadHeaders()#请求头
        self._analysis404()#404处理
        self.STOP_ME = False

        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.run())
        
    def _loadDict(self, dict_list):
        self.q = queue.Queue()
        with open(dict_list,encoding='utf-8') as f:
            for line in f:
                if line[0:1] != '#':
                    self.q.put(line.strip())
        if self.q.qsize() > 0:
            print (Str.DICT_TOTAL+format(self.q.qsize()))
        else:
            print (Str.ERROT_DICT)
            quit()

    def _loadHeaders(self):
        self.headers = {
            'Accept': '*/*',
            'Referer': 'http://www.baidu.com',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; ',
            'Cache-Control': 'no-cache',
        }
    def _analysis404(self):
        notFoundPage = hp.get(self.Scan_URL + '/songgeshigedashuaibi/hello.html',proxies=proxy)
        self.notFoundPageText = notFoundPage.text.replace('/songgeshigedashuaibi/hello.html', '')

    def _writeOutput(self, result):
        self.lock.acquire()
        with open(self.Scan_OUTPUT, 'a+') as f:
            f.write(result + '\n')
        self.lock.release()

    def _scan(self, url):
        html_result = 0
        try:
            html_result = hp.get(url, headers=self.headers,proxies=proxy,timeout=30)
        except hp.ConnectTimeout:
            # print 'Request Timeout:%s' % url
            pass
        finally:
            if html_result != 0:
                if html_result.status_code == 200 and html_result.text != self.notFoundPageText:
                    print ('[%i]%s' % (html_result.status_code, html_result.url))
                    self._writeOutput('[%i]%s' % (html_result.status_code, html_result.url))

    async def run(self):
        tasks = []
        for i in range(1, 5):
            tasks.append(asyncio.create_task(func1(i)))
#end
