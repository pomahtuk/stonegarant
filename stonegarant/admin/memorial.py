# # -*- coding: utf-8 -*-
from django.contrib import admin
from django.forms import ModelForm  # зависимость для переопределения полей формы в админке
from suit_redactor.widgets import RedactorWidget
from easy_thumbnails.widgets import ImageClearableFileInput

from stonegarant.widgets import *

from ready_work import ReadyWorkInline
from polirovka import PolirovkaInline
from podstavka import PodstavkaInline
from stella import StellaInline
from cvetnik import CvetnikInline
from seo_article import SeoArticleMemorialInline


# ImageClearableFileInput - replace with bulletproof

class MemorialPageForm(ModelForm):
    class Meta:
        widgets = {
            'photo1': ImageClearableFileInput,
            'photo2': ImageClearableFileInput,
            'description': RedactorWidget(editor_options={'lang': 'ru'}),
        }


class MemorialPageAdmin(admin.ModelAdmin):
    form = MemorialPageForm
    list_display = ('admin_thumbnail', 'title', 'slug', 'number', 'price_face', 'price_circle', 'get_categories')
    search_fields = ['title', 'slug', 'description']
    ordering = ['number']
    inlines = [
        PolirovkaInline,
        PodstavkaInline,
        StellaInline,
        CvetnikInline,
        SeoArticleMemorialInline,
        ReadyWorkInline,
    ]
    fieldsets = (
        (u'Основное', {
            'fields': (
                'photo1', 'photo2', 'number', 'title', 'categories',
            )
        }),
        (u'Цены', {
            'fields': (
                'discount', 'base_price', 'discount_price',
            )
        }),
        (u'Старые значения', {
            'fields': (
                'price_face', 'price_circle', 'stella', 'podstavka', 'cvetnik',
            )
        }),
        (u'SEO', {
            'fields': (
                'seo_keywords', 'seo_description', 'meta_title',
            )
        }),
    )
    suit_form_includes = (
        ('admin/extra.html', 'top'),
    )

