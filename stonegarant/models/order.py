# -*- coding: utf-8 -*-
from django.db import models
from datetime import *
import random
from django.core.mail import send_mail
from django.template.loader import render_to_string


from memorial import Memorial
from stella import Stella
from cvetnik import Cvetnik
from podstavka import Podstavka
from polirovka import Polirovka


class Order(models.Model):
    STATUS_CHOICES = (
        ('N', 'Новый'),
        ('S', 'Отправлен'),
        ('D', 'Данные внесены'),
        ('P', 'Производство'),
        ('C', 'Заверешен'),
        ('R', 'Доставлен')
    )
    memorial = models.ForeignKey(Memorial, verbose_name='Мемориал')
    # new references
    stella = models.ForeignKey(Stella, verbose_name='Стэлла')
    cvetnik = models.ForeignKey(Cvetnik, verbose_name='Цветник')
    podstavka = models.ForeignKey(Podstavka, verbose_name='Подставка')
    polirovka = models.ForeignKey(Polirovka, verbose_name='Полировка')
    email = models.CharField(max_length=150, verbose_name='Email')
    # old fields
    calc_result = models.TextField(verbose_name='Результат рассчётов', null=True, blank=True)
    user_phone = models.CharField(max_length=150, verbose_name='Телефон', null=True, blank=True)
    user_name = models.CharField(max_length=150, verbose_name='Фамилия, имя', null=True, blank=True)
    user_comment = models.TextField(max_length=150, verbose_name='Комментарий пользователя', null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='N')
    pub_date = models.DateTimeField('Дата оформления', default=datetime.now())
    # new fields
    user_email = models.CharField(max_length=150, verbose_name='Email', null=True, blank=True)
    total_price = models.BigIntegerField(verbose_name='Итоговая цена заказа')
    notes = models.TextField(verbose_name='Примечания', null=True, blank=True)
    # order_number
    # order_pin
    order_number = models.CharField(max_length=150, verbose_name='Номер заказа',
                                    unique=True)  # генерировать автоматически
    order_pin = models.CharField(max_length=150, verbose_name='ПИН-код')  # так же

    def save(self, *args, **kwargs):
        if not self.order_number:
            # 1 - generate number and pin on creation
            self.order_number = u'%s%s%s%s%s' % (
                self.memorial.number,
                self.stella.pk,
                self.podstavka.pk,
                self.polirovka.pk,
                self.pub_date  # may be better use self pk if not empty? щеру
            )
            self.order_pin = random.randrange(10000, 99999)
            # 3 - update memorial popularity?
            self.memorial.popularity += 100
            # 2 - send email on creation - отправлять руками
            msg_plain = render_to_string('email/text/new_order.txt', {'some_params': 1})
            msg_html = render_to_string('email/html/new_order.html', {'some_params': 2})
            # use some real values
            send_mail(
                u'Новый заказ на сайте Stone-Garant.ru',
                msg_plain,
                'no-reply@example.com',
                [self.user_email, ],
                html_message=msg_html,
            )
        super(Order, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.id

    class Meta:
        verbose_name = u"Заказа"
        verbose_name_plural = u"Заказы"
