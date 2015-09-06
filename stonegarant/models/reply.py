# -*- coding: utf-8 -*-
from django.db import models


class Reply(models.Model):
    reply = models.TextField(verbose_name='Отзыв', null=True, blank=True)
    person = models.CharField(max_length=50, verbose_name='Человек', null=True, blank=True)

    class Meta:
        verbose_name = u"Отзыв"
        verbose_name_plural = u"Отзывы"

    def __unicode__(self):
        return self.person