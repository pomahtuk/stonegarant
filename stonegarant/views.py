from django.shortcuts import get_object_or_404, get_list_or_404, render_to_response, render, redirect
from django.views.decorators.cache import cache_page
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import *
from django.template import RequestContext, Context
import datetime

def not_found (request):
  return render(request,'404.html', status=404)

def index (request):
  replies = Reply.objects.all()
  page = get_object_or_404(ServicePage, id=74)
  return render_to_response('index.html', {'replies':replies, 'page':page}, context_instance=RequestContext(request))

def memorial (request, memorial_slug):
  memorial = get_object_or_404(Memorial, slug=memorial_slug)
  return render_to_response('product.html', {'memorial':memorial}, context_instance=RequestContext(request))

def static_page (request, page_slug):
  page = get_object_or_404(StaticPage, slug=page_slug)
  return render_to_response('content.html', {'page':page}, context_instance=RequestContext(request))

def articles (request):
  articles = StaticPage.objects.filter(show_in_list=True)
  service_page = get_object_or_404(ServicePage, id=80)
  return render_to_response('article.html', {'articles':articles, 'service_page':service_page}, context_instance=RequestContext(request))

def ready_works (request):
  works = ReadyWork.objects.all().order_by('-pub_date')
  service_page = get_object_or_404(ServicePage, id=76)
  return render_to_response('ready_work.html', {'works':works, 'service_page':service_page}, context_instance=RequestContext(request))

def replies (request):
  replies = Reply.objects.all().order_by('-id')
  service_page = get_object_or_404(ServicePage, id=77)
  return render_to_response('reply.html', {'replies':replies, 'service_page':service_page}, context_instance=RequestContext(request))

def sitemap (request):
  memorials = Memorial.objects.all()
  pages = StaticPage.objects.all()
  categories = Category.objects.all()
  now = datetime.datetime.now()
  return render_to_response('sitemap.xml', {'memorials':memorials, 'pages':pages, 'categories':categories, 'now':now}, context_instance=RequestContext(request), mimetype="application/xml")

def catalog (request):
  memorial_list = Memorial.objects.order_by("number")
  service_page = get_object_or_404(ServicePage, id=75)
  
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
    
  return render_to_response('catalog.html', {'memorials': memorials, 'lmt':lmt, 'service_page':service_page}, context_instance = RequestContext(request))

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