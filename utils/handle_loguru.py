# -*- coding: utf-8 -*-
# @File    : handle_loguru.py
# @Time    : 11月 22, 2022
# @Author  : Martin.deng
# @E-mail  : 1637754392@qq.com
# @Software: PyCharm
from configparser import ConfigParser
from loguru import logger
from utils.handle_path import log_path, config_path
from time import strftime
import os
import logging


class PropogateHandler(logging.Handler):
    def emit(self, record):
        logging.getLogger(record.name).handle(record)


class MyLog():
    __instance = None
    __call_flag = True

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
            return cls.__instance

    def get_log(self):
        if self.__call_flag:
            __curdate=strftime('%Y%m%d-%H%M%S')
            cfg = ConfigParser()
            cfg.read(os.path.join(config_path, 'loguru.ini'), encoding='utf-8')
            logger.remove(handler_id=None)
            logger.add(os.path.join(log_path, 'waimai_')+__curdate+'.log', encoding='utf-8',
                       retention=cfg.get('log', 'retention'),
                       rotation=cfg.get('log', 'rotation'),
                       format=cfg.get('log', 'format'),
                       compression=cfg.get('log', 'compression'),
                       level=cfg.get('log', 'level'))
            logger.add(PropogateHandler())
            self.__call_flag = False
        return logger


log = MyLog().get_log()
if __name__ == '__main__':
    log.error('testing11')



