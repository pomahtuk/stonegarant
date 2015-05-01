# -*- coding: utf-8 -*-
from django.db import models

from memorial import *
from category import *


class SeoArticle(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Текст', null=True, blank=True)
    memorial = models.ForeignKey(Memorial, verbose_name='Мемориал', null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name='Категория', null=True, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"SEO статья"
        verbose_name_plural = u"SEO статьи"