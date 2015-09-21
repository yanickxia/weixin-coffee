__author__ = 'yann'

from weixin.services import message


# return xml
def process_reply(xml_data):
    msg_type = xml_data.find("MsgType").text

    if msg_type == 'text':
        content = xml_data.find("Content").text
        from_user = xml_data.find("FromUserName").text
        return message.reply_text_message(from_user, content)
