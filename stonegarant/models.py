# -*- coding: utf-8 -*-
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
import hashlib
from datetime import *
from easy_thumbnails.fields import ThumbnailerImageField
from uuslug import uuslug

class SeoEmpoweredModel(models.Model):
    seo_keywords    = models.CharField(max_length=50, verbose_name='Ключевые слова', null=True, blank=True)
    seo_description = models.CharField(max_length=50, verbose_name='SEO-описание', null=True, blank=True)
    meta_title      = models.CharField(max_length=50, verbose_name='META title', null=True, blank=True)

class Category(SeoEmpoweredModel):
    title       = models.CharField(max_length=50, unique=True, verbose_name='Название')
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = u"Категория"
        verbose_name_plural = u"Категории"

class Memorial(SeoEmpoweredModel):
    photo1       = models.ImageField(upload_to='uploads/memorials', verbose_name='Изображение 1', null=True, blank=True)
    photo2       = models.ImageField(upload_to='uploads/memorials', verbose_name='Изображение 2', null=True, blank=True)
    number       = models.CharField(max_length=50, unique=True, verbose_name='Номер')
    title        = models.CharField(max_length=50, verbose_name='Заголовок')
    description  = models.TextField(verbose_name='Описание', null=True, blank=True)
    stella       = models.CharField(max_length=50, verbose_name='Стелла')
    podstavka    = models.CharField(max_length=50, verbose_name='Подставка')
    cvetnik      = models.CharField(max_length=50, verbose_name='Цветник')
    price_face   = models.BigIntegerField(verbose_name='Цена за лицевую полировку')
    price_circle = models.BigIntegerField(verbose_name='Цена за круговую полировку')
    categories   = models.ManyToManyField(Category)
    def admin_thumbnail(self):
        if self.photo1:
            return u'<img src="%s" height="100" width="100"/>' % (self.photo1.url)
        else:
            return 'нет изображения'
    admin_thumbnail.short_description = 'Изображение 1'
    admin_thumbnail.allow_tags = True
    def get_categories(self):
        return "<br>".join([s.title for s in self.categories.all()])
    get_categories.short_description = 'Категории'
    get_categories.allow_tags = True
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = u"Памятник"
        verbose_name_plural = u"Памятники"

class SeoArticle(models.Model):
    title       = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Текст', null=True, blank=True)
    memorial    = models.ForeignKey(Memorial, verbose_name='Мемориал', null=True, blank=True)
    category    = models.ForeignKey(Category, verbose_name='Категория', null=True, blank=True)
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = u"SEO статья"
        verbose_name_plural = u"SEO статьи"

class ReadyWork(models.Model):
    title       = models.CharField(max_length=50, verbose_name='Название')
    photo       = models.ImageField(upload_to='uploads/ready', verbose_name='Изображение', null=True, blank=True)
    memorial    = models.ForeignKey(Memorial, verbose_name='Мемориал', null=True, blank=True)
    def __unicode__(self):
        return self.title  
    class Meta:
        verbose_name = u"Готовая работа"
        verbose_name_plural = u"Готовые работы"

class StaticPage(SeoEmpoweredModel):
    title       = models.CharField(max_length=50, verbose_name='Название')
    slug        = models.CharField(max_length=255, verbose_name='URL')
    description = models.TextField(verbose_name='Текст', null=True, blank=True)
    def save(self, *args, **kwargs):
        # self.slug = uuslug(self.name, instance=self, separator="_") # optional non-dash separator
        self.slug = uuslug(self.title, instance=self)
        super(StaticPage, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = u"Страница"
        verbose_name_plural = u"Страницы"

class Order(models.Model):
    STATUS_CHOICES = (
        ('S', 'Отправлен'),
        ('D', 'Данные внесены'),
        ('P', 'Производство'),
        ('C', 'Заверешен'),
    )
    memorial     = models.ForeignKey(Memorial, verbose_name='Мемориал')
    email        = models.CharField(max_length=150, verbose_name='Email')
    calc_result  = models.TextField(verbose_name='Результат рассчётов', null=True, blank=True)
    user_phone   = models.CharField(max_length=150, verbose_name='Телефон', null=True, blank=True)
    user_name    = models.CharField(max_length=150, verbose_name='Фамилия, имя', null=True, blank=True)
    user_comment = models.TextField(max_length=150, verbose_name='Комментарий', null=True, blank=True)
    status       = models.CharField(max_length=1, choices=STATUS_CHOICES, default='S')
    pub_date     = models.DateTimeField('Дата оформления', default = datetime.now()) 
    def __unicode__(self):
        return self.id  
    class Meta:
        verbose_name = u"Заказа"
        verbose_name_plural = u"Заказы"