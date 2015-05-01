# # -*- coding: utf-8 -*-
from django.contrib import admin
from django.forms import ModelForm  # зависимость для переопределения полей формы в админке
from suit_redactor.widgets import RedactorWidget


class StaticPageForm(ModelForm):  # вот этот кусок кода дополняет полее ввода картинки её превьюхой
    class Meta:
        widgets = {
            'description': RedactorWidget(editor_options={'lang': 'ru'}),
        }


class StaticPageAdmin(admin.ModelAdmin):
    form = StaticPageForm
    list_display = ('title', 'slug', 'show_in_list', 'short')
    search_fields = ['title', 'slug', 'short', 'description']
    ordering = ('-title',) 
    exclude = ('slug',)
    fields = ('title', 'show_in_list', 'short', 'description', 'seo_keywords', 'seo_description', 'meta_title')