# -*- coding: utf-8 -*-


class PlayState(object):
    def __init__(self,
                 state,
                 nextAction,
                 nextPlayerNickname,
                 donnes,
                 donne,
                 turn,
                 dealerNickname,
                 contract,
                 withChelem,
                 cardCall,
                 color,
                 atoutMax,
                 tablePlayer1,
                 tablePlayer2,
                 tablePlayer3,
                 tablePlayer4,
                 tablePlayer5,
                 centralCards,
                 centralCardsType,
                 deck,
                 positionPlayer
                 ):
        self.state = state
        self.nextAction = nextAction
        self.nextPlayerNickname = nextPlayerNickname
        self.donnes = donnes
        self.donne = donne
        self.turn = turn
        self.dealerNickname = dealerNickname
        self.contract = contract
        self.withChelem = withChelem
        self.cardCall = cardCall
        self.color = color
        self.atoutMax = atoutMax
        self.tablePlayer1 = tablePlayer1
        self.tablePlayer2 = tablePlayer2
        self.tablePlayer3 = tablePlayer3
        self.tablePlayer4 = tablePlayer4
        self.tablePlayer5 = tablePlayer5
        self.centralCards = centralCards
        self.centralCardsType = centralCardsType
        self.deck = deck
        self.positionPlayer = positionPlayer
