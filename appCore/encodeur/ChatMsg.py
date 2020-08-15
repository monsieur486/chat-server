# -*- coding: utf-8 -*-


class ChatMsg:
    def __init__(self, recipientId, recipientNickname, user, nickname, msgToSend):
        self.recipientId = recipientId
        self.recipientNickname = recipientNickname
        self.user = user
        self.nickname = nickname
        self.msgToSend = msgToSend
