from django.shortcuts import get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from stonegarant.models import *
from django.template import RequestContext
from banners.models import CatalogBanner, FooterBanner


def category_view(request, category_slug):
    category_data = get_object_or_404(Category, slug=category_slug)

    footer_banners = FooterBanner.objects.filter(active=True).order_by('-pub_date')[:3]
    catalog_banner = CatalogBanner.objects.filter(active=True).order_by('-pub_date')[:1]

    sort_order = request.GET.get('order')
    page = request.GET.get('page')
    limit = request.GET.get('limit')

    if sort_order == '-price':
        sort_order = '-discount_price'
    elif sort_order == 'price':
        sort_order = 'discount_price'
    elif sort_order == 'title':
        sort_order = 'title'
    elif sort_order == '-title':
        sort_order = '-title'
    else:
        sort_order = 'popularity'

    # this could be tricky
    memorials_list = category_data.memorial_set.all().order_by(u"%s" % sort_order)

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
        'category': category_data,
        'footer_banners': footer_banners,
        'catalog_banner': catalog_banner,
    }, context_instance=RequestContext(request))
