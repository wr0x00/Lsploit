'''
 *@author: wr
 *@GitHub:https://github.com/wr0x00/Lsploit
 *@date: 2022.8.21
 *@description: 命令行程序所需显示的所有字符串
'''

#CN 
class MessageSign:
    EXC = '\033[91m'    +'[!]'+  '\033[1;37;40m'      #错误
    MIN = '\033[4;33m'  +'[-]'+  '\033[0m'            #警告
    STR = '\033[37;42m' +'[*]'+  '\033[0m'            #重要价值信息
    PLS = '\033[32m'    +'[+]'+  '\033[1;37;40m'      #常规执行信息

class String_CN:
    HELP="""
（以空格区分参数）
常用：  upgrade                                从GitHub更新本仓库
        ai                                      开启ai对话框
        i (数字)                                查看本设备详细信息（IP，名称，配置等）
            1：cpu
            2：内存
            3：硬件
            4：磁盘
            5：网络接口
            6：硬件详细信息
            7：PCI 设备信息
            8：USB 设备信息
        sw 网址或IP地址 线程数 字典路径         扫描网址目录（线程默认60,字典默认\modules\dict.t
        sp IP地址  最大端口                     扫描端口（最大端口默认65535）,支持D段‘/’批量扫描
        sd 网址 字典路径                        扫描子域名(字典默认modules\subdomain.txt)
        whois 网址                              whois查询
        shod 字符串                             shodan批量检索IP
        fqfa 字符串 数量                        fqfa批量索引ip(数量默认100)
        c 网址                                  cms检测
        poc 地址 端口                           poc检测（端口默认80）

攻击：  show exps/exp/pocs/poc                 列出本地可用poc/exp的一个列表
        chose 数字                             选择/使用以上列表的选项对应的项目
        survey 数字                            查看选项详细信息
        ssh 地址 用户名 端口 字典路径           ssh爆破(用户默认root,端口默认22,字典路径默认modul
        webshell 网址 密码                      连接php一句话木马,虚拟终端
        dos IP地址 端口 线程                    dos攻击（线程默认40）
        exp cve编号 目标 端口                   exp利用(cve编号的cve后面第一个短横去掉,如cve-2018-9995写成cve2018-9995)

设置：  setnews 数字                            设置播报漏洞数
        setproxy 网址                           设置代理
        setlang CN/cn/EN/en                     设置语言
        setcozeid                               设置ai产品扣子api
        setbotid                                设置扣子智能体id
        """
#NORMAL  
    WARNING="""该项目仅用于学习交流目地，使用者所触犯的一切法律责任与本项目作者无关\n
                         一切未经允许的测试行动皆属于违法行为，请保持清醒，自行斟酌\n"""
    UPGRADE                 =MessageSign.PLS+"正在从github拉取最新版..."
    INSTALL                 =MessageSign.PLS+"正在安装依赖项..."
    LOCALNAME               ="本机名称:"
    LOCALHOST_LAN           ="本机局域网地址:"
    LOCALHOST_WAN           ="本机广域网地址:"
    LOADING                 =MessageSign.PLS+"正在启动..."
    RESULTS_TOTAL           =MessageSign.PLS+"共计:"
    DICT_TOTAL              =MessageSign.PLS+"字典总计:"
    THREAD_TOTAL            =MessageSign.PLS+"线程总计:"
    STOPING                 =MessageSign.PLS+"正在停止..."
    NOW_TRYING              =MessageSign.PLS+"正在尝试:"
    ONLINE                  =MessageSign.STR+"存活主机"
    RESULTS                 ="结果:"
    TIME_TOTAL              ="总耗时:"
    EXIT                    ="Bye"
    ORDINAL                 ="序号"
    NAME                    ="名称"
    INTOR                   ="简介"    
    TARGET                  ="目标:"
    USER                    ="账户"
    PWD                     ="密码"
    PORT                    ="端口"
    ADDR                    = "地址"
    FOUND                   =MessageSign.STR+"发现"
    THREAD_EXIT             =MessageSign.MIN+"请等待所有线程退出"
    TIMES_send              ="次发送到"
    BYTE                    ="字节"
    REMAINING_TIMES         =MessageSign.MIN+"今日剩余次数"
