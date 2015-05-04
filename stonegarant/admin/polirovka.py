# # -*- coding: utf-8 -*-
from django.contrib import admin

from stonegarant.models import Polirovka


class PolirovkaAdmin(admin.ModelAdmin):
    list_display = ('title', 'added_value', 'memorial')
    search_fields = ['title', 'added_value', 'memorial']
    ordering = ('-title',)


class PolirovkaInline(admin.StackedInline):
    model = Polirovka
    extra = 1