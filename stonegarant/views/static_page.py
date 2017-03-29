from django.shortcuts import get_object_or_404, render
from stonegarant.models import *
from django.template import RequestContext


def static_page_view(request, page_slug):
    page = get_object_or_404(StaticPage, slug=page_slug)
    return render(request, 'content.html', {'page': page})
