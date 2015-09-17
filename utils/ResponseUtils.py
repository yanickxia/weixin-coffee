__author__ = 'yann'

from django.http import HttpResponse
import json


def to_json(obj):
    return HttpResponse(json.dumps(obj), content_type="application/json")
