#coding: utf-8

from redis import *

class RedisDB:
    def __init__(self, ip, p):
        self._rcon = StrictRedis(host=ip, port = p, db=0)

    # 一些数据存储方法
    def setUser(self, userId, User):
        pass


    def getUser(self, userId):
        pass



    def pb2str(self, pbData):
        pass


        
