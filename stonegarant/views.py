from django.shortcuts import get_object_or_404, get_list_or_404, render_to_response, redirect
from django.views.decorators.cache import cache_page
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import *
from django.template import RequestContext, Context

def index (request):
    p = Reply.objects.all()
    return render_to_response('index.html', {'replies':p}, context_instance=RequestContext(request))

def memorial (request, memorial_slug):
    p = get_object_or_404(Memorial, slug=memorial_slug)
    return render_to_response('product.html', {'memorial':p}, context_instance=RequestContext(request))

def static_page (request, page_slug):
    p = get_object_or_404(StaticPage, slug=page_slug)
    return render_to_response('content.html', {'page':p}, context_instance=RequestContext(request))

def ready_works (request):
    p = ReadyWork.objects.all()
    return render_to_response('ready_work.html', {'works':p}, context_instance=RequestContext(request))

def catalog (request):
  memorial_list = Memorial.objects.order_by("number")
  
  limit = request.GET.get('limit')
  if limit is not None:
    lmt = int(limit)
  else:
    lmt = 100 #temp decision
    
  page = request.GET.get('page')
  if page is not None:
    pg = int(page)
  else:
    pg = 1
  paginator = Paginator(memorial_list, lmt)
  
  try:
    memorials = paginator.page(pg)
  except PageNotAnInteger:
    memorials = paginator.page(1)
  except EmptyPage:
    memorials = paginator.page(paginator.num_pages)
    
  return render_to_response('catalog.html', {'memorials': memorials, 'lmt':lmt}, context_instance = RequestContext(request))

def catalog_category (request, category_slug):
  category      = get_object_or_404(Category, slug=category_slug)
  memorial_list = category.memorial_set.all().order_by("number")
  
  limit = request.GET.get('limit')
  if limit is not None:
    lmt = int(limit)
  else:
    lmt = 100 #temp decision
    
  page = request.GET.get('page')
  if page is not None:
    pg = int(page)
  else:
    pg = 1
  paginator = Paginator(memorial_list, lmt)
  
  try:
    memorials = paginator.page(pg)
  except PageNotAnInteger:
    memorials = paginator.page(1)
  except EmptyPage:
    memorials = paginator.page(paginator.num_pages)
    
  return render_to_response('catalog.html', {'memorials': memorials, 'lmt':lmt, 'category': category}, context_instance = RequestContext(request))