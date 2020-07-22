# -*- coding: utf-8 -*-


from appCore.game.User import User


class Game:
    def __init__(self,
                 gameId,
                 denomination,
                 private,
                 password,
                 maxPlayers,
                 isWithChat,
                 isWithRelance,
                 isWithAnnonce,
                 isWithRound,
                 isWithBelge,
                 isWithPetite,
                 isWithGarde,
                 isWithGardeSans
                 ):
        self.player = None
        self.gameId = gameId
        self.denomination = denomination
        self.private = private
        self.password = password
        self.nbPlayers = 0
        self.maxPlayers = maxPlayers
        self.state = 1
        self.isWithChat = isWithChat
        self.isWithRelance = isWithRelance
        self.isWithAnnonce = isWithAnnonce
        self.isWithRound = isWithRound
        self.isWithBelge = isWithBelge
        self.isWithPetite = isWithPetite
        self.isWithGarde = isWithGarde
        self.isWithGardeSans = isWithGardeSans

        self.user1 = User(None, True)
        self.user2 = User(None, True)
        self.user3 = User(None, True)
        self.user4 = User(None, True)
        if self.maxPlayers == 4:
            self.user5 = User(None, False)
        else:
            self.user5 = User(None, True)

        self.nextAction = 0
        self.donnes = []
        self.donne = 0
        self.turn = 0
        self.dealer = 0
        self.contract = 0
        self.withChelem = False
        self.cardCall = 0
        self.color = 0
        self.atoutMax = 0
        self.cyclePlayers = []
        self.cyclePosition = 0
        self.chien = []
        self.centralCards = []
        self.centralCardsType = 0

    def addPlayer(self, client):
        flag = False

        if self.user1.slot:
            flag = True
            self.user1.userId = client.user
            self.user1.nickname = client.nickname
            self.user1.cnx = client
            self.user1.isOnline = True
            self.user1.slot = False
            self.nbPlayers += 1

        if not flag:
            if self.user2.slot:
                flag = True
                self.user2.userId = client.user
                self.user2.nickname = client.nickname
                self.user2.cnx = client
                self.user2.isOnline = True
                self.user2.slot = False
                self.nbPlayers += 1

        if not flag:
            if self.user3.slot:
                flag = True
                self.user3.userId = client.user
                self.user3.nickname = client.nickname
                self.user3.cnx = client
                self.user3.isOnline = True
                self.user3.slot = False
                self.nbPlayers += 1

        if not flag:
            if self.user4.slot:
                flag = True
                self.user4.userId = client.user
                self.user4.nickname = client.nickname
                self.user4.cnx = client
                self.user4.isOnline = True
                self.user4.slot = False
                self.nbPlayers += 1

        if not flag:
            if self.user5.slot:
                self.user5.userId = client.user
                self.user5.nickname = client.nickname
                self.user5.cnx = client
                self.user5.isOnline = True
                self.user5.slot = False
                self.nbPlayers += 1

    def loosePlayer(self, userId):
        if self.user1.userId == userId:
            self.user1.cnx = None
            self.user1.isOnline = False

        if self.user2.userId == userId:
            self.user2.cnx = None
            self.user2.isOnline = False

        if self.user3.userId == userId:
            self.user3.cnx = None
            self.user3.isOnline = False

        if self.user4.userId == userId:
            self.user4.cnx = None
            self.user4.isOnline = False

        if self.user5.userId == userId:
            self.user5.cnx = None
            self.user5.isOnline = False

    def removePlayer(self, userId):
        if self.user1.userId == userId:
            self.user1.userId = None
            self.user1.nickname = '--'
            self.user1.cnx = None
            self.user1.isOnline = False
            self.user1.slot = True
            self.nbPlayers -= 1

        if self.user2.userId == userId:
            self.user2.userId = None
            self.user2.nickname = '--'
            self.user2.cnx = None
            self.user2.isOnline = False
            self.user2.slot = True
            self.nbPlayers -= 1

        if self.user3.userId == userId:
            self.user3.userId = None
            self.user3.nickname = '--'
            self.user3.cnx = None
            self.user3.isOnline = False
            self.user3.slot = True
            self.nbPlayers -= 1

        if self.user4.userId == userId:
            self.user4.userId = None
            self.user4.nickname = '--'
            self.user4.cnx = None
            self.user4.isOnline = False
            self.user4.slot = True
            self.nbPlayers -= 1

        if self.user5.userId == userId:
            self.user5.userId = None
            self.user5.nickname = '--'
            self.user5.cnx = None
            self.user5.isOnline = False
            self.user5.slot = True
            self.nbPlayers -= 1

    def reconnectPlayer(self, client):
        if self.user1.userId == client.user:
            self.user1.isOnline = True
            self.user1.cnx = client

        if self.user2.userId == client.user:
            self.user2.isOnline = True
            self.user2.cnx = client

        if self.user3.userId == client.user:
            self.user3.isOnline = True
            self.user3.cnx = client

        if self.user4.userId == client.user:
            self.user4.isOnline = True
            self.user4.cnx = client

        if self.user5.userId == client.user:
            self.user5.isOnline = True
            self.user5.cnx = client

    def onLineClients(self):
        returnList = []

        if self.user1.cnx:
            returnList.append(self.user1.cnx)

        if self.user2.cnx:
            returnList.append(self.user2.cnx)

        if self.user3.cnx:
            returnList.append(self.user3.cnx)

        if self.user4.cnx:
            returnList.append(self.user4.cnx)

        if self.user5.cnx:
            returnList.append(self.user5.cnx)

        return returnList

    def isPlayable(self):
        if len(self.onLineClients()) == self.maxPlayers:
            return True
        else:
            return False

    def freeSlot(self):
        if self.nbPlayers < self.maxPlayers:
            return True
        else:
            return False

    def userPlaysInThisGame(self, userId):
        flag = False

        if self.user1.userId == userId:
            flag = True

        if self.user2.userId == userId:
            flag = True

        if self.user3.userId == userId:
            flag = True

        if self.user4.userId == userId:
            flag = True

        if self.user5.userId == userId:
            flag = True

        return flag

    def isEmpty(self):
        if len(self.onLineClients()) == 0:
            return True
        else:
            return False

    def nobodyPlays(self):
        if self.nbPlayers == 0:
            return True
        else:
            return False

    def captain(self):
        flag = False
        if self.user1.cnx:
            flag = self.user1.userId
        if not flag:
            if self.user2.cnx:
                flag = self.user2.userId
        if not flag:
            if self.user3.cnx:
                flag = self.user3.userId
        if not flag:
            if self.user4.cnx:
                flag = self.user4.userId
        if not flag:
            if self.user5.cnx:
                flag = self.user5.userId
        return flag

    def allVoteOk(self):
        flag = True
        for player in self.cyclePlayers:
            if not player.vote:
                flag = False
        return flag

    def nextNickname(self):
        flag = False
        for player in self.cyclePlayers:
            if player.nextAction:
                flag = player.user.nickname
        return flag

    def dealerNickname(self, position):
        nickname = self.cyclePlayers[position].user.nickname
        return nickname
