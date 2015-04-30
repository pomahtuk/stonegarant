from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from tastypie.api import Api
from stonegarant import views

from tastypie.api import Api
from stonegarant.resources import MemorialResource

v1_api = Api(api_name='v1')
v1_api.register(MemorialResource())

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.index, name="index"),

    url(r'^catalog/(?P<category_slug>(.+))', views.catalog_category, name="category"),
    url(r'^catalog/', views.catalog, name="catalog"),
    url(r'^memorial-(?P<memorial_slug>(.+))', views.memorial, name="memorial"),

    url(r'^api/', include(v1_api.urls)),
    url(r'^page-raboty', views.ready_works, name="ready"),
    url(r'^page-reply', views.replies, name="reply"),
    url(r'^page-articles', views.articles, name="article"),
    url(r'^page-(?P<page_slug>(.+))', views.static_page, name="page"),

    url(r'^404', views.not_found, name="404"),

    url(r'^sitemap.xml$', views.sitemap, name="sitemap"),
)

handler404 = views.not_found

if settings.DEBUG:
    urlpatterns += patterns('', 
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )