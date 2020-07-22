# -*- coding: utf-8 -*-


from appCore.game.createGame import createGame
from appCore.game.gamePlayerLogout import gamePlayerLogout
from appCore.game.privateGameCnx import privateGameCnx
from appCore.game.startGame import startGame
from appCore.network.network import userIsRegistered


def analyseMsg(self, code, value):
    if code == "userDecnx":
        self.transport.loseConnection()

    if code == "userCnx":
        newUser = userIsRegistered(value['user'], value['password'])
        if newUser:
            if not self.authenticated:
                self.connectionAccept(str(value['user']))

    if code == "createGame":
        createGame(self, value)

    if code == "privateGameCnx":
        privateGameCnx(self, value)

    if code == "playerLogout":
        gamePlayerLogout(self, value)

    if code == "startGame":
        startGame(self, value)


