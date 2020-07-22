# -*- coding: utf-8 -*-


from appCore.mainMsg.StatsInfos import StatsInfos
from appCore.mainMsg.UpdateAction import UpdateAction
from appCore.network.network import messageToClient


def playerLogOut(self, nickname):
    privatesGames = self.privatesGamesList()
    free4 = self.freeGames(4)
    free5 = self.freeGames(5)
    nbGames = self.nbGames()
    nbPlayers = self.nbPlayers()

    statsInfos = StatsInfos(nbPlayers, nbGames, free4, free5, privatesGames)

    value = UpdateAction(statsInfos, nickname)
    msg = messageToClient('updateAction', value)
    self.sendAllUsersMsg(msg)
