# Lsploit

![](https://img.shields.io/badge/Size-4MB-informational?style=for-the-badge&logo=appveyor)
![](https://img.shields.io/badge/tested-termux-green?style=for-the-badge&logo=appveyor)
![](https://img.shields.io/github/issues/wr0x00/Lsploit?style=for-the-badge&logo=appveyor)
![](https://img.shields.io/github/stars/wr0x00/Lsploit?style=for-the-badge&logo=appveyor)

lsploit为实战而设计的渗透测试框架,配合httpx、asyncio拥有高性能,功能丰富,结合最新漏洞通告,可自行组装exp,poc

### 安装
```shell
git clone https://github.com/wr0x00/Lsploit
cd Lsploit
pip install -r requirement.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple && pip install bs4 -i https://pypi.tuna.tsinghua.edu.cn/simple && pip install prettytable -i https://pypi.tuna.tsinghua.edu.cn/simple
```
### 使用
```shell
python lp.py
或
bash lp.sh
```
### 效果预览
```shell

  ██╗     ███████╗██████╗ ██╗      ██████╗ ██╗████████╗
  ██║     ██╔════╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝
  ██║     ███████╗██████╔╝██║     ██║   ██║██║   ██║   
  ██║     ╚════██║██╔═══╝ ██║     ██║   ██║██║   ██║   
  ███████╗███████║██║     ███████╗╚██████╔╝██║   ██║   
  ╚══════╝╚══════╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝                                                                                                
                                                                                                                            

+-----------------------------------------------+----------------------+------------------------------------------------------------------------+
|                    最新漏洞                   |         时间         |                                  详情                                  |
+-----------------------------------------------+----------------------+------------------------------------------------------------------------+
| CVE-2023-22374：F5 BIG-IP任意代码执行漏洞通告 | 2023-02-06 07:17:33  | https://cert.360.cn/warning/detail?id=7b69c6dd67f6cf3315be9a93bcc9b183 |
|           安全事件周报 (01.30-02.05)          | 2023-02-06 06:56:22  | https://cert.360.cn/warning/detail?id=0421de226241da8d7d532f20f77c27ad |
+-----------------------------------------------+----------------------+------------------------------------------------------------------------+
                                ----数据来源:https://lyy289065406.github.io/threat-broadcast
(使用setnows设置播报漏洞条数,例如“setnows 2”)                   CURL+c 退出
当前 IP：**.**.**.**  来自于：***

Lsploit>help

常用：
        sw 网址或IP地址 线程数 字典路径      扫描网址目录（线程默认60,字典默认\modules\dict.t
        sp IP地址  最大端口               扫描端口（最大端口默认65535）,支持D段‘/’批量扫描
        sd 网址 字典路径             扫描子域名(字典默认modules\subdomain.txt)
        whois 网址                  whois查询
        shod 字符串                 shodan批量检索IP
        c 网址                      cms检测
        poc 地址 端口                poc检测（端口默认80）

        ssh 地址 用户名 端口 字典路径       ssh爆破(用户默认root,端口默认22,字典路径默认modul
        webshell 网址 密码               连接php一句话木马,虚拟终端
        dos IP地址 端口 线程            dos攻击（线程默认40）
        exp cve编号 目标 端口         exp利用(cve编号的cve后面第一个短横去掉,如cve-2018-9995写成cve2018-9995)

设置：
        setnews 数字                设置播报漏洞数
        setproxy 网址               设置代理
        setlang CN/cn/EN/en         设置语言
        
Lsploit>
```
### 已测试
 * windows 10
 * termux(Android)
 * debain

 >[自带的poc](https://github.com/wr0x00/Lizard/wiki/Supported_poc_CN)
 
 >[自带的exp](https://github.com/wr0x00/Lizard/wiki/Support_EXP_CN)
### 性能测试（2023.1.29在codespaces上）
#### 1.http+协程 扫目录 默认字典: 17.3449s
#### 2.协程扫端口 
```
Lsploit>sp 127.0.0.1
[+]正在启动...
地址:127.0.0.1端口:2000         木马GirlFriend 1.3、Millenium 1.0开放此端口

地址:127.0.0.1端口:2222         木马Prosiak开放此端口

地址:127.0.0.1端口:5990 
地址:127.0.0.1端口:5991 
地址:127.0.0.1端口:16634 
地址:127.0.0.1端口:16635 
地址:127.0.0.1端口:37531 
地址:127.0.0.1端口:40523 
地址:127.0.0.1端口:44240 
地址:127.0.0.1端口:46645 
已生成报告：127.0.0.1_port
扫描完成,总耗时:0:00:03.469478
``` 
比nmap快50倍。
## API
```c
.
├── libs //核心功能
│   ├── arpattack.py //早期计划的arp攻击功能，后因termux不支持scapy，所等待termux官方支持再开发
│   ├── cms.py //cms识别
│   ├── configs.json //用户配置
│   ├── dict.txt //默认字典
│   ├── dosattack.py //dos攻击
│   ├── exp //exp
│   │   ├── C2018_9995_EXP.py
│   │   ├── C2019_16313_EXP.py
│   │   ├── C2022_21907_EXP.py
│   │   └── WLAN_AP_WEA453e_EXP.py
│   ├── __init__.py
│   ├── ports.txt //端口服务对照表
│   ├── pwddic 
│   │   └── password //额外字典，免费送
│   ├── __pycache__ 
│   │   ├── __init__.cpython-310.pyc
│   │   ├── sniff.cpython-310.pyc
│   │   └── strings.cpython-310.pyc
│   ├── sniff.py //嗅探模块
│   ├── ssh.py //ssh爆破模块
│   ├── stars //poc
│   │   ├── CNVD_2021_30167.py
│   │   ├── console.py
│   │   ├── cve_2014_4210.py
│   │   ├── cve_2016_0638.py
│   │   ├── cve_2016_3510.py
│   │   ├── cve_2017_10271.py
│   │   ├── cve_2017_3248.py
│   │   ├── cve_2017_3506.py
│   │   ├── cve_2018_2628.py
│   │   ├── cve_2018_2893.py
│   │   ├── cve_2018_2894.py
│   │   ├── cve_2018_3191.py
│   │   ├── cve_2018_3245.py
│   │   ├── cve_2018_3252.py
│   │   ├── CVE_2019_0708.py
│   │   ├── cve_2019_2618.py
│   │   ├── cve_2019_2725.py
│   │   ├── cve_2019_2729.py
│   │   ├── cve_2019_2888.py
│   │   ├── cve_2019_2890.py
│   │   ├── cve_2020_14750.py
│   │   ├── cve_2020_14882.py
│   │   ├── cve_2020_14883.py
│   │   ├── cve_2020_2551.py
│   │   ├── cve_2020_2555.py
│   │   ├── cve_2020_2883.py
│   │   ├── cve_2021_21907.py
│   │   └── __init__.py
│   ├── strings.py //语言包
│   ├── subdomain.py //子域名
│   ├── subdomain.txt //子域名字典
│   ├── utils
│   │   ├── __init__.py
│   │   ├── logger.py
│   │   ├── process.py
│   │   └── state.py
│   ├── webshell.py //连马
│   ├── web_sniff.py //django下sniff模块
│   └── ws.py
├── LICENSE
├── lp.py //启动程序
├── lp.sh
├── Lsploit //django
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── view.py
│   └── wsgi.py
├── manage.py //django
├── order.py //命令处理（if屎山）
├── __pycache__
│   ├── ls.cpython-39.pyc
│   ├── order.cpython-310.pyc
│   └── order.cpython-39.pyc
├── README.md
├── requirement.txt
└── templates //前端文件
    ├── index.html
    ├── results.html
    └── sw.html
```
详细信息见wiki

### 声明
**用户使用本项目所触犯的一切法律责任与本项目作者无关，使用即接受此声明**

### 结语
本项目若有不足或侵权，欢迎发送issue
  <br>
  <br>
  <br>
  <br>
无须追忆昨暮之夕阳，暂且珍视今晨之朝霞
