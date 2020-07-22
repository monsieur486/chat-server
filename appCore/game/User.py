# -*- coding: utf-8 -*-
from appCore.game.Player import Player


class User:
    def __init__(self, userId, slot):
        self.userId = userId
        self.nickname = '--'
        self.isOnline = False
        self.cnx = None
        self.slot = slot
