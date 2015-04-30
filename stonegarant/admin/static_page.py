# # -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms #зависимость для переопределения полей формы в админке
from suit_redactor.widgets import RedactorWidget

class StaticPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'show_in_list', 'short')
    search_fields = ['title', 'slug', 'short', 'description']
    ordering = ('-title',) 
    exclude = ('slug',)
    fields = ('title', 'show_in_list', 'short', 'description', 'seo_keywords', 'seo_description', 'meta_title')
    class form(forms.ModelForm): #вот этот кусок кода дополняет полее ввода картинки её превьюхой
        class Meta:
            widgets = {
                'short': RedactorWidget(editor_options={'lang': 'ru'}),
                'description': RedactorWidget(editor_options={'lang': 'ru'}),
            }