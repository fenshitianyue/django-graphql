# -*- coding:UTF-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from datetime import date

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
    passwd = request.GET['PassWord']
    Email = request.GET['Email']
    User.objects.create(name=user_name, password=passwd, email=Email, register_date=date.today())

    message = "<p>注册成功！</p>"
    return HttpResponse(message)

def get_user(request):
    '''
    获取已注册用户信息
    '''
    List = User.objects.all()
    response = ""
    for var in List:
        response += var.name + " | " + var.password + " | " + var.email + "<br>"
    return HttpResponse("<p>" + response + "</p>")

def push_comment(request):
    '''
    发表评论
    '''
    pass

def get_comment(request):
    '''
    获取评论信息
    '''
    pass

# def delete_comment(request):
#     '''
#     删除评论
#     '''
#     pass

# def delete_user(request):
#     '''
#     删除用户
#     '''
#     pass

