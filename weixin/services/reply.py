__author__ = 'yann'

from weixin.caller import apistore, tuling
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

        index = str(content).index("天气")
        if index == 0:
            weather = apistore.get_weather()
        else:
            weather = apistore.get_weather(content[:index])
        data = '今天:[%s]\n天气:[日:%s 夜:%s]\n温度:[最高:%s 最低:%s]' \
               % (weather['date'], weather['cond']['txt_d'], weather['cond']['txt_n'], weather['tmp']['max'],
                  weather['tmp']['min'])

    elif '美女' in content or '妹子' in content or 'mm' in content.lower():
        beauty = apistore.get_beauty()
        data = '送你一个妹子大礼包, 想看汉子?抱歉还没实现 \n 图片:%s \n 地址:%s' % (beauty['picUrl'], beauty['url'])

    else:
        data = tuling.chat(content, from_user)

    return message.reply_text_message(from_user, data)
