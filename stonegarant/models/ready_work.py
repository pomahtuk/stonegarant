# -*- coding: utf-8 -*-
from django.db import models

from memorial import *

class ReadyWork(models.Model):
    title       = models.CharField(max_length=50, verbose_name='Название')
    photo       = models.ImageField(upload_to='uploads/ready', verbose_name='Изображение', null=True, blank=True)
    memorial    = models.ForeignKey(Memorial, verbose_name='Мемориал', null=True, blank=True)
    description = models.TextField(verbose_name='Текст', null=True, blank=True)
    pub_date    = models.DateTimeField()

    def admin_thumbnail(self):
        if self.photo:
            return u'<img src="%s" height="100" width="100"/>' % (self.photo.url)
        else:
            return 'нет изображения'
    admin_thumbnail.short_description = 'Изображение 1'
    admin_thumbnail.allow_tags = True

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"Готовая работа"
        verbose_name_plural = u"Готовые работы"