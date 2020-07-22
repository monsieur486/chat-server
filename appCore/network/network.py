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


def getRequest(my_request):
    url = appSettings.DATA_URL + my_request
    okRequest = requests.get(url)
    dataBrute = okRequest.json()
    if okRequest.status_code == 200:
        dataRebuild = (ast.literal_eval(json.dumps(dataBrute)))
        result = json.loads(dataRebuild)
        appSettings.dataSrvIsOn = True
        return result


def getUserInfos(user_id):
    url = appSettings.SERVER_URL + "users/" + user_id
    request = requests.get(url)
    if request.status_code == 200:
        dataBrute = request.json()
        data = (ast.literal_eval(json.dumps(dataBrute)))
        result = json.loads(data)
        return result


def userIsRegistered(user, password):
    if user and password:
        url = appSettings.SERVER_URL + 'api-token-auth/'
        payload = {"username": user, "password": password}
        header = {"content-type": "application/json"}
        warnings.filterwarnings('ignore', message='Unverified HTTPS request')
        response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
        status = response.status_code
        if status == 200:
            userInfos = getUserInfos(user)
            return userInfos
        else:
            return False
    else:
        return False
