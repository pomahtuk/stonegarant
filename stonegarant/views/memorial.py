from django.shortcuts import get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from stonegarant.models import *
from django.template import RequestContext


def memorial_view(request, memorial_slug):
    memorial_data = get_object_or_404(Memorial, slug=memorial_slug)
    return render_to_response('product.html', {'memorial': memorial_data}, context_instance=RequestContext(request))


def memorial_list_view(request):
    memorials_list = Memorial.objects.order_by("number")
    service_page_data = get_object_or_404(ServicePage, id=75)

    limit = request.GET.get('limit')
    if limit is not None:
        lmt = int(limit)
    else:
        lmt = 100  # temp decision

    page = request.GET.get('page')
    paginator = Paginator(memorials_list, lmt)

    if page is not None:
        pg = int(page)
    else:
        pg = 1

    try:
        memorials = paginator.page(pg)
    except PageNotAnInteger:
        memorials = paginator.page(1)
    except EmptyPage:
        memorials = paginator.page(paginator.num_pages)

    return render_to_response('catalog.html', {
        'memorials': memorials,
        'lmt': lmt,
        'service_page': service_page_data
    }, context_instance=RequestContext(request))