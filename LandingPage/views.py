from django.shortcuts import render, render_to_response, redirect

from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

import logging, logging.config
import sys

import requests


LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO'
    }
}

logging.config.dictConfig(LOGGING)

def login(request):
    # context = RequestContext(request, {
    #     'request': request, 'user': request.user})
    # return render_to_response('login.html', context_instance=context)
    #return render(request, 'LandingPage.html')
    logging.info(request)
    return render(request, 'LandingPage.html')


@login_required(login_url='/')
def home(request):
    #return render_to_response('home.html')
    return render_to_response('home.html')



def logout(request):
    auth_logout(request)
    return redirect('/')