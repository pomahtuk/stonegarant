# -*- coding: utf-8 -*-
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

from memorial import Memorial


def upload_path_handler(self, filename):
    model_type = 'generic'
    model_id = 0
    if self.memorial:
        model_type = 'memorial'
        model_id = self.memorial.pk
    return "uploads/{type}/{id}/{file}".format(type=model_type, id=model_id, file=filename)


class AttachedImage(models.Model):
    order = models.PositiveIntegerField(verbose_name='Порядок')
    photo = ThumbnailerImageField(upload_to=upload_path_handler, verbose_name='Изображение')
    memorial = models.ForeignKey(Memorial, verbose_name='Мемориал',
                                 related_name='images', null=True, blank=True)

    def __unicode__(self):
        return self.photo.url

    class Meta:
        verbose_name = u"Прикрепленное изображение"
        verbose_name_plural = u"Прикрепленные изображения"