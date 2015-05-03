# -*- coding: utf-8 -*-
from datetime import *
from uuslug import uuslug
from seo_model import SeoEmpoweredModel
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.files import get_thumbnailer
from PIL import Image

from category import *

# ordered memorial should be stored in separate model, associated with orders model

# As well we need to add some sort criteria
# and find a way to sort by popularity
# sort by price
# sort by name

# Price could be a text (from ...) and int (...)
# This will be based on presence of memorial variants

# Will it be a good decision  to calculate price after discount?


class Memorial(SeoEmpoweredModel):
    photo1 = ThumbnailerImageField(upload_to='uploads/memorials',
                                   verbose_name='Изображение 1',
                                   null=True,
                                   blank=True
                                   )
    photo2 = ThumbnailerImageField(upload_to='uploads/memorials',
                                   verbose_name='Изображение 2',
                                   null=True,
                                   blank=True
                                   )
    admin_thumb = ThumbnailerImageField(upload_to='uploads/memorials', null=True, blank=True)
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

    # stella_variants
    # podstavka_variants
    # cvetnik_variants
    # polirovka_variants

    discount = models.BooleanField(verbose_name='Со скидкой')
    discount_percent = models.BigIntegerField(verbose_name='Скидка(процент)', null=True, blank=True)
    discount_price = models.BigIntegerField(verbose_name='Цена со скидкой', null=True, blank=True)

    base_price = models.BigIntegerField(verbose_name='Базовая цена', null=True, blank=True)

    # especially for sorting
    popularity = models.BigIntegerField(verbose_name='Популярность', null=True, blank=True, default=0)

    # price_from - calculate

    # this one generates 'view on site link'
    def get_absolute_url(self):
        return u'/memorial-%s' % self.slug

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self)
        super(Memorial, self).save(*args, **kwargs)

    # model methods
    def admin_thumbnail(self):
        output = [
            u'<style>',
            u'.field-admin_thumbnail a{display: block; text-align: center}',
            u'.field-admin_thumbnail a img{display: inline-block;}',
            u'</style>',
        ]
        if self.admin_thumb:
            output.append(u'<img src="%s" />' % self.admin_thumb.url)
            return u''.join(output)
        else:
            if self.photo1:
                try:  # an image
                    Image.open(self.photo1)
                    thumbnailer = get_thumbnailer(self.photo1)
                    thumbnailer_options = ({'size': (100, 100), 'crop': False})
                    thumb_file = thumbnailer.get_thumbnail(thumbnailer_options)
                    # save resulting thumb to admin thumb
                    # self.admin_thumb = thumb_file
                    self.admin_thumb.save(thumb_file.name, thumb_file)
                    self.save()
                    output.append(u'<img src="%s" />' % thumb_file.url)
                    return u''.join(output)
                except IOError:  # not image
                    return 'not an image'

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