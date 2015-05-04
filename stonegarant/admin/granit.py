# # -*- coding: utf-8 -*-
from django.contrib import admin


class GranitAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    ordering = ('-title',)
    fields = ['title']
