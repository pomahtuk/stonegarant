# # -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms

from stonegarant.models import Stella
from stonegarant.helpres import InlineEditLinkMixin

from cvetnik import CvetnikInline
from podstavka import PodstavkaInline
from polirovka import PolirovkaInline


# class StellaChoiceForm(forms.ModelForm):
#     exclude = ('memorial',)
#
#     def __init__(self, *args, **kwargs):
#         super(StellaChoiceForm, self).__init__(*args, **kwargs)
#         ref = False
#         if self.Meta.model.memorial.field.slug:
#             ref = self.instance.memorial.slug
#         # this will work only after creation of option :(
#         # need other solution
#         self.fields['stella'].queryset = Stella.objects.filter(memorial__slug=ref)


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

    # # Read about form includes in next section
    # suit_form_includes = (
    #     ('admin/examples/country/custom_include.html', 'middle', 'polirovka'),
    #     ('admin/examples/country/custom_include.html', 'middle', 'cities'),
    #     ('admin/examples/country/custom_include.html', 'middle', 'cities'),
    #     ('admin/examples/country/tab_info.html', '', 'info'),
    # )



class StellaInline(InlineEditLinkMixin, admin.TabularInline):
    fields = ['title', 'added_value', 'edit_details']
    model = Stella
    extra = 0
