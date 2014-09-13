# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'servers_openomf.main.views',
    url(r'^$', 'index', name="index"),
)