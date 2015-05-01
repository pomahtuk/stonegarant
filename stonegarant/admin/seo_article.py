# # -*- coding: utf-8 -*-
from django.contrib import admin
from django.forms import ModelForm  # зависимость для переопределения полей формы в админке
from suit_redactor.widgets import RedactorWidget

from stonegarant.models import SeoArticle


class SeoArticleForm(ModelForm):  # вот этот кусок кода дополняет полее ввода картинки её превьюхой
    class Meta:
        widgets = {
            'description': RedactorWidget(editor_options={'lang': 'ru'}),
        }


class SeoArticleCategoryInline(admin.StackedInline):
    form = SeoArticleForm
    model = SeoArticle
    extra = 1
    exclude = ('memorial',)


class SeoArticleMemorialInline(admin.StackedInline):
    form = SeoArticleForm
    model = SeoArticle
    extra = 1
    exclude = ('category',)


class SeoArticleAdmin(admin.ModelAdmin):
    form = SeoArticleForm
    list_display = ('title', 'description', 'memorial', 'category')
    search_fields = ['title', 'description', 'memorial']
    ordering = ('-title',)
