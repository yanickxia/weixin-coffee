__author__ = 'yann'

from weixin import const
from weixin.models import AccessToken
from datetime import *
import requests
import logging

logger = logging.getLogger(__name__).setLevel(logging.DEBUG)
access_token_url = 'https://api.weixin.qq.com/cgi-bin/token'
call_back_ip_url = 'https://api.weixin.qq.com/cgi-bin/getcallbackip'


def get_access_token():
    logger.debug("get access token")

    access_token = AccessToken.objects.all()
    if access_token.exists() and access_token[0].expires_time < datetime.now():
        return access_token

    params = {'grant_type': 'client_credential', 'appid': const.APP_ID, 'secret': const.APP_SECRET}
    dates = requests.get(access_token_url, params).json()
    now = datetime.now() + timedelta(seconds=(dates['expires_in'] - (60 * 2)))
    access_token = AccessToken(access_token=dates['access_token'], expires_time=now)
    access_token.save()

    return access_token


def get_call_back_ip():
    logger.debug("get call back ip")

    access_token = get_access_token()
    params = {'access_token': access_token.access_token}

    return requests.get(call_back_ip_url, params).json()
