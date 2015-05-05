# # -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms

from stonegarant.models import Cvetnik
# from stella import StellaChoiceForm


class CvetnikAdmin(admin.ModelAdmin):
    list_display = ('title', 'length', 'width', 'height', 'added_value', 'memorial')
    search_fields = ['title', 'width', 'height', 'length', 'added_value', 'memorial']
    ordering = ('-title',)


class CvetnikInline(admin.StackedInline):
    # form = StellaChoiceForm
    model = Cvetnik
    extra = 0
    suit_classes = 'suit-tab suit-tab-cvetnik'