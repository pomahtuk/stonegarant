# # -*- coding: utf-8 -*-
from models import *
from django.contrib import admin
from feincms.admin import tree_editor
from mptt.admin import MPTTModelAdmin #зависимость для отображения материалов в виде дерева в админке
from django import forms #зависимость для переопределения полей формы в админке
from django.utils.translation import ugettext_lazy as _
from suit_redactor.widgets import RedactorWidget
from widgets import *  #подключаем все свои виджеты

class SeoArticleCategoryInline(admin.StackedInline):
    model = SeoArticle
    extra = 1
    exclude = ('memorial',)
    class form(forms.ModelForm): #вот этот кусок кода дополняет полее ввода картинки её превьюхой
        class Meta:
            widgets = {
                'description': RedactorWidget(editor_options={'lang': 'ru'}),
            }

class SeoArticleMemorialInline(admin.StackedInline):
    model = SeoArticle
    extra = 1
    exclude = ('category',)
    class form(forms.ModelForm): #вот этот кусок кода дополняет полее ввода картинки её превьюхой
        class Meta:
            widgets = {
                'description': RedactorWidget(editor_options={'lang': 'ru'}),
            }

class ReadyWorkInline(admin.TabularInline):
    model = ReadyWork
    extra = 1
    class form(forms.ModelForm): #вот этот кусок кода дополняет полее ввода картинки её превьюхой
        class Meta:
            widgets = {
                'photo2': AdminImageWidget,
            }

class MemorialPageAdmin(admin.ModelAdmin):
    list_display = ('admin_thumbnail','title','number','price_face','price_circle','get_categories')
    search_fields = ['title', 'slug', 'description']
    ordering = ['-title']
    inlines = [
        SeoArticleMemorialInline,
        ReadyWorkInline,
    ]
    fields = ('photo1', 'photo2', 'number', 'title', 'price_face', 'price_circle', 'description', 'stella', 'podstavka', 'cvetnik', 'categories', 'seo_keywords', 'seo_description', 'meta_title')
    class form(forms.ModelForm): #вот этот кусок кода дополняет полее ввода картинки её превьюхой
        class Meta:
            widgets = {
                'photo1': AdminImageWidget, #виджет определён в allvbg/widgets.py
                'photo2': AdminImageWidget,
                'description': RedactorWidget(editor_options={'lang': 'ru'}),
            }

class StaticPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','description')
    search_fields = ['title', 'slug', 'description']
    ordering = ('-title',) 
    exclude = ('slug',)
    fields = ('title', 'description', 'seo_keywords', 'seo_description', 'meta_title')
    class form(forms.ModelForm): #вот этот кусок кода дополняет полее ввода картинки её превьюхой
        class Meta:
            widgets = {
                'description': RedactorWidget(editor_options={'lang': 'ru'}),
            }

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title']
    ordering = ('-title',)
    inlines = [
        SeoArticleCategoryInline,
    ]
    fields = ('title', 'seo_keywords', 'seo_description', 'meta_title')

class SeoArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'memorial', 'category')
    search_fields = ['title', 'description', 'memorial']
    ordering = ('-title',)   
    class form(forms.ModelForm): #вот этот кусок кода дополняет полее ввода картинки её превьюхой
        class Meta:
            widgets = {
                'description': RedactorWidget(editor_options={'lang': 'ru'}),
            }

class OrderAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'email', 'memorial', 'user_name','user_phone','user_comment','status')
    search_fields = ['email', 'memorial', 'user_name','user_phone','user_comment','status']
    ordering = ('-pub_date',)
    list_filter = ['status'] 

admin.site.register(Order, OrderAdmin)
admin.site.register(SeoArticle, SeoArticleAdmin)
admin.site.register(StaticPage, StaticPageAdmin)
admin.site.register(Memorial, MemorialPageAdmin)
admin.site.register(Category, CategoryAdmin)