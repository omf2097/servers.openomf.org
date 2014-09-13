from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', include('servers_openomf.main.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

admin.autodiscover()
