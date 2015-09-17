from django.test import TestCase
from weixin.caller import access_token


# Create your tests here.

class CallerTest(TestCase):
    def test_access_token(self):
        access_token.get_access_token()
