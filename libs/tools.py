import os
from .config.config import Config

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
            
# 遍历文件夹
def traversal_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        # 遍历当前文件夹下的所有文件
        for file_name in files:
            file_path = os.path.join(root, file_name)
            print(file_path)
    return files
class search(object):
    
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def expand_exp()->dict:
        Config.change_config_file(Config().fothers,"others","status","exp")
        outcome=[]
        for root, dirs, files in os.walk(Config().exp_path):
            i=1
            for file_name in files:
                print(os.path.join(f"[{i}]",file_name))
                outcome.append([i,file_name.strip('/')])
                i+=1
        return outcome
    
    def expand_poc()->dict:
        Config.change_config_file(Config().fothers,"others","status","poc")
        outcome=[]
        for root, dirs, files in os.walk(Config().poc_path):
            i=1
            for file_name in files:
                print(os.path.join(f"[{i}]",file_name))
                outcome.append([i,file_name])
                i+=1
        return outcome
    
    def detail(n): #打印poc/exp详细信息

        import sys
        sys.dont_write_bytecode = True# 设置不生成 .pyc 文件

        number=n-1
        if Config().status == "exp":
            exec("import sys")
            exec("sys.dont_write_bytecode = True")# 设置不生成 .pyc 文件

            exec(f"from {(((Config().exp_path+search.expand_exp()[number][1])).replace('/','.')).strip('.py')} import {search.expand_exp()[number][1].strip('.py')}")
            exec(f"print({search.expand_exp()[number][1].strip('.py')}().details)")
            exec(f"print({search.expand_exp()[number][1].strip('.py')}().argumens)")

        if Config().status == "poc":
            exec("import sys")
            exec("sys.dont_write_bytecode = True")# 设置不生成 .pyc 文件

            exec(f"from {(((Config().poc_path+search.expand_poc()[number][1])).replace('/','.')).strip('.py')} import {search.expand_poc()[number][1].strip('.py')}")
            exec(f"print({search.expand_poc()[number][1].strip('.py')}().details)")

#search.expand_exp()
#search.detail(1)
#print(f"from {(((Config().exp_path+search.expand_exp()[0][1]).strip('libs/')).replace('/','.')).strip('.py')} import {search.expand_exp()[0][1].strip('.py')}")

'''
from exp.cve_2018_9995 import cve_2018_9995
print(cve_2018_9995().details)
print(cve_2018_9995().argumens)
'''