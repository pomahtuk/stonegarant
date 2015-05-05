# # -*- coding: utf-8 -*-
from django.contrib import admin
from django.forms import ModelForm #зависимость для переопределения полей формы в админке
from suit_redactor.widgets import RedactorWidget
from suit.widgets import SuitSplitDateTimeWidget

from stonegarant.widgets import *
from stonegarant.models import ReadyWork


class ReadyWorkPageForm(ModelForm):  # вот этот кусок кода дополняет полее ввода картинки её превьюхой
    class Meta:
        widgets = {
            'photo2': AdminImageWidget,
        }


class ReadyWorkInlineForm(ModelForm):  # вот этот кусок кода дополняет полее ввода картинки её превьюхой
    exclude = ('admin_thumb',)

    class Meta:
        widgets = {
            'photo': AdminImageWidget,
            'description': RedactorWidget(editor_options={'lang': 'ru'}),
            'pub_date': SuitSplitDateTimeWidget,
        }


class ReadyWorkPageAdmin(admin.ModelAdmin):
    form = ReadyWorkPageForm
    list_display = ('admin_thumbnail', 'title', 'description', 'pub_date', 'memorial')
    search_fields = ['title', 'description']
    ordering = ['-pub_date']
    list_filter = ['pub_date']


class ReadyWorkInline(admin.StackedInline):
    exclude = ('admin_thumb',)
    form = ReadyWorkInlineForm
    model = ReadyWork
    extra = 0
