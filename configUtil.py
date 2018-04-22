# -*- coding: UTF-8 -*-
from configobj import ConfigObj


class ConfigUtil:

    def __init__(self):
        conf_ini = "./test.ini"
        self = ConfigObj('epdconfig.ini', encoding='UTF8')
        pass

    def getConfigString(self, key, section='path'):
        return self[section][key]
