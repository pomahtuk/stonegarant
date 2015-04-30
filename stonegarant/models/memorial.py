# -*- coding: utf-8 -*-
from datetime import *
from uuslug import uuslug

from seo_model import *
from category import *

class Memorial(SeoEmpoweredModel):
    photo1       = models.ImageField(upload_to='uploads/memorials', verbose_name='Изображение 1', null=True, blank=True)
    photo2       = models.ImageField(upload_to='uploads/memorials', verbose_name='Изображение 2', null=True, blank=True)
    number       = models.BigIntegerField(unique=True, verbose_name='Номер')
    title        = models.CharField(max_length=50, verbose_name='Заголовок')
    slug         = models.CharField(max_length=255, verbose_name='URL')
    description  = models.TextField(verbose_name='Описание', null=True, blank=True)
    stella       = models.CharField(max_length=50, verbose_name='Стелла')
    podstavka    = models.CharField(max_length=50, verbose_name='Подставка')
    cvetnik      = models.CharField(max_length=50, verbose_name='Цветник')
    price_face   = models.BigIntegerField(verbose_name='Цена за лицевую полировку')
    price_circle = models.BigIntegerField(verbose_name='Цена за круговую полировку')
    categories   = models.ManyToManyField(Category, verbose_name='Категории')

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self)
        super(Memorial, self).save(*args, **kwargs)

    def admin_thumbnail(self):
        if self.photo1:
            return u'<img src="%s" height="100" width="100"/>' % (self.photo1.url)
        else:
            return 'нет изображения'

    def get_categories(self):
        return "<br>".join([s.title for s in self.categories.all()])

    # admin sections
    get_categories.short_description = 'Категории'
    get_categories.allow_tags = True
    admin_thumbnail.short_description = 'Изображение 1'
    admin_thumbnail.allow_tags = True

    # meta section
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"Памятник"
        verbose_name_plural = u"Памятники"