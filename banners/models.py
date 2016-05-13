# -*- coding: utf-8 -*-
from django.db import models


class FooterBanner(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    contents = models.TextField(verbose_name='Текст', null=True, blank=True)
    active = models.BooleanField(null=False, default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"Баннер в подвале"
        verbose_name_plural = u"Баннеры в подвале"


class CatalogBanner(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    contents = models.TextField(verbose_name='Текст', null=True, blank=True)
    active = models.BooleanField(null=False, default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"Баннер в каталоге"
        verbose_name_plural = u"Баннеры в каталоге"