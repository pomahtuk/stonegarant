from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from tastypie.api import Api
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', TemplateView.as_view(template_name='index.html')),
    # Examples:
    # url(r'^$', 'stonegarant.views.home', name='home'),
    # url(r'^stonegarant/', include('stonegarant.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
