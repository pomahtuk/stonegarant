# -*- coding: utf-8 -*-
from django.db import models

from memorial import *


class Stella(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название', null=True, blank=True)
    length = models.BigIntegerField(verbose_name='Длина, см', default=0)
    width = models.BigIntegerField(verbose_name='Ширина, см', default=0)
    height = models.BigIntegerField(verbose_name='Высота, см', default=0)
    added_value = models.BigIntegerField(verbose_name='Надбавка к базовой цене', null=True, blank=True, default=0)
    # memorial reference
    memorial = models.ForeignKey(Memorial, verbose_name='Мемориал', related_name='stella_variants', null=True, blank=True)

    class Meta:
        verbose_name = u"Вариант стэллы"
        verbose_name_plural = u"Варианты стэллы"

    def data_size(self):
        return '%s,%s,%s' % (
            self.length,
            self.width,
            self.height,
        )

    def text_size(self):
        return '%sx%sx%s см' % (
            self.length,
            self.width,
            self.height,
        )

    def __unicode__(self):
        memorial_title = self.memorial.title if self.memorial else ''
        memorial_base_price = self.memorial.base_price if self.memorial else ''
        return u'%s (%s*%s*%sсм, +%s руб.) - %s, %s' % (
            self.title,
            self.length,
            self.width,
            self.height,
            self.added_value,
            memorial_title,
            memorial_base_price,
        )