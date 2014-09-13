# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'servers_openomf.main.views',
    url(r'^servers/$', 'servers', name="servers"),
    url(r'^search/$', 'search', name="search"),
    url(r'^login/$', 'login', name="login"),
    url(r'^profile/$', 'profile', name="profile"),
    url(r'^$', 'index', name="index"),
)
