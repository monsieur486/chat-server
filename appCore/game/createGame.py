# -*- coding: utf-8 -*-


import time

from appCore.game.Game import Game
from appCore.game.GameState import GameState
from appCore.game.GameAction import GameAction
from appCore.mainMsg.StatsInfos import StatsInfos
from appCore.network.network import messageToClient


def createGame(self, gameInfos):
    key = time.strftime("%d%H%M%S" + gameInfos['user'][4:])
    gameId = 'game#' + key
    denomination = gameInfos['denomination']
    if not denomination:
        denomination = gameId
    private = gameInfos['private']
    password = gameInfos['password']
    maxPlayers = int(gameInfos['maxPlayers'])
    isWithChat = gameInfos['isWithChat']
    isWithRelance = gameInfos['isWithRelance']
    isWithAnnonce = gameInfos['isWithAnnonce']
    isWithRound = gameInfos['isWithRound']
    isWithBelge = gameInfos['isWithBelge']
    isWithPetite = gameInfos['isWithPetite']
    isWithGarde = gameInfos['isWithGarde']
    isWithGardeSans = gameInfos['isWithGardeSans']

    newGame = Game(gameId,
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
                   isWithGardeSans)

    newGame.addPlayer(self)

    self.factory.games.append(newGame)

    gameConnectInfos = GameState(gameId,
                                 denomination,
                                 private,
                                 newGame.nbPlayers,
                                 maxPlayers,
                                 isWithChat,
                                 isWithRelance,
                                 isWithAnnonce,
                                 isWithRound,
                                 isWithBelge,
                                 isWithPetite,
                                 isWithGarde,
                                 isWithGardeSans,
                                 newGame.isPlayable(),
                                 newGame.state,
                                 newGame.user1.nickname,
                                 newGame.user1.isOnline,
                                 newGame.user2.nickname,
                                 newGame.user2.isOnline,
                                 newGame.user3.nickname,
                                 newGame.user3.isOnline,
                                 newGame.user4.nickname,
                                 newGame.user4.isOnline,
                                 newGame.user5.nickname,
                                 newGame.user5.isOnline,
                                 newGame.captain(),
                                 )

    privatesGames = self.privatesGamesList()
    free4 = self.freeGames(4)
    free5 = self.freeGames(5)
    nbGames = self.nbGames()
    nbPlayers = self.nbPlayers()

    statsInfos = StatsInfos(nbPlayers, nbGames, free4, free5, privatesGames)

    value = GameAction(statsInfos, gameConnectInfos)
    msg = messageToClient('gameAction', value)
    self.sendAllUsersMsg(msg)
