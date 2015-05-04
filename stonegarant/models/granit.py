# -*- coding: utf-8 -*-
from django.db import models


class Granit(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тип', null=True, blank=True)

    class Meta:
        verbose_name = u"Тип гранита"
        verbose_name_plural = u"Типы гранита"

    def __unicode__(self):
        return self.title