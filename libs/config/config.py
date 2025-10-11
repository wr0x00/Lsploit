'''
@author: wr
@GitHub:https://github.com/wr0x00/Lsploit
@date: 2024.5
@description: 提取配置文件信息
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml


class Config(object):
    def __init__(self) -> None:
        super().__init__()

        # Open config files explicitly with UTF-8 to avoid Windows default (gbk/cp936) decoding errors
        paths_file = "libs/config/paths.yml"
        with open(paths_file, encoding="utf-8") as f:
            paths = self.get_config_file(f) or {}

        self.fkeys = paths.get("paths", {}).get("fkeys")
        self.fothers = paths.get("paths", {}).get("fothers")

        # load keys file
        if self.fkeys:
            with open(self.fkeys, encoding="utf-8") as f:
                keys_cfg = self.get_config_file(f) or {}
        else:
            keys_cfg = {}
        keys = keys_cfg.get("keys", {})
        self.fqfa_key = keys.get("fqfa_key")
        self.shodan_key = keys.get("shodan_key")
        self.coze_taken = keys.get("coze_taken")
        self.bot_id = keys.get("bot_id")

        # load others file
        if self.fothers:
            with open(self.fothers, encoding="utf-8") as f:
                others_cfg = self.get_config_file(f) or {}
        else:
            others_cfg = {}
        others = others_cfg.get("others", {})
        self.first = others.get("first")
        self.news = others.get("news")
        self.language = others.get("language")
        self.proxy = others.get("proxy")
        self.status = others.get("status")
        self.threat_web = others.get("threat_web")

        self.exp_path = paths.get("paths", {}).get("exp_path")
        self.poc_path = paths.get("paths", {}).get("poc_path")

    @staticmethod
    def get_config_file(content) -> dict:
        """Load YAML from a file-like object or string and return a dict."""
        return yaml.safe_load(content)

    @staticmethod
    def change_config_file(file, key1, key2, data) -> None:
        """Read a YAML file, change a nested key and write it back using UTF-8.

        file: path to YAML file
        key1: top-level key (e.g. 'others')
        key2: nested key under key1 (e.g. 'news')
        data: new value
        """
        with open(file, 'r', encoding='utf-8') as f:
            s = yaml.safe_load(f) or {}

        if key1 not in s or not isinstance(s[key1], dict):
            s[key1] = {}
        s[key1][key2] = data

        with open(file, 'w', encoding='utf-8') as f:
            yaml.safe_dump(s, f, allow_unicode=True)


if __name__ == '__main__':
    # quick smoke test when run directly
    cfg = Config()
    print(cfg.exp_path)