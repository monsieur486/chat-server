# -*- coding: utf-8 -*-


import random

from appCore.game.PlayState import PlayState
from appCore.game.PlayerTableInfos import PlayerTableInfos
from appCore.game.initializeGame import initializeGame
from appCore.game.nextPlayer import nextPlayer
from appCore.network.network import messageToClient


def coupeDeck(deck):
    n = random.randint(3, 77)
    part1 = deck[:n - 1]
    m = 79 - n
    part2 = deck[-m:]
    result = part2 + part1
    return result


def distributeCards(game, deck, dealer):
    initializeGame(game)

    newDeck = coupeDeck(deck)
    maxPlayers = game.maxPlayers

    if maxPlayers == 5:
        paquets = 21
        chien = 3
    else:
        paquets = 17
        chien = 6

    shuffleDonne = []
    serieDonne = []

    for f in range(chien):
        shuffleDonne.append(4)

    for f in range(paquets):
        shuffleDonne.append(3)

    random.shuffle(shuffleDonne)
    serieDonne.append(3)
    for f in shuffleDonne:
        serieDonne.append(f)

    count = 0
    prevSlot = dealer

    for giveCards in serieDonne:
        selectSlot = nextPlayer(prevSlot, maxPlayers)
        player = game.cyclePlayers[selectSlot]
        if giveCards == 3:
            player.deck.append(newDeck[count])
            player.deck.append(newDeck[count + 1])
            player.deck.append(newDeck[count + 2])
            count += 3
        else:
            game.chien.append(newDeck[count])
            player.deck.append(newDeck[count + 1])
            player.deck.append(newDeck[count + 2])
            player.deck.append(newDeck[count + 3])
            count += 4

        prevSlot = selectSlot

    nextAction = nextPlayer(dealer, maxPlayers)
    player = game.cyclePlayers[nextAction]
    player.nextAction = True

    game.donne += 1
    game.state = 3
    game.nextAction = 1
    game.cyclePosition = game.maxPlayers - 1

    infos = game.cyclePlayers[0]
    nickname = infos.user.nickname
    if game.dealer == 0:
        nickname += ' (D)'
    score = infos.score
    selectCard = infos.selectCard
    nextAction = infos.nextAction
    isPreneur = infos.isPreneur
    viewCall = infos.viewCall
    isOnline = infos.user.isOnline
    player1 = PlayerTableInfos(nickname, score, selectCard, nextAction, isPreneur, viewCall, isOnline)

    infos = game.cyclePlayers[1]
    nickname = infos.user.nickname
    if game.dealer == 1:
        nickname += ' (D)'
    score = infos.score
    selectCard = infos.selectCard
    nextAction = infos.nextAction
    isPreneur = infos.isPreneur
    viewCall = infos.viewCall
    isOnline = infos.user.isOnline
    player2 = PlayerTableInfos(nickname, score, selectCard, nextAction, isPreneur, viewCall, isOnline)

    infos = game.cyclePlayers[2]
    nickname = infos.user.nickname
    if game.dealer == 2:
        nickname += ' (D)'
    score = infos.score
    selectCard = infos.selectCard
    nextAction = infos.nextAction
    isPreneur = infos.isPreneur
    viewCall = infos.viewCall
    isOnline = infos.user.isOnline
    player3 = PlayerTableInfos(nickname, score, selectCard, nextAction, isPreneur, viewCall, isOnline)

    infos = game.cyclePlayers[3]
    nickname = infos.user.nickname
    if game.dealer == 3:
        nickname += ' (D)'
    score = infos.score
    selectCard = infos.selectCard
    nextAction = infos.nextAction
    isPreneur = infos.isPreneur
    viewCall = infos.viewCall
    isOnline = infos.user.isOnline
    player4 = PlayerTableInfos(nickname, score, selectCard, nextAction, isPreneur, viewCall, isOnline)

    if game.maxPlayers == 5:
        infos = game.cyclePlayers[4]
        nickname = infos.user.nickname
        if game.dealer == 4:
            nickname += ' (D)'
        score = infos.score
        selectCard = infos.selectCard
        nextAction = infos.nextAction
        isPreneur = infos.isPreneur
        viewCall = infos.viewCall
        isOnline = infos.user.isOnline
    else:
        nickname = '--'
        score = 0
        selectCard = 0
        nextAction = False
        isPreneur = False
        viewCall = False
        isOnline = True
    player5 = PlayerTableInfos(nickname, score, selectCard, nextAction, isPreneur, viewCall, isOnline)

    position = 0

    for player in game.cyclePlayers:
        state = game.state
        nextAction = game.nextAction
        nextPlayerNickname = game.nextNickname()
        donnes = game.donnes
        donne = game.donne
        turn = game.turn
        dealerNickname = game.dealerNickname(game.dealer)
        contract = game.contract
        withChelem = game.withChelem
        cardCall = game.cardCall
        color = game.color
        atoutMax = game.atoutMax
        tablePlayer1 = player1
        tablePlayer2 = player2
        tablePlayer3 = player3
        tablePlayer4 = player4
        tablePlayer5 = player5
        centralCards = game.centralCards
        centralCardsType = game.centralCardsType
        playerDeck = player.deck
        positionPlayer = position

        value = PlayState(state,
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
                          playerDeck,
                          positionPlayer
                          )
        msg = messageToClient('playActionSelectContract', value)
        player.user.cnx.sendMsg(msg)
        position += 1
