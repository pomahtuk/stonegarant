# -*- coding: utf-8 -*-
from django.db import models

from memorial import Memorial
from stella import Stella


class Podstavka(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тип', null=True, blank=True)
    length = models.BigIntegerField(verbose_name='Длина, см', default=0)
    width = models.BigIntegerField(verbose_name='Ширина, см', default=0)
    height = models.BigIntegerField(verbose_name='Высота, см', default=0)
    added_value = models.BigIntegerField(verbose_name='Надбавка к базовой цене', null=True, blank=True, default=0)
    stella = models.ForeignKey(Stella, verbose_name='Стэлла', null=True, related_name='podstavka')

    class Meta:
        verbose_name = u"Вариант подставки"
        verbose_name_plural = u"Варианты подставок"

    def text_size(self):
        return '%sx%sx%s см' % (
            self.length,
            self.width,
            self.height,
        )

    def order_text(self):
        return 'Подставка %sx%sx%s см' % (
            self.length,
            self.width,
            self.height,
        )

    def lightbox_info(self):
        return '%sx%sx%s см - %s р.' % (
            self.length,
            self.width,
            self.height,
            self.added_value
        )

    def __unicode__(self):
        return u'%s (%s * %s * %s см): +%s руб.' % (self.title, self.length, self.width, self.height, self.added_value)