# -*- coding: utf-8 -*-


from appCore.encodeur.ChatMsg import ChatMsg
from appCore.network.network import userIsRegistered, MessageToClient


def analyseMsg(self, code, value):
    if code == "userQuit":
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

    if code == "sendMsg":
        userID = value['userID']
        nickname = value['nickname']
        msgToSend = value['msgToSend']

        value = ChatMsg(userID, nickname, msgToSend)
        msg = MessageToClient('newMessage', value)
        self.sendAllUsersMsg(msg)

    if code == "pingAll":
        msg = MessageToClient('ping', True)
        self.sendAllUsersMsg(msg)

    if code == "pingUser":
        userID = value
        msg = MessageToClient('ping', True)
        self.sendUserIdMsg(userID, msg)

