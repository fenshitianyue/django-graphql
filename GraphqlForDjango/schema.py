# -*- coding:UTF-8 -*-

from graphene_django import DjangoObjectType
import graphene

from fakedata.models import User  # 引入User表句柄
from fakedata.models import Comment  # 引入Comment表句柄
from fakedata.models import UserComment  # 引入UserComment表句柄

class UserType(DjangoObjectType):
    class Meta:
        model = User

class CommentType(DjangoObjectType):
    class Meta:
        model = Comment

class UserCommentType(DjangoObjectType):
    class Meta:
        model = UserComment





