# -*- coding: utf-8 -*-


import Queue
import json
import time
import jsonpickle

from colorama import Fore, Style
from twisted.internet import reactor, protocol
from twisted.protocols import basic
from appCore.decodeur.analyseMsg import analyseMsg
from appCore.game.GameState import GameState
from appCore.game.gameLooseUser import gameLooseUser
from appCore.mainMsg.MainAction import MainAction
from appCore.mainMsg.StatsInfos import StatsInfos
from appCore.mainMsg.playerLogOut import playerLogOut
from appCore.network.network import messageToClient, getRequest, getUserInfos


def t():
    return "[" + time.strftime("%Y-%m-%d %H:%M:%S") + "] "


def log():
    return Style.RESET_ALL + t()


print("")
print(log() + Fore.BLUE + 'Initialisation')
print("")
print(Fore.GREEN + "       #########################")
print(Fore.GREEN + "       #                       #")
print(Fore.GREEN + "       #     Serveur ON !!!    #")
print(Fore.GREEN + "       #                       #")
print(Fore.GREEN + "       #########################")
print(Style.RESET_ALL)


jobs = Queue.Queue()


def serialize(msg):
    msgJSON = jsonpickle.encode(msg, unpicklable=False)
    return msgJSON


class EchoProtocol(basic.LineReceiver):
    def __init__(self):
        self.authenticated = False
        self.user = "xxx"
        self.nickname = "xxx"
        self.locale = "Fr"

    def connectionMade(self):
        msg = messageToClient('cnx', "Bienvenue sur l'application : Chat SUB-PUB")
        self.sendMsg(msg)
        self.factory.onlineClients.append(self)

        print(
                Style.RESET_ALL +
                t() +
                Fore.BLUE +
                "+ connection établie depuis l'adresse IP " +
                Fore.YELLOW +
                self.transport.getPeer().host)

    def connectionLost(self, reason):
        user = self.user
        print(log() + Fore.RED + "- connection perdue: " + Fore.GREEN + user)
        gameUpdate = False
        gameId = False
        for game in self.factory.games:
            if game.userPlaysInThisGame(user):
                gameUpdate = True
                gameId = game.gameId
                game.loosePlayer(user)
                if game.nobodyPlays() or game.isEmpty():
                    print(log() + Fore.BLUE + "- partie " + Fore.GREEN + gameId + Fore.BLUE + " terminée")
                    self.factory.games.remove(game)
                    gameUpdate = False

        self.factory.onlineClients.remove(self)
        if gameUpdate:
            gameLooseUser(self, gameId)
        else:
            playerLogOut(self, user)

    def lineReceived(self, line):
        dataBrut = json.dumps(line)
        msgJSON = jsonpickle.decode(dataBrut)
        task = json.loads(msgJSON)

        jobs.put(task)

        while not jobs.empty():
            message = jobs.get()
            code = message['code']
            value = False
            if message['value']:
                value = message['value']
            analyseMsg(self, code, value)

    def rawDataReceived(self, data):
        pass

    ####################################################################################################################

    def sendMsg(self, msg):
        self.sendLine(serialize(msg))

    def sendAllUsersMsg(self, msg):
        for client in self.factory.onlineClients:
            client.sendLine(serialize(msg))

    def sendGameMsg(self, gameId, msg):
        for game in self.factory.games:
            if game.gameId == gameId:
                for client in game.onLineClients():
                    client.sendLine(serialize(msg))

    ####################################################################################################################

    def reconnectUser(self, user):
        for game in self.factory.games:
            if game.userPlaysInThisGame(user):
                self.play = game.gameId
                game.reconnectPlayer(self)

    def connectionAccept(self, user):
        userInfos = getUserInfos(user)
        self.user = user
        self.nickname = (userInfos['nickname']).encode('utf-8')
        self.authenticated = True

        self.reconnectUser(self.user)

        statsInfos = StatsInfos(self.nbPlayers(),
                                self.nbGames(),
                                self.freeGames(4),
                                self.freeGames(5),
                                self.privatesGamesList())

        gameInfos = False
        if self.play:
            gameInfos = self.gameStates(self.play)

        value = MainAction(statsInfos, userInfos, gameInfos)
        msg = messageToClient('mainAction', value)
        self.sendAllUsersMsg(msg)

        msg = Style.RESET_ALL + t()
        msg += Fore.BLUE + "~ adresse IP "
        msg += Fore.YELLOW + self.transport.getPeer().host
        msg += Fore.BLUE + " validée pour l'utilisateur "
        msg += Fore.GREEN + self.user
        print(msg)

    ####################################################################################################################

    def freeGames(self, players):
        nbGames = 0
        for game in self.factory.games:
            if game.freeSlot() and not game.private:
                if game.maxPlayers == players:
                    nbGames += 1
        return nbGames

    def nbGames(self):
        countGame = len(self.factory.games)
        return countGame

    def nbPlayers(self):
        countPlayers = len(self.factory.onlineClients)
        return countPlayers

    def privatesGamesList(self):
        exportList = []
        gameList = sorted(self.factory.games, key=lambda PrivatesGamesList: PrivatesGamesList.denomination)
        for game in gameList:
            if game.freeSlot() and game.private:
                exportList.append((game.gameId, game.maxPlayers, game.denomination))
        return exportList

    def gameStates(self, gameId):
        for game in self.factory.games:
            if game.gameId == gameId:
                result = GameState(game.gameId,
                                   game.denomination,
                                   game.private,
                                   game.nbPlayers,
                                   game.maxPlayers,
                                   game.isWithChat,
                                   game.isWithRelance,
                                   game.isWithAnnonce,
                                   game.isWithRound,
                                   game.isWithBelge,
                                   game.isWithPetite,
                                   game.isWithGarde,
                                   game.isWithGardeSans,
                                   game.isPlayable(),
                                   game.state,
                                   game.user1.nickname,
                                   game.user1.isOnline,
                                   game.user2.nickname,
                                   game.user2.isOnline,
                                   game.user3.nickname,
                                   game.user3.isOnline,
                                   game.user4.nickname,
                                   game.user4.isOnline,
                                   game.user5.nickname,
                                   game.user5.isOnline,
                                   game.captain(),
                                   )
                return result

    def getGameFromId(self, gameId):
        for game in self.factory.games:
            if game.gameId == gameId:
                return game


class EchoServerFactory(protocol.ServerFactory):
    def __init__(self):
        pass

    protocol = EchoProtocol
    onlineClients = []
    games = []


if __name__ == "__main__":
    reactor.listenTCP(12530, EchoServerFactory())
    reactor.run()
