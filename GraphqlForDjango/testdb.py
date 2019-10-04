# -*- coding:UTF-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from datetime import date
from datetime import datetime

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
        response = "请填写内容后提交！"
    user_name = request.GET['UserName']
    passwd = request.GET['PassWord']
    Email = request.GET['Email']
    User.objects.create(name=user_name, password=passwd, email=Email, register_date=date.today())

    response = "<p>注册成功！</p>"
    return HttpResponse(response)

def get_user(request):
    '''
    获取已注册用户信息
    '''
    List = User.objects.all()
    response = ""
    for var in List:
        response += var.name + " | " + var.password + " | " + var.email + "<br>"
    return HttpResponse("<p>" + response + "</p>")

def push_comment_form(request):
    return render_to_response('comment_form.html')

def push_comment(request):
    '''
    发表评论
    '''
    request.encoding = 'utf-8'
    if 'UserName' not in request.GET:
        message = "请填写内容后提交！"
    user_name = request.GET['UserName']
    message = request.GET['Message']

    # 获取作者中间模型
    user_tmp = User.objects.get(name=user_name)
    # 添加评论,并获取评论中间模型
    comment_tmp = Comment.objects.create(data=message)
    # 向 user_comment_relationship 表添加数据
    UserComment.objects.create(user=user_tmp, comment=comment_tmp, pushed_at=datetime.now())

    response = "<p>注册成功！</p>"
    return HttpResponse(response)

def get_comment(request):
    '''
    获取评论信息
    '''
    List = UserComment.objects.all()
    response = ""
    for var in List:
        response += var.user.name + " | " + str(var.pushed_at)[0:-13] + " | " + var.comment.data + "<br>"
    return HttpResponse("<p>" + response + "</p>")


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

