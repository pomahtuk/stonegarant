from django.shortcuts import get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from stonegarant.models import *
from django.template import RequestContext
from django.views.decorators.cache import cache_page


def memorial_view(request, memorial_slug):
    memorial_data = get_object_or_404(Memorial, slug=memorial_slug)
    # add 1 to popularity of this particular monument on view
    memorial_data.popularity += 1
    memorial_data.save()
    return render_to_response('product.html', {'memorial': memorial_data}, context_instance=RequestContext(request))


@cache_page(60 * 60)
def memorial_list_view(request):
    service_page_data = get_object_or_404(ServicePage, id=75)

    sort_order = request.GET.get('order')
    page = request.GET.get('page')
    limit = request.GET.get('limit')

    if sort_order == '-price':
        sort_order = '-base_price'
    elif sort_order == 'price':
        sort_order = 'base_price'
    elif sort_order == 'title':
        sort_order = 'title'
    elif sort_order == '-title':
        sort_order = '-title'
    else:
        sort_order = '-popularity'

    # this could be tricky
    memorials_list = Memorial.objects.order_by(u"%s" % sort_order)

    if limit is not None:
        lmt = int(limit)
    else:
        lmt = 100  # temp decision

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
        'sort_order': sort_order,
        'memorials': memorials,
        'lmt': lmt,
        'service_page': service_page_data
    }, context_instance=RequestContext(request))