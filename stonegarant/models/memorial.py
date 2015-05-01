# -*- coding: utf-8 -*-
from datetime import *
from uuslug import uuslug
from django.db import models

from seo_model import SeoEmpoweredModel
from category import *
from stella import *
from polirovka import *
from cvetnik import *

# to be clear:
# we need to have memorial variation depending on:
# variant of stella
# presence of podstavka
# variant of polirovka
# sizes of cvetnik
# and based on cheapest option provide a price
# but now we are faking this one

# ordered memorial should be stored in separate model, associated with orders model

# As well we need to add some sort criteria
# and find a way to sort by popularity
# sort by price
# sort by name

# Price could be a text (from ...) and int (...)
# This will be based on presence of memorial variants

# Will it be a good decision  to calculate price after discount?


class Memorial(SeoEmpoweredModel):
    photo1 = models.ImageField(upload_to='uploads/memorials', verbose_name='Изображение 1', null=True, blank=True)
    photo2 = models.ImageField(upload_to='uploads/memorials', verbose_name='Изображение 2', null=True, blank=True)
    number = models.BigIntegerField(unique=True, verbose_name='Номер')
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    slug = models.CharField(max_length=255, verbose_name='URL')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    categories = models.ManyToManyField(Category, verbose_name='Категории')

    # this fields will be deprecated
    stella = models.CharField(max_length=50, verbose_name='Стелла')
    podstavka = models.CharField(max_length=50, verbose_name='Подставка')
    cvetnik = models.CharField(max_length=50, verbose_name='Цветник')

    # and this prices but... wait...
    price_face = models.BigIntegerField(verbose_name='Цена за лицевую полировку')
    price_circle = models.BigIntegerField(verbose_name='Цена за круговую полировку')

    stella_variants = models.ManyToManyField(Stella, verbose_name='Варианты стэллы')
    cvetnik_variants = models.ManyToManyField(Cvetnik, verbose_name='Варианты цветника')
    polirovka_variants = models.ManyToManyField(Polirovka, verbose_name='Варианты полировки')

    discount = models.BooleanField(verbose_name='Со скидкой')
    discount_percent = models.BigIntegerField(verbose_name='Скидка(процент)', null=True, blank=True)
    discount_price = models.BigIntegerField(verbose_name='Цена со скидкой', null=True, blank=True)

    base_price = models.BigIntegerField(verbose_name='Базовая цена', null=True, blank=True)
    # price_from - calculate

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self)
        super(Memorial, self).save(*args, **kwargs)

    # model methods
    def admin_thumbnail(self):
        if self.photo1:
            return u'<img src="%s" height="100" width="100"/>' % self.photo1.url
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