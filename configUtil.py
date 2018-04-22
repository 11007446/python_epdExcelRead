# -*- coding: UTF-8 -*-
from configobj import ConfigObj


class ConfigUtil:

    def __init__(self):
        conf_ini = "./test.ini"
        self.__config = ConfigObj('epdconfig.ini', encoding='UTF8')
        pass

    def getConfigString(self, section, key):
        return self.__config[section][key]
