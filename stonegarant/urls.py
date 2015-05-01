from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from stonegarant.views import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', index_view, name="index"),

    url(r'^catalog/(?P<category_slug>(.+))', category_view, name="category"),
    url(r'^catalog/', memorial_list_view, name="catalog"),
    url(r'^memorial-(?P<memorial_slug>(.+))', memorial_view, name="memorial"),

    url(r'^page-raboty', ready_works_view, name="ready"),
    url(r'^page-reply', replies_view, name="reply"),
    url(r'^page-articles', articles_view, name="article"),
    url(r'^page-(?P<page_slug>(.+))', static_page_view, name="page"),

    url(r'^404', not_found_view, name="404"),

    url(r'^sitemap.xml$', sitemap_view, name="sitemap"),
)

handler404 = not_found_view

if settings.DEBUG:
    urlpatterns += patterns('', 
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )