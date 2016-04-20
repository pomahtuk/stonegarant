# -*- coding: utf-8 -*-
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

from memorial import *


class ReadyWork(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    photo = ThumbnailerImageField(upload_to='uploads/ready', verbose_name='Изображение', null=True, blank=True)
    admin_thumb_url = models.CharField(max_length=255, null=True, blank=True)
    memorial = models.ForeignKey(Memorial, verbose_name='Мемориал', null=True, blank=True)
    description = models.TextField(verbose_name='Текст', null=True, blank=True)
    pub_date = models.DateTimeField()

    # model methods
    def admin_thumbnail(self):
        output = [
            u'<style>',
            u'.field-admin_thumbnail a{display: block; text-align: center}',
            u'.field-admin_thumbnail a img{display: inline-block;}',
            u'</style>',
        ]
        photo = self.admin_thumb_url
        if not photo:
            create_admin_thumb(False, self)

        output.append(u'<img src="%s" />' % photo)
        return u''.join(output)

    admin_thumbnail.short_description = 'Изображение 1'
    admin_thumbnail.allow_tags = True

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"Готовая работа"
        verbose_name_plural = u"Готовые работы"


def create_admin_thumb(sender, instance, **kwargs):
    # sometimes order is not updated
    if instance.photo:
        photo = instance.photo
        # generate new thumb
        thumbnailer = get_thumbnailer(photo.name, photo)
        thumbnailer_options = ({'size': (100, 100), 'crop': False})
        thumb_file = thumbnailer.get_thumbnail(thumbnailer_options)
        same = instance.admin_thumb_url == thumb_file.url if thumb_file.url else True
        # print u'%s, %s, %s' % (instance.admin_thumb_url, thumb_file.url, same)
        if not same:
            print u'not same'
            instance.admin_thumb_url = thumb_file.url
            print 'thumb_file %s' % thumb_file.url
            instance.save()
    else:
        print 'no image provided'
        # # current thumb is irrelevant
        # instance.admin_thumb = None
        # instance.save()

signals.post_save.connect(create_admin_thumb, sender=ReadyWork)
