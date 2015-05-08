# -*- coding: utf-8 -*-
from django.db import models
import os

from memorial import Memorial


def upload_path_handler(self, filename):
    model_type = 'generic'
    model_id = 0
    if self.memorial:
        model_type = 'memorial'
        model_id = self.memorial.pk
    target_filename = os.path.basename(filename)
    return "uploads/{type}/{id}/{file}".format(type=model_type, id=model_id, file=target_filename)


class AttachedImage(models.Model):
    order = models.PositiveIntegerField(verbose_name='Порядок')
    photo = models.FileField(upload_to=upload_path_handler, verbose_name='Изображение', null=True, blank=True)
    memorial = models.ForeignKey(Memorial, verbose_name='Мемориал',
                                 related_name='images', null=True, blank=True)

    def save(self, *args, **kwargs):
        super(AttachedImage, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.photo.url

    class Meta:
        verbose_name = u"Прикрепленное изображение"
        verbose_name_plural = u"Прикрепленные изображения"