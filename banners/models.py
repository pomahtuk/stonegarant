# -*- coding: utf-8 -*-
from django.db import models


class FooterBanner(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    active = models.BooleanField(null=False, default=False, verbose_name='Активный')
    link = models.CharField(max_length=255, verbose_name='Ссылка', default='/page-aktsii-i-skidki')
    link_title = models.CharField(max_length=255, verbose_name='Текст на кнопке', default='Рассчитать памятник')
    contents = models.TextField(verbose_name='Содержимое', null=True, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"Баннер в подвале"
        verbose_name_plural = u"Баннеры в подвале"


class CatalogBanner(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    active = models.BooleanField(null=False, default=False, verbose_name='Активный')
    photo = models.FileField(upload_to='/catalog/banners/', verbose_name='Изображение', null=True, blank=True)
    text = models.CharField(max_length=255, verbose_name='Альтернатинвый текст', null=True, blank=True)
    link = models.CharField(max_length=255, verbose_name='ссылка', default='/page-aktsii-i-skidki')
    contents = models.TextField(verbose_name='Содержимое', null=True, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"Баннер в каталоге"
        verbose_name_plural = u"Баннеры в каталоге"