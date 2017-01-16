from django.apps import AppConfig
import json, os

class KurulKomisyonConfig(AppConfig):
    name = 'kurulkomisyon'

    conf = {}
    
    def ready(self):
        if not os.path.isfile('kurulkomisyon/config.json'):
            KurulKomisyonConfig.save_config()
        
        with open('kurulkomisyon/config.json', 'r') as fp:
            KurulKomisyonConfig.conf = json.load(fp)

    
    @classmethod
    def save_config(cls):
        with open('kurulkomisyon/config.json', 'w') as fp:
            json.dump(cls.conf, fp,  indent=2)

    
    @classmethod
    def get(cls, key):
        return cls.conf.get(key)
        

    @classmethod
    def set(cls, key, value):
        cls.conf[key] = value
        
    