#ERROR
    ERROR_AI_USERAPI        =MessageSign.EXC+"未设置ai产品用户api"   
    ERROR_AI_BOTID          =MessageSign.EXC+"未设置ai机器人id"
    ERROR_IP_FORMAT         =MessageSign.EXC+"IP地址格式不正确"
    ERROR_CONNECT           =MessageSign.EXC+"无法连接 :("
    ERROT_DICT              =MessageSign.EXC+"字典为空 :("
    ERROR_ORDER             =MessageSign.EXC+"命令错误,输入'help'查看帮助"
    ERROR_OS                =MessageSign.EXC+"未知操作系统"
#SUCCESS
    SUCCESS_SCAN            =MessageSign.PLS+"扫描完成"
    SUCCESS_SSH             =MessageSign.PLS+"ssh爆破成功"
    SUCCESS_SET             =MessageSign.PLS+"设置成功,重启生效"
    SUCCESS_WRITTEN         =MessageSign.PLS+"已生成报告："
#HTML
    TITTEL                  ="LSPLOIT"
    WELCOME                 ="欢迎回到Lsploit!"
    ISSUE                   ="到GitHub报告问题"
    URL                     ="地址："
    DO                      ="执行"
    GO_BACK                 ="返回"

#EN
class String_EN:
    HELP="""
（以空格区分参数）
常用：  upgrade                                从GitHub更新本仓库
        sw 网址或IP地址 线程数 字典路径         扫描网址目录（线程默认60,字典默认\modules\dict.t
        sp IP地址  最大端口                     扫描端口（最大端口默认65535）,支持D段‘/’批量扫描
        sd 网址 字典路径                        扫描子域名(字典默认modules\subdomain.txt)
        whois 网址                              whois查询
        shod 字符串                             shodan批量检索IP
        fqfa 字符串 数量                        fqfa批量索引ip(数量默认100)
        c 网址                                  cms检测
        poc 地址 端口                           poc检测（端口默认80）

攻击：  show exps/exp/pocs/poc                 列出本地可用poc/exp的一个列表
        chose 数字                             选择/使用以上列表的选项对应的项目
        survey 数字                            查看选项详细信息
        ssh 地址 用户名 端口 字典路径           ssh爆破(用户默认root,端口默认22,字典路径默认modul
        webshell 网址 密码                      连接php一句话木马,虚拟终端
        dos IP地址 端口 线程                    dos攻击（线程默认40）
        exp cve编号 目标 端口                   exp利用(cve编号的cve后面第一个短横去掉,如cve-2018-9995写成cve2018-9995)

设置：  setnews 数字                            设置播报漏洞数
        setproxy 网址                           设置代理
        setlang CN/cn/EN/en                     设置语言
        """

    WARNING="""The project is only used for the purpose of learning and communication, the legal responsibility of the user has nothing to do with the author of the project\n
            all unauthorized test actions are illegal, please stay sober and consider it yourself.\n"""
    INSTALL                 =MessageSign.PLS+"installing requirement..."
    LOCALNAME               ="local name:"
    LOCALHOST_LAN           ="your LAN:"
    LOCALHOST_WAN           ="your WAN:"
    LOADING                 ="starting..."
    RESULTS                 ="results:"
    RESULTS_TOTAL           ="Results found:"
    DICT_TOTAL              ="add dictionary's lines up:"
    TIME_TOTAL              ="total time:"
    THREAD_TOTAL            ="add threads up:"
    STOPING                 ="stoping..."
    EXIT                    ="Bye"
    TARGET                  ="target:"
    USER                    ="user"
    PWD                     ="password"
    PORT                    ="port"
    ADDR                    ="address"
    FOUND                   ="found"
    THREAD_EXIT             ="please wait for all threads exited"
    NOW_TRYING              ="now is trying:"
    TIMES_send              ="times send to"
    BYTE                    ="bytes"
    REMAINING_TIMES         ="The number of times remaining today"

    ERROR_IP_FORMAT         =MessageSign.EXC+"IP address format is wrong"
    ERROR_CONNECT           =MessageSign.EXC+"connect error :("
    ERROT_DICT              =MessageSign.EXC+"dictionary is none :("
    ERROR_ORDER             =MessageSign.EXC+"command error"

    SUCCESS_SCAN            ="scanning over"
    SUCCESS_SSH             ="ssh brute force crack successful"
    SUCCESS_SET             ="setted successful,restart takes effect"
