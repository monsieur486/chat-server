# -*- coding: utf-8 -*-


from appCore.encodeur.ChatMsg import ChatMsg


class PrivateChatMsg(ChatMsg):
    def __init__(self, recipientId, recipientNickname, user, nickname, msgToSend):
        ChatMsg.__init__(self, user, nickname, msgToSend)
        self.recipientId = recipientId
        self.recipientNickname = recipientNickname
