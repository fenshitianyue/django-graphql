# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# import datetime

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)  # 用户名
    password = models.CharField(max_length=20, default="")  # 密码
    email = models.EmailField()  # email
    register_date = models.DateField()  # 注册时间：YYYY-MM-DD


class Comment(models.Model):
    data = models.CharField(max_length=100)  # 评论内容
    users = models.ManyToManyField(User, through='UserComment')  # 评论和用户是多对多关系

class UserComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    # 添加其他字段
    # pushed_at = models.DateTimeField(default=datetime.datetime.now())
    # TODO:这里以后再做的时候换成上面那行代码，因为timezone.now是带着时区限制的，而django默认时区是美国那边
    pushed_at = models.DateTimeField(default=timezone.now)

    # 使用自定义的名称
    class Meta:
        db_table = "user_comment_relationship"

