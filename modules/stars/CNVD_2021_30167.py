
#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# CVE-2019-2618
# 用友beanshell漏洞
# updated 2022/7/26
# by wr0x00

from stars import target_type, Star
from utils import http
from multiprocessing.managers import SyncManager
from typing import Any, Dict, List, Mapping, Tuple, Union
# @universe.groups()
class CNVD_2021_30167(Star):
    info = {
    'NAME': '',
    'CVE': 'CNVD_2021_30167',
    'TAG': []
    }
    type = target_type.MODULE
    def light_up(self, dip, dport, force_ssl=None, *args, **kwargs) -> (bool, dict):
        import requests
        
        url=dip
        host_uri = "/servlet/~ic/bsh.servlet.BshServlet"
        hostall = url + host_uri
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        r = requests.post(hostall,headers=header,timeout=5)
        r_text = r.text
        if r.status_code==200 and 'BeanShell Test Servlet' in r_text:
            return True, {'msg': 'finish.'}
        else:
            return False, {'msg': 'finish.'}


def run(queue: SyncManager.Queue, data: Dict):
    obj = CNVD_2021_30167()
    result = {
        'IP': data['IP'],
        'PORT': data['PORT'],
        'NAME': obj.info['CVE'] if obj.info['CVE'] else obj.info['NAME'],
        'MSG': '',
        'STATE': False
    }
    result['STATE'], result['MSG'] = obj.light_and_msg(
        data['IP'], data['PORT'], data['IS_SSL'])

    queue.put(result)