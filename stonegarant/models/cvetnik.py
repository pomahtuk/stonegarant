# -*- coding: utf-8 -*-
from django.db import models


class Cvetnik(models.Model):
    title = models.TextField(verbose_name='Название', null=True, blank=True)
    size = models.TextField(verbose_name='Размер', null=True, blank=True)
    added_value = models.BigIntegerField(verbose_name='Надбавка к базовой цене', null=True, blank=True, default=0)

    class Meta:
        verbose_name = u"Вариант цветника"
        verbose_name_plural = u"Варианты цветников"

    def __unicode__(self):
        return u'%s (%s) - +%s' % (self.title, self.size, self.added_value)