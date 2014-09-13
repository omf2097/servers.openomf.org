# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', include('servers_openomf.main.urls', namespace="mainsite")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('servers_openomf.main.urls')),
)

admin.autodiscover()
