# # -*- coding: utf-8 -*-
from django.contrib import admin

from stonegarant.models import Stella
from stonegarant.helpres import InlineEditLinkMixin

from cvetnik import CvetnikInline
from podstavka import PodstavkaInline
from polirovka import PolirovkaInline


class StellaAdmin(admin.ModelAdmin):
    list_display = ('title', 'length', 'width', 'height', 'added_value', 'memorial')
    search_fields = ['title', 'added_value', 'memorial__title']
    ordering = ('-title',)
    inlines = [
        PolirovkaInline,
        PodstavkaInline,
        CvetnikInline,
    ]

    list_filter = ('memorial',)

    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ('memorial', 'title', 'length', 'width', 'height', 'added_value',)
        }),
    ]

    suit_form_tabs = (('general', u'Основное'), ('polirovka', u'Полировка'),
                 ('podstavka', u'Подставка'), ('cvetnik', u'Цветник'))


class StellaInline(InlineEditLinkMixin, admin.TabularInline):
    fields = ['title', 'added_value', 'edit_details']
    model = Stella
    extra = 0
