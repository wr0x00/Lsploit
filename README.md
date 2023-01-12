# Lsploit

![](https://img.shields.io/badge/Size-4MB-informational?style=for-the-badge&logo=appveyor)
![](https://img.shields.io/badge/tested-termux-green?style=for-the-badge&logo=appveyor)
![](https://img.shields.io/github/issues/wr0x00/Lsploit?style=for-the-badge&logo=appveyor)
![](https://img.shields.io/github/stars/wr0x00/Lsploit?style=for-the-badge&logo=appveyor)

lsploit为一款命令行下的渗透测试框架,快速命令平台,涵盖常用功能,结合最新漏洞通告,可自行组装exp,poc

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
```js
__       ____     ____     __       _____    ______  ______   
 /\ \     /\  _`\  /\  _`\  /\ \     /\  __`\ /\__  _\/\__  _\  
 \ \ \    \ \,\L\_\ \ \L\ \ \ \    \ \ \/\ \/_/\ \/\/_/\ \/  
  \ \ \  __\/_\__ \ \ \ ,__/ \ \ \  __\ \ \ \ \  \ \ \   \ \ \  
   \ \ \L\ \ /\ \L\ \ \ \/   \ \ \L\ \ \ \_\ \  \_\ \__ \ \ \ 
    \ \____/ \ `\____\ \_\    \ \____/ \ \_____\ /\_____\ \ \_、
     \/___/   \/_____/ \/_/     \/___/   \/_____/ \/_____/  \/_/

+--------------------------------------------+---------------------+------------------------------------------------------------------------+
|                  最新漏洞                  |         时间        |                                  详情                                  |
+--------------------------------------------+---------------------+------------------------------------------------------------------------+
| CVE-2022-3236：Sophos Firewall代码注入漏洞 | 2022-09-27 06:54:41 | https://cert.360.cn/warning/detail?id=7dd2729178b6e52796bd57708b3266ed |
|         安全事件周报 (09.19-09.25)         | 2022-09-26 09:02:22 | https://cert.360.cn/warning/detail?id=105231120c8d712dd9c394d27128c4a6 |
+--------------------------------------------+---------------------+------------------------------------------------------------------------+
                                ----数据来源:https://lyy289065406.github.io/threat-broadcast
(使用setnows设置播报漏洞条数,例如“setnows 2”)                   CURL+c 退出
当前 IP：***.***.***.***  来自于：** ** ** **

Lsploit>help

常用：
        sw 网址或IP地址 线程数 字典路径      扫描网址目录（线程默认60,字典默认\modules\dict.t
        sp IP地址  最大端口               扫描端口（最大端口默认65535）
        sd 网址 字典路径             扫描子域名(字典默认modules\subdomain.txt)
        whois 网址                  whois查询
        shod 字符串                 shodan批量检索IP
        c 网址                      cms检测
        poc 地址 端口                poc检测（端口默认80）

        ssh 地址 用户名 端口 字典路径       ssh爆破(用户默认root,端口默认22,字典路径默认modul
        webshell 网址 密码               连接php一句话木马,虚拟终端
        dos IP地址 端口 线程            dos攻击（线程默认40）
        exp cve编号 目标 端口         exp利用(cve编号的cve后面第一个短横去掉,如cve2018-9995

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
### 声明
**用户使用本项目所触犯的一切法律责任与本项目作者无关，使用即接受此声明**

### 结语
本项目若有不足或侵权，欢迎发送issue
  <br>
  <br>
  <br>
  <br>
无须追忆昨暮之夕阳，暂且珍视今晨之朝霞
