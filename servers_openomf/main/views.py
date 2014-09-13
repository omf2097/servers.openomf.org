# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse

def index(request):
    return render_to_response('main/index.html', {
    }, context_instance=RequestContext(request))
