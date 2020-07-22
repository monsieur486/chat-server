# -*- coding: utf-8 -*-


import time

from colorama import Style, Fore
from appCore.game.GameState import GameState
from appCore.game.GameAction import GameAction
from appCore.mainMsg.StatsInfos import StatsInfos
from appCore.network.network import messageToClient


def t():
    return "[" + time.strftime("%Y-%m-%d %H:%M:%S") + "] "


def log():
    return Style.RESET_ALL + t()


def gamePlayerLogout(self, gameInfos):
    for game in self.factory.games:
        if game.gameId == gameInfos['gameId']:
            game.removePlayer(gameInfos['user'])
            gameConnectInfos = GameState(game.gameId,
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

            gameUpdate = True

            if game.nobodyPlays() or game.isEmpty():
                print(log() + Fore.BLUE + "- partie " + Fore.GREEN + game.gameId + Fore.BLUE + " terminée")
                self.factory.games.remove(game)
                gameUpdate = False

            privatesGames = self.privatesGamesList()
            free4 = self.freeGames(4)
            free5 = self.freeGames(5)
            nbGames = self.nbGames()
            nbPlayers = self.nbPlayers()

            statsInfos = StatsInfos(nbPlayers, nbGames, free4, free5, privatesGames)

            if gameUpdate:
                value = GameAction(statsInfos, gameConnectInfos)
                msg = messageToClient('gameAction', value)
            else:
                msg = messageToClient('updateStatsInfos', statsInfos)

            self.sendAllUsersMsg(msg)
