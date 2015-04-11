from django.shortcuts import render, render_to_response, redirect

from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

import logging, logging.config
import sys

import requests

import uuid

from django.contrib.auth.models import User
from friendship.models import Friend, Follow

from django.http import HttpResponse

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
    following = Follow.objects.following(request.user)
    allusers = User.objects.all().values('pk')
    other_user = User.objects.get(pk = 3)

    following_created = Follow.objects.add_follower(request.user, other_user)

    return render(request,'home.html',{'allusers':allusers})

@login_required(login_url='/')
def addfriend(request, id):
    following = Follow.objects.following(request.user)
    allusers = User.objects.all().values('pk')
    return render(request,'home.html',{'allusers':allusers})



def logout(request):
    auth_logout(request)
    return redirect('/')