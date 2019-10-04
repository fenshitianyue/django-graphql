# -*- coding:UTF-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from fakedata.models import User  # 引入User表句柄
from fakedata.models import Comment  # 引入Comment表句柄
from fakedata.models import UserComment  # 引入UserComment表句柄

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def register_form(request):
    return render_to_response('register_form.html')

def register(request):
    '''
    注册用户
    '''
    request.encoding = 'utf-8'
    if 'UserName' not in request.GET:
        message = "请填写内容后提交！"
    user_name = request.GET['UserName']
    password = request.GET['PassWord']
    email = request.GET['Email']

    # message = "注册成功！"
    message = user_name + "|" + password + "|" + email
    return HttpResponse(message)


def push_comment(request):
    '''
    发表评论
    '''
    pass

def get_user(request):
    '''
    获取已注册用户信息
    '''
    pass

def get_comment(request):
    '''
    获取评论信息
    '''

def delete_user(request):
    '''
    删除用户
    '''

def delete_comment(request):
    '''
    删除评论
    '''
