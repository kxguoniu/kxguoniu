# -*- coding:utf-8 -*-
from django.conf.urls import include, url
from views import *

urlpatterns = [
    url(r'^login', login, name='login'),
    url(r'^show', show, name='show'),
]