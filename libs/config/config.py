import yaml

class Config(object):
    def __init__(self) -> None:
        super().__init__()

        self.fkeys   = "libs/config/keys.yml"
        self.fothers = "libs/config/others.yml"


        self.fqfa_key   = self.get_config_file(open(self.fkeys))["keys"]["fqfa_key"]
        self.shodan_key = self.get_config_file(open(self.fkeys))["keys"]["shodan_key"]
        
        self.first      =  self.get_config_file(open(self.fothers))["others"]["first"]
        self.news       =  self.get_config_file(open(self.fothers))["others"]["news"]  
        self.language   =  self.get_config_file(open(self.fothers))["others"]["language"]
        self.proxy      =  self.get_config_file(open(self.fothers))["others"]["proxy"]    
    
    @staticmethod
    def get_config_file(content: dict) -> dict:
        return yaml.safe_load(content)
    
    @staticmethod
    def change_config_file(content,file,key,data)->None:
        s = Config().get_config_file(open(content))
        s[file][key] = data
        yaml.safe_dump(s,open(content,'w'))
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