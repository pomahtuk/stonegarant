# -*- coding: utf-8 -*-
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

from memorial import *


class ReadyWork(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    photo = ThumbnailerImageField(upload_to='uploads/ready', verbose_name='Изображение', null=True, blank=True)
    admin_thumb = ThumbnailerImageField(upload_to='uploads/ready', null=True, blank=True)
    memorial = models.ForeignKey(Memorial, verbose_name='Мемориал', null=True, blank=True)
    description = models.TextField(verbose_name='Текст', null=True, blank=True)
    pub_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        if self.pk is not None:
            orig = ReadyWork.objects.get(pk=self.pk)
            if orig.photo != self.photo:
                # generate new thumb
                thumbnailer = get_thumbnailer(self.photo)
                thumbnailer_options = ({'size': (100, 100), 'crop': False})
                thumb_file = thumbnailer.get_thumbnail(thumbnailer_options)
                self.admin_thumb = thumb_file
        super(ReadyWork, self).save(*args, **kwargs)

    # model methods
    def admin_thumbnail(self):
        return admin_thumb(self, self.photo)

    admin_thumbnail.short_description = 'Изображение 1'
    admin_thumbnail.allow_tags = True

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"Готовая работа"
        verbose_name_plural = u"Готовые работы"