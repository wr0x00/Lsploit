'''
 *@author: wr
 *@GitHub:https://github.com/wr0x00/Lsploit
 *@date: 2022.8.21
 *@description: 程序所需显示的所有字符串
'''

#CN 
from sre_constants import SUCCESS


class MessageSign:
    EXC = '[!]'
    STR = '[*]'
    PLS = '[+]'
    MIN = '[-]'

class String_CN:
    HELP="""
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
        exp cve编号 目标 端口         exp利用(cve编号的cve后面第一个短横去掉,如cve-2018-9995

设置：
        setnews 数字                设置播报漏洞数
        setproxy 网址               设置代理
        setlang CN/cn/EN/en         设置语言
        """
    
    WARNING="该项目仅用于学习交流目地，使用者所触犯的一切法律责任与本项目作者无关\n一切未经允许的测试行动皆属于违法行为，请保持清醒，自行斟酌\n"
    
    LOCALNAME="本机名称:"
    LOCALHOST_LAN="本机局域网地址:"
    LOCALHOST_WAN="本机广域网地址:"
    LOADING="正在启动..."
    RESULTS="结果:"
    RESULTS_TOTAL="共找到:"
    DICT_TOTAL="字典总计:"
    TIME_TOTAL="总耗时:"
    THREAD_TOTAL="线程总计:"
    STOPING="正在停止..."
    EXIT="Bye"
    TARGET="目标:"
    USER = "账户"
    PWD = "密码"
    PORT = "端口"
    ADDR = "地址"
    FOUND="发现"
    THREAD_EXIT="请等待所有线程退出"
    NOW_TRYING="正在尝试:"
    TIMES_send="次发送到"
    BYTE="字节"
    REMAINING_TIMES="今日剩余次数"

    ERROR_IP_FORMAT="IP地址格式不正确"
    ERROR_CONNECT="无法连接 :("
    ERROT_DICT="字典为空 :("
    ERROR_ORDER="命令错误"

    SUCCESS_SCAN="扫描完成"
    SUCCESS_SSH="ssh爆破成功"
    SUCCESS_SET="设置成功"

class String_EN:
    HELP="""
常用：
        sw 网址或IP地址 线程数 字典路径      扫描网址目录（线程默认60,字典默认\modul
        sp IP地址 最大端口             扫描端口
        sd 网址 字典路径             扫描子域名(字典默认modules\subdomain.txt)
        whois 网址                  whois查询
        shod 字符串                 shodan批量检索IP
        c 网址                      cms检测
        poc 地址 端口                poc检测（端口默认80）

        ssh 地址 用户名 端口 字典路径       ssh爆破(用户默认root,端口默认22,字典路径
        webshell 网址 密码               连接php一句话木马,虚拟终端
        dos IP地址 端口 线程            dos攻击（线程默认40）
        exp cve编号 目标 端口         exp利用(cve编号的cve后面第一个短横去掉,如cve-2

设置：
        setnews 数字                设置播报漏洞多少数
        setproxy 网址               设置代理
        """

    WARNING="The project is only used for the purpose of learning and communication, the legal responsibility of the user has nothing to do with the author of the project, and all unauthorized test actions are illegal, please stay sober and consider it yourself.\n"
    
    LOCALNAME="local name:"
    LOCALHOST_LAN="your LAN:"
    LOCALHOST_WAN="your WAN:"
    LOADING="starting..."
    RESULTS="results:"
    RESULTS_TOTAL="Results found:"
    DICT_TOTAL="add dictionary's lines up:"
    TIME_TOTAL="total time:"
    THREAD_TOTAL="add threads up:"
    STOPING="stoping..."
    EXIT="Bye"
    TARGET="target:"
    USER="user"
    PWD="password"
    PORT="port"
    ADDR="address"
    FOUND="found"
    THREAD_EXIT="please wait for all threads exited"
    NOW_TRYING="now is trying:"
    TIMES_send="times send to"
    BYTE="bytes"
    REMAINING_TIMES="The number of times remaining today"

    ERROR_IP_FORMAT="IP address format is wrong"
    ERROR_CONNECT="connect error :("
    ERROT_DICT="dictionary is none :("
    ERROR_ORDER="order error"

    SUCCESS_SCAN="scanning over"
    SUCCESS_SSH="ssh brute force crack successful"
    SUCCESS_SET="setted successful"