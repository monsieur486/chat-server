# -*- coding: utf-8 -*-


import random

from appCore.game.Player import Player
from appCore.game.distributeCards import distributeCards
from appCore.game.returnUserFromSlot import returnUserFromSlot


def startGame(self, gameId):
    game = self.getGameFromId(gameId)
    nbPlayers = game.maxPlayers

    game.nextAction = 0
    game.donnes[:] = []
    game.donne = 0
    game.turn = 0
    game.dealer = 0
    game.contract = 0
    game.withChelem = False
    game.cardCall = 0
    game.color = 0
    game.atoutMax = 0
    game.cyclePosition = 0
    game.chien[:] = []

    sampling = list(range(1, nbPlayers + 1))
    random.shuffle(sampling)

    game.cyclePlayers[:] = []

    for position in range(nbPlayers):
        selectSlot = sampling[position]
        user = returnUserFromSlot(game, selectSlot)
        game.cyclePlayers.append(Player(user))

    deck = list(range(1, 79))
    for f in range(1973):
        random.shuffle(deck)

    distributeCards(game, deck, 0)
