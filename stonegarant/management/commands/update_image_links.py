# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from stonegarant.models import *


class Command(BaseCommand):
    help = 'Updates image url for memorials to support https'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    def handle(self, *args, **options):
        all_memorials = Memorial.objects.all()
        for single_memorial in all_memorials:
            old_link = single_memorial.catalog_thumb
            new_link = old_link[5:]
            print old_link, '==>', new_link
            # single_memorial.catalog_thumb
            single_memorial.catalog_thumb = new_link
            single_memorial.save()
