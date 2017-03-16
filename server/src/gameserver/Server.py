# coding: utf-8

from os import *
from Net import *
from signal import *

from BaseModule import *

from GM import *


global server


def usr1Handler(signo, frame):
    global server
    GM().getLogMgr().logI("进程关闭")
    server.stop()


class Server:
    def __init__(self, config):

        GM().setServer(self)
        self._host = config["host"]
        self._port = config["port"]
        self._timeout = config["timeout"]

        # 创建消息分发器
        self._msgHandler = MsgHandler()

        # 向消息分发器注册消息处理模块
        baseModule = BaseModule(0x00010000)
        self._msgHandler.registerModule(baseModule)

        # 初始化网络并监听
        self._net = Net(self._host, self._port, self._timeout, self._msgHandler)

    def run(self):
        self._net.run()

    def stop(self):
        self._net.stop()

    def getNet(self):
        return self._net


if __name__ == "__main__":
    global server
    pidfile = "../proc/pid"
    if path.exists(pidfile):
        GM().getLogMgr().logE("pid文件已经存在，请检查程序是否已经运行")
    else:
        f = file(pidfile, "w")
        f.write(str(getpid()))
        f.close()


        config = {}
        config["host"] = "115.29.53.18"
        config["port"] = 8888
        config["timeout"] = 10
        server = Server(config)
        signal(SIGUSR1, usr1Handler)

        server.run()

        if path.exists(pidfile):
            GM().getLogMgr().logD("程序正常退出，移除pid文件")
            remove(pidfile)



