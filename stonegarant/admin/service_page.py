# # -*- coding: utf-8 -*-
from django.contrib import admin
from django.forms import ModelForm  # зависимость для переопределения полей формы в админке
from suit_redactor.widgets import RedactorWidget


class ServicePageForm(ModelForm):  # вот этот кусок кода дополняет полее ввода картинки её превьюхой
    class Meta:
        widgets = {
            'description': RedactorWidget(editor_options={'lang': 'ru'}),
        }


class ServicePageAdmin(admin.ModelAdmin):
    form = ServicePageForm
    list_display = ('id', 'title', 'description')
    search_fields = ['title', 'description']
    ordering = ('-title',) 
    fields = ('title', 'description', 'seo_keywords', 'seo_description', 'meta_title')

