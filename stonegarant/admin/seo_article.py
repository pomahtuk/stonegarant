# # -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms #зависимость для переопределения полей формы в админке
from suit_redactor.widgets import RedactorWidget

from stonegarant.models import SeoArticle


class SeoArticleCategoryInline(admin.StackedInline):
    model = SeoArticle
    extra = 1
    exclude = ('memorial',)

    class Form(forms.ModelForm):  # вот этот кусок кода дополняет полее ввода картинки её превьюхой
        class Meta:
            widgets = {
                'description': RedactorWidget(editor_options={'lang': 'ru'}),
            }


class SeoArticleMemorialInline(admin.StackedInline):
    model = SeoArticle
    extra = 1
    exclude = ('category',)

    class Form(forms.ModelForm):  # вот этот кусок кода дополняет полее ввода картинки её превьюхой
        class Meta:
            widgets = {
                'description': RedactorWidget(editor_options={'lang': 'ru'}),
            }


class SeoArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'memorial', 'category')
    search_fields = ['title', 'description', 'memorial']
    ordering = ('-title',)

    class Form(forms.ModelForm):  # вот этот кусок кода дополняет полее ввода картинки её превьюхой
        class Meta:
            widgets = {
                'description': RedactorWidget(editor_options={'lang': 'ru'}),
            }