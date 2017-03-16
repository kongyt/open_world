#coding: utf-8


# 房间管理类
class RoomMgr:
    def __init__(self):
        self._max_id = 0
        self._rooms = {}


    # 开房间
    def createRoom(self, player1, player2):
        self._max_id += 1
        room = Room(self._max_id, player1, player2)
        self._rooms[self._max_id] = room
        return room
        

    # 关闭房间
    def closeRoom(self, room):
        if self._rooms.has_key(room.getRoomId()):
            del self._rooms[room.getRoomId()]



#房间类，只负责玩家匹配成功后开始游戏，以及消息转发，不做输赢判定
class Room:
    def __init__(self, roomId, player1, player2):
        self._roomId = roomId
        self._player1 = player1
        self._player2 = player2
        self._player1.setRoom(self, True) # player1 在主场，开始游戏
        self._player2.setRoom(self, False) # player2 在客场, 开始游戏
        self._isEnd = False
        
    def getRoomId(self):
        return self._roomId


    def getPlayer1(self):
        return self._player1

    def getPlayer2(self):
        return self._player2

    # 开始游戏
    def startGame(self):
        self._player1.startGameWith(self._player2)
        self._player2.startGameWith(self._player1) 


    # 玩家断线或中途离开,通知对手,然后结束游戏
    def leave(self, player):
        if player.getRoomPos() is True:
            self._player2.peerLeave()
        elif player.getRoomPos() is False:
            self._player1.peerLeave()
        # 结束游戏
        self.endGame()


    # 游戏结束，此方法负责清理房间
    def endGame(self):
        if self._isEnd is False:
            self._player1.setRoom(None, True)
            self._player2.setRoom(None, True)
            self._player1 = None
            self._player2 = None


        
