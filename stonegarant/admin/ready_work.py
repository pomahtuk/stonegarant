# # -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms #зависимость для переопределения полей формы в админке
from suit_redactor.widgets import RedactorWidget
from suit.widgets import SuitSplitDateTimeWidget

from stonegarant.widgets import *
from stonegarant.models import ReadyWork

class ReadyWorkPageAdmin(admin.ModelAdmin):
    list_display = ('admin_thumbnail','title','description','pub_date','memorial')
    search_fields = ['title', 'description']
    ordering = ['-pub_date']
    list_filter = ['pub_date'] 
    class form(forms.ModelForm): #вот этот кусок кода дополняет полее ввода картинки её превьюхой
        class Meta:
            widgets = {
                'photo': AdminImageWidget,
                'description': RedactorWidget(editor_options={'lang': 'ru'}),
                'pub_date': SuitSplitDateTimeWidget,
            }

class ReadyWorkInline(admin.TabularInline):
    model = ReadyWork
    extra = 1
    class form(forms.ModelForm): #вот этот кусок кода дополняет полее ввода картинки её превьюхой
        class Meta:
            widgets = {
                'photo2': AdminImageWidget,
            }