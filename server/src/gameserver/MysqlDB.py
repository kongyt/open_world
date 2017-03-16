#coding: utf-8

import MySQLdb



class MysqlDB:
    def __init__(self):
        self._host = '115.29.53.18'
        self._port = 3306
        self._user = 'duel'
        self._pwd = 'duel4kyt?'
        self._db = 'duel'

        self._conn = None

    def connectServer(self):
        self._conn = MySQLdb.connect(host = self._host, port = self._port, user = self._user, passwd = self._pwd, db = self._db)


    def getPlayerInfo(self, uuid):
        rs = None
        cur = self._conn.cursor()
        if cur.execute("select uuid, name from user_info where uuid = \"%s\"" % (uuid)) == 1:
            rs =  cur.fetchone()
        cur.close()
        return rs

    def addPlayerInfo(self, uuid, name):
        cur = self._conn.cursor()
        sqli = "insert into user_info (uuid, name) values(%s, %s)"
        cur.execute(sqli, (uuid, name))
        cur.close()
        self._conn.commit()

    def updatePlayerInfo(self, uuid, name):
        cur = self._conn.cursor()
        cur.execute("update user_info set name= \"%s\" where uuid=\"%s\"" %(name, uuid))
        cur.close()
        self._conn.commit()



    def disconnectServer(self):
        self._conn.close()

    def destory(self):
        if self._conn is not None:
            self.disconnectServer()
            self._conn = None



