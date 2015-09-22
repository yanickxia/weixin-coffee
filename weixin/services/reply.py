__author__ = 'yann'

from weixin.caller import apistore
from weixin.services import message
import logging

logger = logging.getLogger(__name__)


# return xml
def process_reply(xml_data):
    msg_type = xml_data.find("MsgType").text

    if msg_type == 'text':
        return process_text(xml_data)


def process_text(xml_data):
    content = xml_data.find("Content").text
    from_user = xml_data.find("FromUserName").text
    data = None

    if '天气' in content:
        weather = apistore.get_weather()
        data = '今天: ' + weather['date'] + '\n天气:[日:' + weather['cond']['txt_d'] + ' 夜:' \
               + weather['cond']['txt_n'] + '] \n温度:[最高: ' + weather['tmp']['max'] + ' 最低: ' \
               + weather['tmp']['min'] + ']'
    else:
        data = content

    return message.reply_text_message(from_user, data)
