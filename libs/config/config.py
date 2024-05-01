
class Config(object):
    def __init__(self) -> None:
        super().__init__()

        import yaml
        with open("libs/config/keys.yml", encoding='utf-8') as fkeys:
            self.fqfa_key = yaml.load(fkeys.read(), Loader=yaml.FullLoader)["keys"]["fqfa_key"]
            self.shodan_key = yaml.load(fkeys.read(), Loader=yaml.FullLoader)["keys"]["shodan_key"]
            