#coding: utf-8

import logging
import logging.handlers
from Singleton import *


class LogMgr:
    # 日志等级
    CRITICAL = logging.CRITICAL
    ERROR = logging.ERROR
    WARNING = logging.WARNING
    INFO = logging.INFO
    DEBUG = logging.DEBUG
    NOTSET = logging.NOTSET


    def __init__(self, logfile, level):
        self.logfile = logfile
        # 实例化handler
        self.handler = logging.handlers.RotatingFileHandler('../log/' + self.logfile + '.log', maxBytes = 1014 * 1024, backupCount = 5)
        self.fmt = "%(asctime)s - %(levelname)s - %(message)s"

        # 实例化formatter
        self.formatter = logging.Formatter(self.fmt)
        # 为logger添加formatter
        self.handler.setFormatter(self.formatter)

        # 获取名字为filename的logger
        self.logger = logging.getLogger(self.logfile)

        # 为logger添加handler
        self.logger.addHandler(self.handler)

        # 设置日志等级
        self.setLevel(level)

    def setLevel(self, level):
        self.logger.setLevel(level)


    def logC(self, msg):
        self.logger.critical(msg)

    def logE(self, msg):
        self.logger.error(msg)

    def logW(self, msg):
        self.logger.warning(msg)

    def logI(self, msg):
        self.logger.info(msg)

    def logD(self, msg):
        self.logger.debug(msg)



