# -*- coding: utf-8 -*-
from uuslug import uuslug

from seo_model import *


class ServicePage(SeoEmpoweredModel):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Текст', null=True, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"Служебная страница"
        verbose_name_plural = u"Служебные страницы"