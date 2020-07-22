# -*- coding: utf-8 -*-


class Player:
    def __init__(self, user):
        self.user = user
        self.deck = []
        self.plis = []
        self.score = 0
        self.selectCard = 0
        self.nextAction = False
        self.isPreneur = False
        self.isCall = False
        self.viewCall = False
        self.vote = True

