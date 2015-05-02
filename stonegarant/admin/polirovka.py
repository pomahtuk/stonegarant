# # -*- coding: utf-8 -*-
from django.contrib import admin


class PolirovkaAdmin(admin.ModelAdmin):
    list_display = ('title', 'added_value', 'memorial')
    search_fields = ['title', 'added_value', 'memorial']
    ordering = ('-title',)