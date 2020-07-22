# -*- coding: utf-8 -*-


def nextPlayer(position, maxPlayers):
    nextP = position + 1
    if nextP > maxPlayers - 1:
        nextP = 0
    return nextP
