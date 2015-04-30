# -*- coding: utf-8 -*-
from seo_model import *

class StaticPage(SeoEmpoweredModel):
    title        = models.CharField(max_length=100, verbose_name='Название')
    slug         = models.CharField(max_length=255, verbose_name='URL')
    short        = models.TextField(verbose_name='Короткое поисание', null=True, blank=True)
    description  = models.TextField(verbose_name='Текст', null=True, blank=True)
    show_in_list = models.BooleanField(verbose_name='Статья?', default=False, blank=True)
    def save(self, *args, **kwargs):
        # self.slug = uuslug(self.name, instance=self, separator="_") # optional non-dash separator
        self.slug = uuslug(self.title, instance=self)
        super(StaticPage, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = u"Страница"
        verbose_name_plural = u"Страницы"