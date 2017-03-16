#coding: utf-8

from Singleton import *
from Room import *
from Player import *
from Log import *
from RedisDB import *
from Timer import *

@singleton
class GM:
    def __init__(self):
        self.playerMgr = PlayerMgr(self)
        self.roomMgr = RoomMgr()
        self.redisDB = RedisDB("127.0.0.1", 6379)
        self.timerMgr = TimerMgr()
        self.logMgr = LogMgr("open_world", LogMgr.DEBUG)
        self.server = None

    def setServer(self, server):
        self.server = server

    def getServer(self):
        return self.server

    def getPlayerMgr(self):
        return self.playerMgr

    def getRoomMgr(self):
        return self.roomMgr


    def getRedisDB(self):
        return self.redisDB

    def getTimerMgr(self):
        return self.timerMgr

    def getLogMgr(self):
        return self.logMgr
        
