# -*- coding: utf-8 -*-
from datetime import *
from uuslug import uuslug
from seo_model import SeoEmpoweredModel
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.files import get_thumbnailer
from django.db.models import signals

from stonegarant.helpres import simple_admin_thumb

from category import *
from granit import *

# ordered memorial should be stored in separate model, associated with orders model

# As well we need to add some sort criteria
# and find a way to sort by popularity
# sort by price
# sort by name

# Price could be a text (from ...) and int (...)
# This will be based on presence of memorial variants


class Memorial(SeoEmpoweredModel):
    admin_thumb = models.CharField(max_length=255, null=True, blank=True)
    catalog_thumb = models.CharField(max_length=255, null=True, blank=True)
    number = models.BigIntegerField(unique=True, verbose_name='Номер')
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    slug = models.CharField(max_length=255, verbose_name='URL')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    categories = models.ManyToManyField(Category, verbose_name='Категории')

    # stella_variants
    discount = models.BooleanField(verbose_name='Со скидкой')
    # discount_percent - auto populated field not exposed to admin area
    discount_percent = models.BigIntegerField(verbose_name='Скидка (процент)', null=True, blank=True)
    discount_price = models.BigIntegerField(verbose_name='Цена со скидкой', null=True, blank=True)

    base_price = models.BigIntegerField(verbose_name='Базовая цена', null=True, blank=True)

    # especially for sorting
    popularity = models.BigIntegerField(verbose_name='Популярность', null=True, blank=True, default=0)

    # future - granit types
    granit = models.ForeignKey(Granit, verbose_name='Тип гранита', null=True, blank=True)

    # it's better, images reference
    # images now available

    # this one generates 'view on site link'
    def get_absolute_url(self):
        return u'/memorial-%s' % self.slug

    def save(self, *args, **kwargs):
        if self.pk is not None:
            orig = Memorial.objects.get(pk=self.pk)
            if not self.discount_price:
                self.discount_price = self.base_price
            # update discount_percent
            if orig and ((orig.discount_price != self.discount_price) or (orig.base_price != self.base_price)):
                if self.base_price > 0:
                    # error!
                    division_value = 100 - (float(self.discount_price) / float(self.base_price) * 100)
                    self.discount_percent = round(division_value)
            if not self.discount_price:
                self.discount_price = self.base_price
        # generate slug
        self.slug = uuslug(self.title, instance=self)
        super(Memorial, self).save(*args, **kwargs)

    def ordered_images(self):
        return self.images.order_by('order')

    def catalog_image(self):
        photo_list = self.images.order_by('order')
        if len(photo_list) > 0:
            return photo_list[0]
        else:
            return False

    # model methods
    def admin_thumbnail(self):
        photo_list = self.images.order_by('order')
        if len(photo_list) > 0:
            photo = photo_list[0].photo
        else:
            photo = None
        return simple_admin_thumb(self, photo)

    def catalog_thumbnail(self):
        photo = self.catalog_thumb
        if photo:
            return photo
        else:
            create_catalog_thumb(False, self)
            return self.catalog_thumb

    def formatted_price(self):
        return "{:,}".format(self.base_price).replace(',', ' ')

    def get_categories(self):
        return "<br>".join([s.title for s in self.categories.all()])

    def get_images(self):
        return self.images.order_by('order')

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


def create_catalog_thumb(sender, instance, **kwargs):
    # sometimes order is not updated
    photo_list = instance.get_images()
    if len(photo_list) > 0:
        photo = photo_list[0].photo
        # generate new thumb
        thumbnailer = get_thumbnailer(photo.name, photo)
        thumbnailer_options = ({'size': (230, 320), 'crop': False, 'autocrop': True})
        thumb_file = thumbnailer.get_thumbnail(thumbnailer_options)
        same = instance.catalog_thumb == thumb_file.url if thumb_file.url else True
        # print u'%s, %s, %s' % (instance.catalog_thumb, thumb_file.url, same)
        if not same:
            # print u'not same'
            instance.catalog_thumb = thumb_file.url
            print 'thumb_file %s' % thumb_file.url
            instance.save()
    else:
        print 'no image provided'


def create_admin_thumb(sender, instance, **kwargs):
    # sometimes order is not updated
    photo_list = instance.get_images()
    if len(photo_list) > 0:
        photo = photo_list[0].photo
        # generate new thumb
        thumbnailer = get_thumbnailer(photo.name, photo)
        thumbnailer_options = ({'size': (100, 100), 'crop': False})
        thumb_file = thumbnailer.get_thumbnail(thumbnailer_options)
        same = instance.admin_thumb == thumb_file.url if thumb_file.url else True
        # print u'%s, %s, %s' % (instance.admin_thumb, thumb_file.url, same)
        if not same:
            print u'not same'
            instance.admin_thumb = thumb_file.url
            print 'thumb_file %s' % thumb_file.url
            instance.save()
    else:
        print 'no image provided'
        # # current thumb is irrelevant
        # instance.admin_thumb = None
        # instance.save()


signals.post_save.connect(create_admin_thumb, sender=Memorial)
signals.post_save.connect(create_catalog_thumb, sender=Memorial)
