# coding=utf-8


import ast
import json
import time
import warnings
import requests
import appSettings


def t():
    return "[" + time.strftime("%Y-%m-%d %H:%M:%S") + "] "


class messageToClient:
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
