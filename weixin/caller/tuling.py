__author__ = 'yann'

import requests
from weixin import const


def chat(info: str, userid: str):
    return requests.get(url='http://www.tuling123.com/openapi/api',
                        params={'key': const.TULING_KEY, 'info': info, 'userid': userid}).json()['text']