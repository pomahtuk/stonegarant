# # -*- coding: utf-8 -*-
from django.contrib import admin

from seo_article import SeoArticleCategoryInline

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    search_fields = ['title']
    ordering = ('-title',)
    inlines = [
        SeoArticleCategoryInline,
    ]
    fields = ['title', 'slug', 'seo_keywords', 'seo_description', 'meta_title']
