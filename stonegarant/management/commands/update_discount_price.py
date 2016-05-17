# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from stonegarant.models import *


class Command(BaseCommand):
    help = 'Updates discount_price for memorials'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    def handle(self, *args, **options):
        all_memorials = Memorial.objects.all()
        for single_memorial in all_memorials:
            if not single_memorial.discount_price:
                single_memorial.discount_price = single_memorial.base_price
                single_memorial.save()
