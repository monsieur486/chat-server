# -*- coding: utf-8 -*-


import random

from appCore.game.Player import Player


def initializeGame(game):

    for player in game.cyclePlayers:
        player.deck[:] = []
        player.plis[:] = []
        player.selectCard = 0
        player.nextAction = False
        player.isPreneur = False
        player.isCall = False
        player.viewCall = False
        player.vote = True




