from django.contrib import admin
from codemirror import CodeMirrorTextarea
from models import *
from django.forms import ModelForm


class BannerCodeForm(ModelForm):
    class Meta:
        widgets = {
            'contents': CodeMirrorTextarea(mode="html"),
        }


# Register your models here.
class FooterBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')
    search_fields = ['title', 'active']
    ordering = ('-title',)


class CatalogBannerAdmin(admin.ModelAdmin):
    form = BannerCodeForm
    list_display = ('title', 'active')
    search_fields = ['title', 'active']
    ordering = ('-title',)


admin.site.register(FooterBanner, FooterBannerAdmin)
admin.site.register(CatalogBanner, CatalogBannerAdmin)
