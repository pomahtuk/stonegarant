# -*- coding: utf-8 -*-
from django.db import models

from memorial import *

class Stella(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название', null=True, blank=True)
    width = models.BigIntegerField(verbose_name='Ширина, см', default=0)
    height = models.BigIntegerField(verbose_name='Высота, см', default=0)
    length = models.BigIntegerField(verbose_name='Длина, см', default=0)
    added_value = models.BigIntegerField(verbose_name='Надбавка к базовой цене', null=True, blank=True, default=0)
    # memorial reference
    memorial = models.ForeignKey(Memorial, verbose_name='Мемориал', related_name='stella_variants', null=True, blank=True)

    class Meta:
        verbose_name = u"Стэлла"
        verbose_name_plural = u"Стэллы"

    def __unicode__(self):
        return u'%s (%s см, %s см, %s см): +%s руб.' % (self.title, self.width, self.height, self.length, self.added_value)