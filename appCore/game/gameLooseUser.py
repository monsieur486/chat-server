# -*- coding: utf-8 -*-


from appCore.game.GameState import GameState
from appCore.game.GameAction import GameAction
from appCore.mainMsg.StatsInfos import StatsInfos
from appCore.network.network import messageToClient


def gameLooseUser(self, gameId):

    for game in self.factory.games:
        if game.gameId == gameId:
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

            privatesGames = self.privatesGamesList()
            free4 = self.freeGames(4)
            free5 = self.freeGames(5)
            nbGames = self.nbGames()
            nbPlayers = self.nbPlayers()

            statsInfos = StatsInfos(nbPlayers, nbGames, free4, free5, privatesGames)

            value = GameAction(statsInfos, gameConnectInfos)
            msg = messageToClient('gameAction', value)
            self.sendAllUsersMsg(msg)
