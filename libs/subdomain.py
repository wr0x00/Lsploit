'''
 *@author: mocusez
 *@GitHub:https://github.com/wr0x00/Lsploit
 *@date: 2022.8.2
 *@description: 子域名扫描功能
'''

from glob import escape
import socket

def subdomain(domain, dictonary):
    try:
        with open(dictonary, 'r') as f:
            for i in f:
                i = i.strip()
                subdomain = i + '.' + domain
                try:
                    ip = socket.gethostbyname(subdomain)
                    print("\033[1;32;40m %s \033[0m" % (subdomain + '   ' + ip))
                except Exception:
                    pass
    except KeyboardInterrupt:
        exit()