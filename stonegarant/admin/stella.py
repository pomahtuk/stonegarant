# # -*- coding: utf-8 -*-
from django.contrib import admin

from stonegarant.models import Stella


class StellaAdmin(admin.ModelAdmin):
    list_display = ('title', 'length', 'width', 'height', 'added_value', 'memorial')
    search_fields = ['title', 'width', 'height', 'length', 'added_value', 'memorial']
    ordering = ('-title',)


class StellaInline(admin.StackedInline):
    model = Stella
    extra = 1