# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse

def index(request):
    return render_to_response('main/index.html', {
    }, context_instance=RequestContext(request))

def servers(request):
    return render_to_response('main/servers.html', {
    }, context_instance=RequestContext(request))

def search(request):
    return render_to_response('main/search.html', {
    }, context_instance=RequestContext(request))

def login(request):
    return render_to_response('main/login.html', {
    }, context_instance=RequestContext(request))

def profile(request):
    return render_to_response('main/profile.html', {
    }, context_instance=RequestContext(request))
