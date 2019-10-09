# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=100)
    pushed_at = models.DateTimeField(default=timezone.now)

