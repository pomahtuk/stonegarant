# # -*- coding: utf-8 -*-
from django.contrib import admin
from django.forms import ModelForm  # зависимость для переопределения полей формы в админке
from suit_redactor.widgets import RedactorWidget
from easy_thumbnails.widgets import ImageClearableFileInput

from stonegarant.widgets import *

from ready_work import ReadyWorkInline
from stella import StellaInline
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
        StellaInline,
        SeoArticleMemorialInline,
        ReadyWorkInline,
    ]
    readonly_fields = ('discount_percent',)
    fieldsets = (
        (u'Основное', {
            'fields': (
                'photo1', 'photo2', 'number', 'title', 'categories',
            )
        }),
        (u'Цены', {
            'fields': (
                'discount', 'base_price', 'discount_price', 'discount_percent',
            )
        }),
        (u'Старые значения', {
            'fields': (
                'price_face', 'price_circle', 'stella', 'podstavka', 'cvetnik',
            )
        }),
        (u'Сортировка (считается автоматически)', {
            'fields': (
                'popularity',
            )
        }),
        (u'SEO', {
            'fields': (
                'seo_keywords', 'seo_description', 'meta_title',
            )
        }),
        (u'На будущее', {
            'fields': (
                'granit',
            )
        })
    )
    suit_form_includes = (
        ('admin/extra.html', 'top'),
    )

