from django.conf.urls import url,include
from views import *
from  webqq import settings

urlpatterns = [
    url(r'^$',index,name='index'),
    url(r'^sendMsg$',sendMsg,name='sendMsg'),
    url(r'^getMsg$',getMsg,name='getMsg'),
    url(r'^getMember$',getMember,name='getMember'),
]

