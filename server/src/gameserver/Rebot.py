#coding: utf-8

from message_pb2 import *
from socket import *
from sys import argv
import time

class RebotModule(Module):
    def procMsg(self, msg):
        if msg["msg_id"] == Match_Player_Res:
            pass
        else:
            pass


class Rebot:
    def __init__(self):
        self.runFlag = True
        self.sock = None
        self.wbuf = ""
        self.rbuf = ""
        self.msgHandler = MsgHandler()
        self.msgHandler.registerModule()

    # 连接服务器
    def conn(self,ip, port):
        self.sock = socket(AF_INET, SOCK_STREAM, 0)
        self.sock.connect((ip, port))


    # 断开与服务器的连接
    def disconn(self):
        if self.sock is not None:
            self.sock.close()
            self.sock = None

    # 发送消息包
    def sendMsg(self, user_data, msgId, serializeData):
        data_len = len(serializeData) + 8
        buf = create_string_buffer(8)
        struct.pack_into('!I', buf, 0, msgId)
        struct.pack_into('!I', buf, 4, data_len)
        self.wbuf += (buf.raw + serializeData)
        self.sock.send(self.wbuf)
        self.wbuf = ""
        print "发送消息包给服务器，消息ID=",msgId


    # 接收并分发消息包
    def recvMsg(self):
        try:
            data = self.sock.recv(1024)
            if data:
                self.rbuf += data
                bufdata = self.rbuf
                while len(bufdata) >= 8:
                    msg_id = struct.unpack('!I', bufdata[0:4])[0]
                    data_len = struct.unpack('!I', bufdata[4:8])[0]
                    if len(bufdata) >= data_len:
                        packet_data = bufdata[8:data_len]
                        self.rbuf = bufdata[data_len:]
                        bufdata = self.rbuf
                        msg = {}
                        msg["msg_id"] = msgId
                        msg["msg_data"] = packet_data
                        self._msgHandler.handleMsg(msg)
                    else:
                        break
            else:
                self.disconn()
        except socket.error, arg:
            pass



    def run(self):
        pass



if __name__ == "__main__":
    print sys.argv[1]
    rebotNum = int(argv[1])
    rebots = []
    for i in range(rebotNum):
        print "启动机器人",i
        rebot = Rebot()
        rebots.append(rebot)
        rebot.conn("115.29.53.18", 8888)
        rebot.run()

    for rebot in rebots:
        rebot.disconn()


