# -*- coding: utf-8 -*-


class GameState(object):
    def __init__(self,
                 gameId,
                 denomination,
                 private,
                 nbPlayers,
                 maxPlayers,
                 isWithChat,
                 isWithRelance,
                 isWithAnnonce,
                 isWithRound,
                 isWithBelge,
                 isWithPetite,
                 isWithGarde,
                 isWithGardeSans,
                 isPlayable,
                 state,
                 user1,
                 user1onLine,
                 user2,
                 user2onLine,
                 user3,
                 user3onLine,
                 user4,
                 user4onLine,
                 user5,
                 user5onLine,
                 captain,
                 ):
        self.gameId = gameId
        self.denomination = denomination
        self.private = private
        self.nbPlayers = nbPlayers
        self.maxPlayers = maxPlayers
        self.isWithChat = isWithChat
        self.isWithRelance = isWithRelance
        self.isWithAnnonce = isWithAnnonce
        self.isWithRound = isWithRound
        self.isWithBelge = isWithBelge
        self.isWithPetite = isWithPetite
        self.isWithGarde = isWithGarde
        self.isWithGardeSans = isWithGardeSans
        self.isPlayable = isPlayable
        self.state = state
        self.user1 = user1
        self.user1onLine = user1onLine
        self.user2 = user2
        self.user2onLine = user2onLine
        self.user3 = user3
        self.user3onLine = user3onLine
        self.user4 = user4
        self.user4onLine = user4onLine
        self.user5 = user5
        self.user5onLine = user5onLine
        self.captain = captain
