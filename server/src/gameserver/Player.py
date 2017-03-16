#coding: utf-8

import uuid
from MysqlDB import *

class PlayerMgr:
    def __init__(self, gm):
        self.gm = gm
        self.players = {}
        self.mysqlDb = MysqlDB()
        self.mysqlDb.connectServer()


    # 玩家重连, 如果玩家在线，则断开老旧连接，并重新设置user_data，返回True. 否则返回False
    def reconnect(self, uuid, user_data):
        if self.players.has_key(uuid):
            player = self.players[uuid]
            ud = player.getUserData()
            if ud.has_key("uuid"):
                del ud["uuid"]
            self.gm.getServer().getNet().kickout(ud)
            player.setUserData(user_data)
            return True
        else:
            return False


    # 玩家通过uuid登录，如果玩家存在，则登录成功返回True并设置user_data，否则返回False
    def login(self, uuid, user_data):
        player = self.getPlayer(uuid)
        if player is None:
            return False
        else:
            player.setUserData(user_data)
            return True

    # 如果玩家在内存中，直接返回玩家实体，否则从数据库中查找并加载到内存中。当数据中也无此玩家时则，返回None
    def getPlayer(self, uuid):
        if self.players.has_key(uuid):
            return self.players[uuid]
        else:
            playerInfo = self.mysqlDb.getPlayerInfo(uuid)
            if playerInfo is not None:
                player = Player()
                player.setUuid(playerInfo.uuid)
                player.setName(playerInfo.name)
                self.players[player.getUuid()] = player 
                return player
            else:
                return None

    # 获取在线玩家
    def getOnlinePlayer(self, uuid):
        if self.players.has_key(uuid):
            return self.players[uuid]
        else:
            return None
    

    # 将玩家添加到在线玩家列表中
    def addPlayer(self, player):
        self.players[player.getUuid()] = player


    # 创建一个新玩家，并将新玩家数据插入到数据库
    def createPlayer(self, user_data):
        tmpUuid = str(uuid.uuid1())        
        player = Player()
        player.setUuid(tmpUuid)
        player.setName("player")
        player.setUserData(user_data)
        self.addPlayer(player)
        self.mysqlDb.addPlayerInfo(player.getUuid(), player.getName())
        return player

    # 从内存中移除玩家，如何玩家数据修改了，则同步到数据库
    def delPlayer(self, uuid):
        if self.players.contains(uuid):
            if self.players[uuid].isModified() is True:
                player = self.players[uuid]
                self.mysqlDb.updatePlayerInfo(player)
                del self.players[uuid]

    # 销毁函数，目前只是断开数据库连接
    def destory(self):
        self.mysqlDb.destory()
        self.mysqlDb = None
    

# 玩家实体
class Player:
    def __init__(self):
        self._uuid = None		# uuid 全局唯一标识
        self._name = None		# 玩家名字
        self._modified = False		# 是否修改过，修改过则需要同步到数据库中
        self._user_data = None		# user_data 网络相关数据
        self._room = None		# 房间
        self._room_pos = True		# 所处房间位置 True:主场  False:客场


    # 设置房间及所处位置
    def setRoom(self, room, room_pos):
        self._room = room
        self._room_pos = room_pos

    # 返回房间引用
    def getRoom(self):
        return self._room

    # 返回所处房间位置
    def getRoomPos(self):
        return self._room_pos

    # 设置全局唯一标识uuid
    def setUuid(self, uuid):
        self._uuid = uuid


    # 设置名字
    def setName(self, name):
        self._name = name

    # 返回uuid
    def getUuid(self):
        return self._uuid

    # 返回名字
    def getName(self):
        return self._name

    # 设置修改标志位
    def setModified(self, modified):
        self._modified = modified

    # 返回修改标志位
    def isModified(self):
        return self._modified

    # 返回网络相关数据user_data
    def getUserData(self):
        return self._user_data

    # 设置网络相关数据user_data，并将uuid加入到user_data中
    def setUserData(self, user_data):
        self._user_data = user_data
        self._user_data["uuid"] = self.getUuid()


    # 开始游戏
    def startGameWith(self, player):
        noti = Notifaction()
        noti.startGameNoti.peerUuid = player.getUuid()
        noti.startGameNoti.peerName = player.getName()
        noti_str = noti.SerializeToString()
        self.sendMsg(Start_Game_Noti, noti_str)

    # 对手离开游戏
    def peerLeave(self):
        noti = Notifaction()
        noti_str = noti.SerializeToString()
        self.sendMsg(Peer_Leave_Noti, noti_str)


    # 发送消息
    def sendMsg(self, msgId, serializeData):
        data_len = len(serializeData) + 8
        buf = create_string_buffer(8)
        struct.pack_into('!I', buf, 0, msgId)
        struct.pack_into('!I', buf, 4, data_len)
        user_data = self.getUserData()
        if user_data is not None:
            user_data["wbuf"] += (buf.raw + serializeData)
            user_data["epl"].modify(user_data["fd"], EPOLLOUT)

