# -*- coding: utf-8 -*-
from django.db import models


class SeoEmpoweredModel(models.Model):
    seo_keywords = models.CharField(max_length=300, verbose_name='Ключевые слова', null=True, blank=True)
    seo_description = models.CharField(max_length=300, verbose_name='SEO-описание', null=True, blank=True)
    meta_title = models.CharField(max_length=300, verbose_name='META title', null=True, blank=True)