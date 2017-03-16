# coding: utf-8

from socket import *
from select import *
from MsgHandler import *
from ctypes import *
import struct

from message_pb2 import *

from GM import *

# 基础消息处理模块
class BaseModule(Module):
    def procMsg(self, user_data):
        if user_data["msg_id"] == Register_Req:
            self.onRegisterReq(user_data)
        elif user_data["msg_id"] == Login_Req:
            self.onLoginReq(user_data)
        elif user_data["msg_id"] == Reconnect_Req:
            self.onReconnectReq(user_data)
        elif user_data["msg_id"] == Route_Msg:
            self.onRouteMsg(user_data)
        else:
            GM().getLogMgr().logD("No function to response msg.(msgid=" + str(msg_id) + ")")


    # 处理注册消息
    def onRegisterReq(self, user_data):
        GM().getLogMgr().logD("收到注册消息")
        req = Request()
        req.ParseFromString(user_data["msg_data"])
        if req.HasField("registerReq"):
            GM().getLogMgr().logD("onRegisterReq()")
            player = GM().getPlayerMgr().createPlayer(user_data)
            res = Response()
            res.result = True
            res.lastResponse = True
            res.registerRes.uuid = player.getUuid()
            res.registerRes.name = player.getName()
            res_str = res.SerializeToString()
            self.sendMsg(user_data, Register_Res, res_str)

    # 处理登陆消息
    def onLoginReq(self, user_data):
        GM().getLogMgr().logD("收到登陆消息")
        req = Request()
        req.ParseFromString(user_data["msg_data"])
        res = Response()
        if req.HasField("loginReq"):
            if GM().getPlayerMgr().login(req.loginReq.uuid, user_data):
                GM().getLogMgr().logD("登陆成功")
                res.result = True
                res.lastResponse = True
                res_str = res.SerializeToString()
                self.sendMsg(user_data, Login_Res, res_str)
            else:
                GM().getLogMgr().logD("无法登陆")
                res.result = False
                res.lastResponse = True
                res.errorDescribe = "用户不存在"
        else:
            res.result = False
            res.lastResponse = True
            res.errorDescribe = "wrong login message!"

        res_str = res.SerializeToString()
        self.sendMsg(user_data, Login_Res, res_str)

    # 处理重连消息
    def onReconnectReq(self, user_data):
        GM().getLogMgr().logD("收到重新连接消息")
        req = Request()
        req.ParseFromString(user_data["msg_data"])
        res = Response()
        if req.HasField("reconnectReq"):
            if GM().getPlayerMgr().reconnect(req.reconnectReq.uuid, user_data):
                GM().getLogMgr().logD("onReconnectReq()")
                res.result = True
            else:
                res.result = False
                res.errorDescribe = "the player if off line, can't reconnect!"
        else:
            res.result = False
            res.errorDescribe = "wrong reconnect message!"
        res.lastResponse = True
        res_str = res.SerializeToString()
        self.sendMsg(user_data, Reconnect_Res, res_str)


    # 处理转发消息
    def onRouteMsg(self, user_data):
        GM().getLogMgr().logD("收到转发消息")
        player = GM().getPlayerMgr().getOnlinePlayer(user_data["uuid"])
        if player is not None:
            room = player.getRoom()
            if room is not None:
                if player.getRoomPos() is True:
                    peerPlayer = room.getPlayer2()
                else:
                    peerPlayer = room.getPlayer1()
                if peerPlayer is not None:
                    peerPlayer.sendMsg(user_data["msg_id"], user_data["msg_data"])
                else:
                    GM().getLogMgr().logD("对手不存在，无法转发消息")
            else:
                GM().getLogMgr().logD("玩家没有在房间中，无法转发消息")
        else:
            GM().getLogMgr().logD("玩家尚未登录")
            

    # 响应登录请求消息
#    def onLoginRequest(self, user_data):
#        req = Request()
#        req.ParseFromString(user_data["msg_data"])
#        if req.HasField('login'):
#            Log().d('onLoginRequest(' + req.login.username +"," + req.login.password + ")")
#            # TODO
#            res = Response()
#            res.result = True
#            res.last_response = True
#            res.login.token = 1234
#            res_str = res.SerializeToString()
#            Log().d("len(reponse)="+str(len(res_str)))
#            self.sendMsg(user_data, Login_Response, res_str)



    # 响应注册注册消息
#    def onRegisterRequest(self, user_data):
#        req = Request()
#        req.ParseFromString(user_data["msg_data"])
#        if req.HasField('register'):
#            Log().d('onRegisterRequest(' + req.register.username + "," + req.register.password + ")")
#            res = Response()
#            res.result = True
#            res.last_response = True
#            res_str = res.SerializeToString()
#            self.sendMsg(user_data, Register_Response, res_str)
##
#    # 响应Debug命令
#    def onDebugCommand(self, user_data):
#        cmd = Command()
#        cmd.ParseFromString(user_data["msg_data"])
#        if cmd.HasField('debug'):
#            Log().d('onDebugCommand(' + cmd.debug.command + ")")
#            notify = Notification()
#            notify.welcome.text = "Welcome, i received your debug command!"
#
     # 发送串行化后的数据
    def sendMsg(self, user_data, msgId, serializeData):
        data_len = len(serializeData) + 8
        buf = create_string_buffer(8)
        struct.pack_into('!I', buf, 0, msgId)
        struct.pack_into('!I', buf, 4, data_len)
        user_data["wbuf"] += (buf.raw + serializeData)
        user_data["epl"].modify(user_data["fd"], EPOLLOUT)
        
        
