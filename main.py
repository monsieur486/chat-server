# -*- coding: utf-8 -*-


import Queue
import json
import time
import jsonpickle

from colorama import Fore, Style
from twisted.internet import reactor, protocol
from twisted.protocols import basic
from appCore.decodeur.analyseMsg import analyseMsg
from appCore.encodeur.ChangeInfos import ChangeInfos
from appCore.encodeur.StatesInfos import StatsInfos
from appCore.network.network import MessageToClient


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
        self.user = "anonyme"
        self.nickname = "anonyme"

    def connectionMade(self):
        user01State = self.factory.user01State
        user02State = self.factory.user02State
        user03State = self.factory.user03State

        statsInfos = StatsInfos(user01State, user02State, user03State)

        msg = MessageToClient('cnx', statsInfos)
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

        if user == 'user01':
            self.factory.user01State = 0

        if user == 'user02':
            self.factory.user02State = 0

        if user == 'user03':
            self.factory.user03State = 0

        user01State = self.factory.user01State
        user02State = self.factory.user02State
        user03State = self.factory.user03State

        self.factory.onlineClients.remove(self)

        value = ChangeInfos("loose",
                            self.user,
                            self.nickname,
                            StatsInfos(
                                user01State,
                                user02State,
                                user03State)
                            )
        msg = MessageToClient('mainAction', value)
        self.sendAllUsersMsg(msg)

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

    # def rawDataReceived(self, data):
    #     pass

    ####################################################################################################################

    def sendMsg(self, msg):
        self.sendLine(serialize(msg))

    def sendAllUsersMsg(self, msg):
        for client in self.factory.onlineClients:
            client.sendLine(serialize(msg))

    def sendUserIdMsg(self, userID, msg):
        for client in self.factory.onlineClients:
            if client.user == userID:
                client.sendLine(serialize(msg))

    ####################################################################################################################

    def connectionAccept(self, user):
        self.user = user
        self.authenticated = True

        if user == 'user01':
            self.nickname = "Poste 01"
            self.factory.user01State = 1

        if user == 'user02':
            self.nickname = "Poste 02"
            self.factory.user02State = 1

        if user == 'user03':
            self.nickname = "Poste 03"
            self.factory.user03State = 1

        user01State = self.factory.user01State
        user02State = self.factory.user02State
        user03State = self.factory.user03State

        value = ChangeInfos("win",
                            self.user,
                            self.nickname,
                            StatsInfos(
                                user01State,
                                user02State,
                                user03State)
                            )
        msg = MessageToClient('mainAction', value)
        self.sendAllUsersMsg(msg)

        msg = Style.RESET_ALL + t()
        msg += Fore.BLUE + "~ adresse IP "
        msg += Fore.YELLOW + self.transport.getPeer().host
        msg += Fore.BLUE + " validée pour l'utilisateur "
        msg += Fore.GREEN + self.user
        print(msg)

    ####################################################################################################################


class EchoServerFactory(protocol.ServerFactory):
    def __init__(self):
        pass

    protocol = EchoProtocol
    onlineClients = []
    user01State = 0
    user02State = 0
    user03State = 0


if __name__ == "__main__":
    reactor.listenTCP(12534, EchoServerFactory())
    reactor.run()
