# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from stonegarant.models import *


class Command(BaseCommand):
    help = 'Migrates old stonegarant data to new one'

    def __init__(self, *args, **kwargs):
        self.memorial = []
        self.stella = []
        super(Command, self).__init__(*args, **kwargs)

    def create_all_options(self):
        # each stella has 2 variants of cvetnik
        # and 2 variants of polirovka
        for x in range(0, 2):
            # getting names
            cvetnik_name = u'Цветник' if x is 0 else u'Плита'
            polirovka_name = u'Лицевая' if x is 0 else u'Круговая'
            # getting price
            polirovka_price = 0 if x is 0 else self.memorial.price_circle - self.memorial.base_price
            cvetnik = self.stella.cvetnik_set.create(
                title=cvetnik_name,
            )
            self.stdout.write('Created cvetnik(%s) for stella(%s)' % (cvetnik.pk, self.stella.pk))
            polirovka = self.stella.polirovka_set.create(
                title=polirovka_name,
                added_value=polirovka_price
            )
            self.stdout.write('Created polirovka(%s) for stella(%s)' % (polirovka.pk, self.stella.pk))
        # also stella has one podstavka
        podstavka = self.stella.podstavka_set.create(
            title=u'Подставка',
        )
        self.stdout.write('Created polirovka(%s) for stella(%s)' % (podstavka.pk, self.stella.pk))

    def create_stella_variants(self):
        # only one stella per memorial
        self.stella = self.memorial.stella_variants.create(
            title=u'Стэлла',
        )
        self.stdout.write('Successfully created stella for %s' % self.memorial.slug)
        self.create_all_options()

    def handle(self, *args, **options):
        all_memorials = Memorial.objects.all()
        for single_memorial in all_memorials:
            # updating base price
            self.memorial = single_memorial
            self.memorial.base_price = self.memorial.price_face
            self.memorial.discount_price = self.memorial.base_price
            self.stdout.write('%s/%s' % (self.memorial.discount_price,  self.memorial.base_price))
            self.create_stella_variants()
            # saving price update
            self.memorial.save()
        self.stdout.write('Successfully executed command')