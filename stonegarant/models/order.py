# -*- coding: utf-8 -*-
from django.db import models

from memorial import *

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
