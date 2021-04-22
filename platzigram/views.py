"""Platzigram views"""
# Django
from django.urls import path
from django.http import HttpResponse, JsonResponse
# Utilities
from datetime import datetime
import pdb
import json


def hello_word(request):
    return HttpResponse("Hello word!\nThe time is {now}".format(
        now=str(datetime.now().strftime('%b %dth, %y - %H:%M hrs'))))


def sort_integers(request):
    numbers = sorted([int(i) for i in request.GET['numbers'].split(",")])
    data = {
        'status': 'ok',
        'numbers': numbers,
        'message': 'Integers sorted successfully.'
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )


def say_hi(request, name, age):
    """Return a greeting"""
    if age < 12:
        message = 'Sorry {}, you\'re not allowed here.'.format(name)
    else:
        message = 'Hello {}, welcome to Platzigram.'.format(name)

    return HttpResponse(message)
