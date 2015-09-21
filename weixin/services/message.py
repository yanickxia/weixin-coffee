__author__ = 'yann'

from weixin import const
from weixin import template
from weixin.caller import access_token
import time
import requests
import logging

logger = logging.getLogger(__name__)


def reply_text_message(to: str, content: str):
    logger.debug("reply text message to %s, content %s" % (to, content))
    return template.reply_text_message % (to, const.WX_ACCOUNT, int(time.time()), content)
