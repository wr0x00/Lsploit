'''
 *@author: wr
 *@GitHub:https://github.com/wr0x00/Lsploit
 *@date: 2024.5
 *@description: 提取配置文件信息
'''

import yaml

class Config(object):
    def __init__(self) -> None:
        super().__init__()

        self.fkeys   = self.get_config_file(open("libs/config/paths.yml"))["paths"]["fkeys"]
        self.fothers   = self.get_config_file(open("libs/config/paths.yml"))["paths"]["fothers"]

        self.fqfa_key   = self.get_config_file(open(self.fkeys))["keys"]["fqfa_key"]
        self.shodan_key = self.get_config_file(open(self.fkeys))["keys"]["shodan_key"]
        
        self.first      =  self.get_config_file(open(self.fothers))["others"]["first"]
        self.news       =  self.get_config_file(open(self.fothers))["others"]["news"]  
        self.language   =  self.get_config_file(open(self.fothers))["others"]["language"]
        self.proxy      =  self.get_config_file(open(self.fothers))["others"]["proxy"]    
        self.status     =  self.get_config_file(open(self.fothers))["others"]["status"]
        self.threat_web =  self.get_config_file(open(self.fothers))["others"]["threat_web"]    

        self.exp_path   = self.get_config_file(open("libs/config/paths.yml"))["paths"]["exp_path"]
        self.poc_path   = self.get_config_file(open("libs/config/paths.yml"))["paths"]["poc_path"]
        
    @staticmethod
    def get_config_file(content: dict) -> dict:
        return yaml.safe_load(content)
    
    @staticmethod
    def change_config_file(file,key1,key2,data)->None:
        s = Config().get_config_file(open(file))
        s[key1][key2] = data
        yaml.safe_dump(s,open(file,'w'))
'''
a=Config()
#print(a.get_config_file(open("libs/config/others.yml"))["others"]["first"])
print(a.fqfa_key)
print(a.shodan_key)

print(a.language)
print(a.proxy)
print(a.first)
print(a.news)
print(type(a.language))
print(type(a.proxy))
print(type(a.first))
print(type(a.news))
Config().change_config_file(content=a.fothers,file="others",key="news",data=10)
'''
a=Config()
#print(a.get_config_file(open("libs/config/others.yml"))["others"]["first"])
print(a.exp_path)