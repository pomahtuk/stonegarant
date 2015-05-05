# # -*- coding: utf-8 -*-
from django.contrib import admin

from stonegarant.models import Polirovka
# from stella import StellaChoiceForm


class PolirovkaAdmin(admin.ModelAdmin):
    list_display = ('title', 'added_value', 'memorial', 'stella')
    search_fields = ['title', 'added_value', 'memorial', 'stella']
    ordering = ('-title',)


class PolirovkaInline(admin.StackedInline):
    # form = StellaChoiceForm
    model = Polirovka
    extra = 0
    suit_classes = 'suit-tab suit-tab-polirovka'