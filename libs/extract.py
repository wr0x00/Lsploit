'''
 *@author: wr
 *@GitHub:https://github.com/wr0x00/Lsploit
 *@date: 2025.9.6
 *@description: 提取系统配置信息
'''
'''
CPU 信息

lscpu: 此命令显示 CPU 的详细信息，包括架构、型号、核心数、线程数等。

lscpu
内存信息

free: 使用此命令可以查看系统的内存使用情况，包括总内存、已使用内存、空闲内存和交换空间等。

free -m
磁盘信息

lsblk: 列出所有块设备的信息，如硬盘和分区等。

lsblk
df: 查看文件系统的磁盘空间使用情况。

df -h
网络接口信息

ifconfig 或 ip addr: 查看网络接口的详细信息，包括 IP 地址、MAC 地址和网关等。

ifconfig
或者

ip addr
硬件详细信息

dmidecode: 提供 BIOS、主板、内存和硬盘等硬件的详细信息。

dmidecode -t memory
PCI 设备信息

lspci: 列出所有 PCI 设备的信息，如网络适配器、声卡和显卡等。

lspci
USB 设备信息

lsusb: 列出所有 USB 设备的信息，如鼠标、键盘和 USB 存储设备等。

lsusb
'''
if not __name__ == '__main__':
	try:
		import json
		# 读入示例json数据
		j= open('libs/configs.json', encoding='utf-8')
		demo_json = json.loads(j.read())

		if demo_json["language"]=='cn'or demo_json["language"]=='CN':
			from .strings import String_CN as Str
		
		if demo_json["language"]=='en'or demo_json["language"]=='EN':
			from .strings import String_EN as Str

	except Exception as e:
		from .strings import String_EN as Str
		print(e)
		
def extract_linux(c:str):
    import os
    if c =='1':     os.system('lscpu')  #cpu
    if c =='2':     os.system('free -m')#内存
    if c =='3':     os.system('lsblk')  #硬件
    if c =='4':     os.system('df -h')  #磁盘
    if c =='5':     os.system('ifconfig')#网络接口
    if c =='6':     os.system('dmidecode -t memory')#硬件详细信息
    if c =='7':     os.system('lspci')#PCI 设备信息
    if c =='8':     os.system('lsusb')#USB 设备信息
def show():
    from prettytable import PrettyTable
    x = PrettyTable([Str.ORDINAL, "i后加空格加数字查看选项信息"])
    i=1
    x.add_row([format(i),"cpu"])
    i+=1
    x.add_row([format(i),"内存"])
    i+=1
    x.add_row([format(i),"硬件"])
    i+=1
    x.add_row([format(i),"磁盘"])
    i+=1
    x.add_row([format(i),"网络接口"])
    i+=1
    x.add_row([format(i),"硬件详细信息"])
    i+=1
    x.add_row([format(i),"PCI 设备信息"])
    i+=1
    x.add_row([format(i),"USB 设备信息"])
    return x
