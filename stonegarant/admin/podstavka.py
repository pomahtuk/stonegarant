# # -*- coding: utf-8 -*-
from django.contrib import admin

from stonegarant.models import Podstavka
# from stella import StellaChoiceForm


class PodstavkaAdmin(admin.ModelAdmin):
    list_display = ('title', 'length', 'width', 'height', 'length', 'added_value', 'memorial', 'stella')
    search_fields = ['title', 'width', 'height', 'length', 'added_value', 'memorial', 'stella']
    ordering = ('-title',)

class PodstavkaInline(admin.StackedInline):
    # form = StellaChoiceForm
    model = Podstavka
    extra = 0
    suit_classes = 'suit-tab suit-tab-podstavka'