__author__ = 'yann'

# -*- coding: utf-8 -*-
import sys, requests, json
from weixin import const
from datetime import *

url = 'http://apis.baidu.com/heweather/weather/free'
header = {"apikey": const.BAIDU_API_STORE_KEY}

last_updated = {'time': None, 'date': None}


def get_weather():
    if last_updated['date'] is None or (datetime.now() - last_updated['time']) > timedelta(hours=1):
        result = requests.get(url=url, params={'city': 'shanghai'}, headers=header).json()
        key = list(result.keys())[0]
        last_updated['date'] = result[key][0]['daily_forecast'][0]
        last_updated['time'] = datetime.now()

    return last_updated['date']
