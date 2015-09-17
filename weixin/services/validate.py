__author__ = 'yann'

import hashlib
from weixin import const


def is_weixin_serve(signature, timestamp, nonce):
    requests = sorted([const.TOKEN, timestamp, nonce])
    requests = ''.join(requests)
    requests = hashlib.sha1(requests.encode("utf-8")).hexdigest()
    if requests == signature:
        return True
    return False
