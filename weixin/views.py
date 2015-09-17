from django.http import HttpResponse
from utils import ResponseUtils
from weixin.services import validate
from xml.etree import ElementTree


def index(request):
    return HttpResponse("welcome")


def weixin(request):
    if request.method == 'GET':
        return process_get(request)
    else:
        return process_post(request)


def _json(request):
    response_data = {'x': 'xx'}
    return ResponseUtils.to_json(response_data)


def process_get(request):
    signature = request.GET['signature']
    timestamp = request.GET['timestamp']
    nonce = request.GET['nonce']
    echostr = request.GET['echostr']

    if validate.is_weixin_serve(signature, timestamp, nonce):
        return HttpResponse(echostr)
    return HttpResponse("False")


def process_post(request):
    signature = request.GET['signature']
    timestamp = request.GET['timestamp']
    nonce = request.GET['nonce']

    if not validate.is_weixin_serve(signature, timestamp, nonce):
        return HttpResponse("False")

    xml_data = ElementTree.fromstring(request.body)

    msg_type = xml_data.find("MsgType").text
    content = xml_data.find("Content").text
    from_user=xml_data.find("FromUserName").text

    if msg_type == 'text' and content == 'H':
        

