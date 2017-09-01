# coding:utf8
from __future__ import  unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m',default='avatar/default.jpg',max_length=100,verbose_name='头像')
    nick = models.CharField(max_length=30,verbose_name='昵称',blank=True)
    friend = models.ManyToManyField('self',verbose_name='朋友',blank=True,null=True)
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __unicode__(self):
        return self.username
