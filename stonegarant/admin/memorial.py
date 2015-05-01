# # -*- coding: utf-8 -*-
from django.contrib import admin
from django.forms import ModelForm  # зависимость для переопределения полей формы в админке
from suit_redactor.widgets import RedactorWidget

from stonegarant.widgets import *

from ready_work import ReadyWorkInline
from seo_article import SeoArticleMemorialInline


class MemorialPageForm(ModelForm):  # вот этот кусок кода дополняет полее ввода картинки её превьюхой
    class Meta:
        widgets = {
            'photo1': AdminImageWidget,  # виджет определён в widgets.py
            'photo2': AdminImageWidget,
            'description': RedactorWidget(editor_options={'lang': 'ru'}),
        }


class MemorialPageAdmin(admin.ModelAdmin):
    form = MemorialPageForm
    list_display = ('admin_thumbnail', 'title', 'slug', 'number', 'price_face', 'price_circle', 'get_categories')
    search_fields = ['title', 'slug', 'description']
    ordering = ['number']
    inlines = [
        SeoArticleMemorialInline,
        ReadyWorkInline,
    ]
    fields = (
        'photo1', 'photo2', 'number', 
        'title', 'price_face', 'price_circle', 
        'description', 'stella', 'podstavka', 
        'cvetnik', 'categories', 'seo_keywords', 
        'seo_description', 'meta_title'
    )

