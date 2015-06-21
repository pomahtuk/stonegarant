# -*- coding: utf-8 -*-
from django.db import models
from datetime import *
import random
import uuid
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
    cvetnik = models.ForeignKey(Cvetnik, verbose_name='Цветник', null=True, blank=True)
    podstavka = models.ForeignKey(Podstavka, verbose_name='Подставка', null=True, blank=True)
    polirovka = models.ForeignKey(Polirovka, verbose_name='Полировка', null=True, blank=True)
    # email = models.CharField(max_length=150, verbose_name='Email', null=True, blank=True)
    # old fields
    calc_result = models.TextField(verbose_name='Результат рассчётов', null=True, blank=True)
    user_phone = models.CharField(max_length=150, verbose_name='Телефон', null=True, blank=True)
    user_name = models.CharField(max_length=150, verbose_name='Фамилия, имя', null=True, blank=True)
    user_comment = models.TextField(max_length=150, verbose_name='Комментарий пользователя', null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='N')
    pub_date = models.DateTimeField('Дата оформления', default=datetime.now())
    # new fields
    user_email = models.CharField(max_length=150, verbose_name='Email', null=True, blank=True)
    total_price = models.BigIntegerField(verbose_name='Итоговая цена заказа', null=True, blank=True)
    notes = models.TextField(verbose_name='Примечания', null=True, blank=True)
    # order_number
    # order_pin
    order_number = models.CharField(max_length=150, verbose_name='Номер заказа',
                                    unique=True)  # генерировать автоматически
    order_pin = models.CharField(max_length=150, verbose_name='ПИН-код')  # так же


    def formatted_price(self):
        return "{:,}".format(self.total_price).replace(',', ' ')

    # this has to ba based on user filling status
    def save(self, *args, **kwargs):
        if self.pk is not None:
            orig = Order.objects.get(pk=self.pk)
        if not self.order_number:
            # 0 - get total price
            total_price = self.memorial.base_price
            total_price += self.stella.added_value
            if self.cvetnik:
                total_price += self.cvetnik.added_value
            if self.podstavka:
                total_price += self.podstavka.added_value
            # this is tricky but still works fine
            total_price = int(total_price * (1 + ((self.polirovka.added_value + 0.0) / 100)))
            self.total_price = total_price
            # 1 - generate number and pin on creation
            # number generation could have some collisions but pretty safe
            self.order_number = str(uuid.uuid4())[:8]
            self.order_pin = random.randrange(10000, 99999)
            # 3 - update memorial popularity?
            self.memorial.popularity += 100
        if self.status == 'D' and orig.status != 'D' and self.user_email:
            print('trying to send an email')
            msg_plain = render_to_string('email/text/new_order.txt', {'order': self})
            msg_html = render_to_string('email/html/new_order.html', {'order': self})
            # use some real values
            send_mail(
                u'Новый заказ на сайте Stone-Garant.ru',
                msg_plain,
                'info@stone-garant.ru',
                [self.user_email, 'pman89@ya.ru', 'info@stone-garant.ru'],
                html_message=msg_html,
            )
        super(Order, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"%s" % self.order_number

    class Meta:
        verbose_name = u"Заказа"
        verbose_name_plural = u"Заказы"
