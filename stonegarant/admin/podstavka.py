# # -*- coding: utf-8 -*-
from django.contrib import admin


class PodstavkaAdmin(admin.ModelAdmin):
    list_display = ('title', 'width', 'height', 'length', 'added_value', 'memorial')
    search_fields = ['title', 'width', 'height', 'length', 'added_value', 'memorial']
    ordering = ('-title',)