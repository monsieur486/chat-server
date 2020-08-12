# -*- coding: utf-8 -*-


from appCore.network.network import userIsRegistered


def analyseMsg(self, code, value):
    if code == "userDecnx":
        self.transport.loseConnection()

    if code == "userCnx":
        newUser = userIsRegistered(value['user'], value['password'])
        if newUser:
            flag = True
            for client in self.factory.onlineClients:
                if client.user == newUser:
                    flag = False

            if not self.authenticated and flag:
                self.connectionAccept(str(value['user']))
            else:
                self.connectionNonAccept("duplicate")
        else:
            self.connectionNonAccept("badcnx")
