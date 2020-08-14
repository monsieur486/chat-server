# -*- coding: utf-8 -*-
from appCore.encodeur.ChatMsg import ChatMsg
from appCore.encodeur.PrivateChatMsg import PrivateChatMsg
from appCore.mainMsg.ChangeInfos import ChangeInfos
from appCore.mainMsg.StatesInfos import StatsInfos
from appCore.network.network import userIsRegistered, messageToClient


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
            else:
                self.connectionNonAccept("duplicate")
        else:
            self.connectionNonAccept("badcnx")

    if code == "userPause":
        if value == "user01":
            self.factory.user01State = 2
        if value == "user02":
            self.factory.user02State = 2
        if value == "user03":
            self.factory.user03State = 2
        if value == "user04":
            self.factory.user04State = 2

        value = ChangeInfos("pause",
                            self.user,
                            self.nickname,
                            StatsInfos(
                                self.factory.user01State,
                                self.factory.user02State,
                                self.factory.user03State,
                                self.factory.user04State)
                            )
        msg = messageToClient('mainAction', value)
        self.sendAllUsersMsg(msg)

    if code == "userDispo":
        if value == "user01":
            self.factory.user01State = 1
        if value == "user02":
            self.factory.user02State = 1
        if value == "user03":
            self.factory.user03State = 1
        if value == "user04":
            self.factory.user04State = 1

        value = ChangeInfos("dispo",
                            self.user,
                            self.nickname,
                            StatsInfos(
                                self.factory.user01State,
                                self.factory.user02State,
                                self.factory.user03State,
                                self.factory.user04State)
                            )
        msg = messageToClient('mainAction', value)
        self.sendAllUsersMsg(msg)

    if code == "sendMsg":
        user = value['user']
        nickname = value['nickname']
        msgToSend = value['msgToSend']

        value = ChatMsg(user, nickname, msgToSend)
        msg = messageToClient('newMessage', value)
        self.sendAllUsersMsg(msg)

    if code == "sendPrivateMsg":
        recipientId = value['recipientId']
        recipientNickname = recipientId
        if recipientId == 'user01':
            recipientNickname = 'Poste 1'
        if recipientId == 'user02':
            recipientNickname = 'Poste 2'
        if recipientId == 'user03':
            recipientNickname = 'Poste 3'
        if recipientId == 'user04':
            recipientNickname = 'Poste 4'
        user = value['user']
        nickname = value['nickname']
        msgToSend = value['msgToSend']

        value = PrivateChatMsg(recipientId, recipientNickname, user, nickname, msgToSend)

        for client in self.factory.onlineClients:
            if client.user == recipientId or client.user == user:
                msg = messageToClient('newPrivateMessage', value)
                self.sendMsg(msg)
