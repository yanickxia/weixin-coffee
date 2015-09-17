from django.shortcuts import render
from django.http import HttpResponse
from utils import ResponseUtils
from weixin.services import validate


def index(request):
    return HttpResponse("welcome")


def weixin(request):
    if request.method != 'GET':
        return HttpResponse("False")

    signature = request.GET['signature']
    timestamp = request.GET['timestamp']
    nonce = request.GET['nonce']
    echostr = request.GET['echostr']

    if validate.is_weixin_serve(signature, timestamp, nonce):
        return HttpResponse(echostr)
    return HttpResponse("False")


def _json(request):
    response_data = {'x': 'xx'}
    return ResponseUtils.to_json(response_data)
