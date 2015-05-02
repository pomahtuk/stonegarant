# # -*- coding: utf-8 -*-
from django.contrib import admin

from stonegarant.models import Podstavka


class PodstavkaAdmin(admin.ModelAdmin):
    list_display = ('title', 'length', 'width', 'height', 'length', 'added_value', 'memorial')
    search_fields = ['title', 'width', 'height', 'length', 'added_value', 'memorial']
    ordering = ('-title',)

class PodstavkaInline(admin.TabularInline):
    model = Podstavka
    extra = 1