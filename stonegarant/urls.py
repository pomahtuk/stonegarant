from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from stonegarant.views import *

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', index_view, name="index"),

    url(r'^catalog/(?P<category_slug>(.+))', category_view, name="category"),
    url(r'^catalog/', memorial_list_view, name="catalog"),
    url(r'^ajax_catalog.html', ajax_memorials, name="ajax_catalog"),
    url(r'^memorial-(?P<memorial_slug>(.+))', memorial_view, name="memorial"),

    url(r'^page-raboty', ready_works_view, name="ready"),
    url(r'^page-reply', replies_view, name="reply"),
    url(r'^page-articles', articles_view, name="article"),
    url(r'^page-(?P<page_slug>(.+))', static_page_view, name="page"),

    url(r'^email-test', order_email_test),

    url(r'^order-create', order_create_view, name="order_create"),
    url(r'^order-confirm-(?P<order_number>(.+))', order_confirm_view, name="order_confirm"),
    url(r'^order-details-(?P<order_number>(.+))', order_details_view, name="order_details"),

    url(r'^404', not_found_view, name="404"),

    url(r'^sitemap.xml$', sitemap_view, name="sitemap"),
    url(r'^robots\.txt$', robots_view, name="robots"),
]

urlpatterns += [
    url(r'^django-rq/', include('django_rq.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = not_found_view
