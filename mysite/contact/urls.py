from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^ok.*', views.ok),
    url(r'^$', views.contact),
]
