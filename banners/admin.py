from django.contrib import admin
from codemirror import CodeMirrorTextarea
from models import *
from django.forms import ModelForm


class BannerCodeForm(ModelForm):
    class Meta:
        widgets = {
            'contents': CodeMirrorTextarea(mode="xml", theme="monokai", config={'htmlMode': True}),
        }


class BannerAdmin(admin.ModelAdmin):
    form = BannerCodeForm
    list_display = ('title', 'active')
    search_fields = ['title', 'active']
    ordering = ('-title',)
    list_editable = ('active',)
    list_filter = (
        ('active', admin.BooleanFieldListFilter),
    )


# Register your models here.
admin.site.register(FooterBanner, BannerAdmin)
admin.site.register(CatalogBanner, BannerAdmin)
