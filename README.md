# Lsploit
![](https://socialify.git.ci/wr0x00/Lsploit/image?description=1&descriptionEditable=A%20network%20penetration%20testing%20framework%20born%20for%20real-world%20situations.%E4%B8%BA%E5%AE%9E%E6%88%98%E8%80%8C%E7%94%9F%E7%9A%84%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E6%A1%86%E6%9E%B6%E3%80%82&font=Rokkitt&forks=1&issues=1&logo=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F86941613%3Fs%3D96%26v%3D4&name=1&owner=1&pattern=Circuit%20Board&pulls=1&stargazers=1&theme=Light) 
![](https://img.shields.io/badge/Size-4MB-informational?style=for-the-badge&logo=appveyor)
![](https://img.shields.io/badge/tested-termux-green?style=for-the-badge&logo=appveyor)

lsploit为实战而设计的渗透测试框架,配合httpx、asyncio拥有高性能,功能丰富,结合最新漏洞通告,可自行组装exp,poc

### 安装
```shell
git clone https://github.com/wr0x00/Lsploit

cd Lsploit

pip install -r requirement.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple && pip install bs4 -i https://pypi.tuna.tsinghua.edu.cn/simple && pip install prettytable -i https://pypi.tuna.tsinghua.edu.cn/simple && pip install httpx[http2] -i https://pypi.tuna.tsinghua.edu.cn/simple

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
        fqfa 字符串 数量            fqfa批量索引ip(数量默认100,在libs/config/keys.yml输入你的fqfa_key)
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
注意命令中间是用空格区分。
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

详细信息见[wiki](https://github.com/wr0x00/Lsploit/wiki)

### 声明
**用户使用本项目所触犯的一切法律责任与本项目作者无关，使用即接受此声明**

### 结语
本项目若有不足或侵权，欢迎发送issue
  <br>
  <br>
  <br>
  <br>
无须追忆昨暮之夕阳，暂且珍视今晨之朝霞
