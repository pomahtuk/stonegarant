from django.shortcuts import get_object_or_404, render_to_response
from stonegarant.models import *
from django.template import RequestContext
from easy_thumbnails.templatetags.thumbnail import thumbnail_url
import threading


def memorial_view(request, memorial_slug):
    memorial_data = get_object_or_404(Memorial.objects.select_related(), slug=memorial_slug)

    catalog_image = memorial_data.catalog_image()

    data_to_render = {
        'ordered_images': [],
        'catalog_image': thumbnail_url(catalog_image.photo, 'product') if catalog_image else False,
        'title': memorial_data.title,
        'description': memorial_data.description,
        'seo_description': memorial_data.seo_description,
        'seo_keywords': memorial_data.seo_keywords,
        'base_price': memorial_data.base_price,
        'formatted_price': memorial_data.formatted_price()
    }

    ordered_images = memorial_data.ordered_images()
    # getting thumbs just suck much
    # slow as hell
    for image in ordered_images:
        data_to_render['ordered_images'].append({
            'product': thumbnail_url(image.photo, 'product'),
            'preview': thumbnail_url(image.photo, 'preview')
        })

    stella_variants = []
    for stella in memorial_data.stella_variants.prefetch_related('cvetnik', 'polirovka', 'podstavka').all():
        stella_variants.append({
            'added_value': stella.added_value,
            'pk': stella.pk,
            'title': stella.title,
            'lightbox_info': stella.lightbox_info,
            'length': stella.length,
            'width': stella.width,
            'height': stella.height,
            'data_size': stella.data_size,
            'text_size': stella.text_size,

            'cvetnik_set': stella.cvetnik.all(),
            'polirovka_set': stella.polirovka.all(),
            'podstavka_set': stella.podstavka.all(),
        })

    # add 1 to popularity of this particular monument on view
    memorial_data.popularity += 1

    # memorial_data.save()
    threading.Thread(target=memorial_data.save).start()

    return render_to_response('product.html', {
        'memorial': data_to_render,
        'stella_variants': stella_variants
    }, context_instance=RequestContext(request))
