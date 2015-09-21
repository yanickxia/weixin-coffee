__author__ = 'yann'

# -*- coding: utf-8 -*-
import sys, requests, json
from weixin import const

url = 'http://apis.baidu.com/heweather/weather/free'
header = {"apikey": const.BAIDU_API_STORE_KEY}


def get_weather():
    result = requests.get(url=url, params={'city': 'shanghai'}, headers=header).json()
    key = list(result.keys())[0]
    return result[key][0]['daily_forecast']


class Weather:
    tmp = {}
    wind = {}
    txt_d = None
    txt_n = None

    