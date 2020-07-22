# -*- coding: utf-8 -*-


class PlayerTableInfos(object):
    def __init__(self, nickname, score, selectCard, nextAction, isPreneur, viewCall, isOnline):
        self.nickname = nickname
        self.score = score
        self.selectCard = selectCard
        self.nextAction = nextAction
        self.isPreneur = isPreneur
        self.viewCall = viewCall
        self.isOnline = isOnline
