from django.shortcuts import get_object_or_404, render
from stonegarant.models import *
from django.template import RequestContext
import datetime


def not_found_view(request, *args, **kwargs):
    return render(request, '404.html', status=404)


def index_view(request):
    all_replies = Reply.objects.all()
    page = get_object_or_404(ServicePage, id=74)
    return render(request, 'index.html', {
        'replies': all_replies,
        'page': page
    })

def robots_view(request):
    return render(request, 'robots.txt', content_type="text/plain")

def sitemap_view(request):
    memorials = Memorial.objects.all()
    pages = StaticPage.objects.all()
    categories = Category.objects.all()
    now = datetime.datetime.now()
    return render(request, 'sitemap.xml', {
        'memorials': memorials,
        'pages': pages,
        'categories': categories,
        'now': now
    }, content_type="application/xml")
