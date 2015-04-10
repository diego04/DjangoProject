from django.shortcuts import render, render_to_response, redirect

from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

import logging, logging.config
import sys

import requests

from django.contrib.auth.models import User
from friendship.models import Friend, Follow
#from friendship.models import *

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
    testing = "ei"
    return render(request, 'LandingPage.html',{'test':testing})


@login_required(login_url='/')
def home(request):
    #return render_to_response('home.html')

    following = Follow.objects.following(request.user)


    return render_to_response('home.html')



def logout(request):
    auth_logout(request)
    return redirect('/')