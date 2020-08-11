# -*- coding: utf-8 -*-


from appCore.network.network import userIsRegistered


def analyseMsg(self, code, value):
    if code == "userDecnx":
        self.transport.loseConnection()

    if code == "userCnx":
        newUser = userIsRegistered(value['user'], value['password'])
        if newUser:
            if not self.authenticated:
                self.connectionAccept(str(value['user']))
