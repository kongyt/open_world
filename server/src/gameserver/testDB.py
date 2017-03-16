#coding: utf-8

from MysqlDB import *



if __name__ == "__main__":
    db = MysqlDB()
    db.connectServer()
    db.addPlayerInfo("abcd", "kongyt")
    db.updatePlayerInfo("abcd", "haha")
    print db.getPlayerInfo("abcd")
    db.destory()
