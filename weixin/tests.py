from django.test import TestCase
from weixin.caller import access_token
from weixin.services import reply
from xml.etree import ElementTree


# Create your tests here.

class CallerTest(TestCase):
    def test_access_token(self):
        access_token.get_access_token()


class WeatherTest(TestCase):
    def test_get_weather(self):
        data = reply.process_reply(ElementTree.fromstring("""
                 <xml>
         <ToUserName><![CDATA[toUser]]></ToUserName>
         <FromUserName><![CDATA[fromUser]]></FromUserName>
         <CreateTime>1348831860</CreateTime>
         <MsgType><![CDATA[text]]></MsgType>
         <Content><![CDATA[天气]]></Content>
         <MsgId>1234567890123456</MsgId>
         </xml>
        """))

        print(data)

