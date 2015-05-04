# # -*- coding: utf-8 -*-
from django.contrib import admin

from stonegarant.models import Cvetnik

class CvetnikAdmin(admin.ModelAdmin):
    list_display = ('title', 'length', 'width', 'height', 'added_value', 'memorial')
    search_fields = ['title', 'width', 'height', 'length', 'added_value', 'memorial']
    ordering = ('-title',)


class CvetnikInline(admin.StackedInline):
    model = Cvetnik
    extra = 1