# -*- coding:UTF-8 -*-

from django.http import HttpResponse
from fakedata.models import User  # 引入User表句柄
from fakedata.models import Comment  # 引入Comment表句柄
from fakedata.models import UserComment  # 引入UserComment表句柄


def Register(request):
    '''
    注册用户
    '''
    pass

def PushComment(request):
    '''
    发表评论
    '''
    pass

def GetUser(request):
    '''
    获取已注册用户信息
    '''
    pass

def GetComment(request):
    '''
    获取评论信息
    '''

def DeleteUser(request):
    '''
    删除用户
    '''

def DeleteComment(request):
    '''
    删除评论
    '''
