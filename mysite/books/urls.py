from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^books/$', views.book_list),
    url(r'^search_form/$', views.search_form),
    url(r'^search.*', views.search),
]
