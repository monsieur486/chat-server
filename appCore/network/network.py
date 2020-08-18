# coding=utf-8


class MessageToClient:
    def __init__(self, code, value):
        self.code = code
        self.value = value


def userIsRegistered(user, password):
    if user and password:
        if user == password:
            userInfos = user
            return userInfos
        else:
            return False
    else:
        return False
