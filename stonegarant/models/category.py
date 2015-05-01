# -*- coding: utf-8 -*-
from uuslug import uuslug
from django.db import models

from seo_model import *


class Category(SeoEmpoweredModel):
    title = models.CharField(max_length=50, unique=True, verbose_name='Название')
    slug = models.CharField(max_length=255, verbose_name='URL')

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = u"Старая категория"
        verbose_name_plural = u"Старые категории"