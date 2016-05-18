from django.shortcuts import get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from stonegarant.models import *
from django.template import RequestContext
from banners.models import CatalogBanner, FooterBanner
from django.views.decorators.cache import cache_page


DEFAULT_LIMIT = 9999


def determine_sort_order(user_order):
    if user_order == '-price':
        resulting_order = '-discount_price'
    elif user_order == 'price':
        resulting_order = 'discount_price'
    elif user_order == 'title':
        resulting_order = 'title'
    elif user_order == '-title':
        resulting_order = '-title'
    else:
        resulting_order = '-popularity'

    return resulting_order


def paginate_memorials(parent_page, page, limit, sort_order):
    if isinstance(parent_page, Category):
        memorials_list = parent_page.memorial_set.all().order_by(u"%s" % sort_order)
    else:
        memorials_list = Memorial.objects.order_by(u"%s" % sort_order)

    if limit is not None:
        limit = int(limit)
    else:
        limit = DEFAULT_LIMIT  # temp decision

    if page is not None:
        page = int(page)
    else:
        page = 1

    paginator = Paginator(memorials_list, limit)

    try:
        memorials = paginator.page(page)
    except PageNotAnInteger:
        memorials = paginator.page(1)
    except EmptyPage:
        memorials = paginator.page(paginator.num_pages)
        
    return memorials


def get_parent_page(category_slug):
    if category_slug is not None:
        parent_page = get_object_or_404(Category, slug=category_slug)
    else:
        parent_page = get_object_or_404(ServicePage, id=75)

    return parent_page


@cache_page(60 * 60)
def category_view(request, category_slug):
    parent_page = get_parent_page(category_slug)

    footer_banners = FooterBanner.objects.filter(active=True)[:3]
    catalog_banner = CatalogBanner.objects.filter(active=True)[:1]

    page = request.GET.get('page', 1)
    limit = request.GET.get('limit', DEFAULT_LIMIT)
    sort_order = determine_sort_order(request.GET.get('order'))

    memorials = paginate_memorials(parent_page, page, limit, sort_order)

    return render_to_response('catalog.html', {
        'sort_order': sort_order,
        'memorials': memorials,
        'lmt': limit,
        'parent_page': parent_page,
        'footer_banners': footer_banners,
        'catalog_banner': catalog_banner[0],
    }, context_instance=RequestContext(request))


@cache_page(60 * 60)
def memorial_list_view(request):
    return category_view(request, None)


def ajax_memorials(request):
    page_slug = request.POST.get('slug', None)
    page = request.POST.get('page', 1)
    limit = request.POST.get('limit', DEFAULT_LIMIT)
    raw_order = request.POST.get('order', '-popularity')

    parent_page = get_parent_page(page_slug)
    sort_order = determine_sort_order(raw_order)

    memorials = paginate_memorials(parent_page, page, limit, sort_order)

    return render_to_response('memorials_list.html', {
        'memorials': memorials,
    }, context_instance=RequestContext(request))


