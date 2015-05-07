# -*- coding: utf-8 -*-
from django.db import models

from memorial import Memorial
from stella import Stella


class Polirovka(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тип', null=True, blank=True)
    added_value = models.BigIntegerField(verbose_name='Надбавка к базовой цене', null=True, blank=True, default=0)
    stella = models.ForeignKey(Stella, verbose_name='Стэлла', null=True, blank=True)

    class Meta:
        verbose_name = u"Вариант полировки"
        verbose_name_plural = u"Варианты полировок"

    def __unicode__(self):
        return u'%s - +%s' % (self.title, self.added_value)