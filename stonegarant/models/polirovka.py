# -*- coding: utf-8 -*-
from django.db import models

from memorial import Memorial


class Polirovka(models.Model):
    title = models.TextField(verbose_name='Тип', null=True, blank=True)
    added_value = models.BigIntegerField(verbose_name='Надбавка к базовой цене', null=True, blank=True, default=0)
    # memorial reference
    memorial = models.ForeignKey(Memorial, verbose_name='Мемориал', related_name='polirovka_variants', null=True)

    class Meta:
        verbose_name = u"Вариант полировки"
        verbose_name_plural = u"Варианты полировок"

    def __unicode__(self):
        return u'%s - +%s' % (self.title, self.added_value)