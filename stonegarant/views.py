from django.shortcuts import get_object_or_404, get_list_or_404, render_to_response, redirect
from django.views.decorators.cache import cache_page
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import *
from django.template import RequestContext, Context

def index (request):
    p = 'hi'
    return render_to_response('index.html', {'event':p}, context_instance=RequestContext(request))    