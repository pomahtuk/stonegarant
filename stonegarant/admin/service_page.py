# # -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms #зависимость для переопределения полей формы в админке
from suit_redactor.widgets import RedactorWidget

class ServicePageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ['title', 'description']
    ordering = ('-title',) 
    fields = ('title', 'description', 'seo_keywords', 'seo_description', 'meta_title')
    class form(forms.ModelForm): #вот этот кусок кода дополняет полее ввода картинки её превьюхой
        class Meta:
            widgets = {
                'description': RedactorWidget(editor_options={'lang': 'ru'}),
            }
