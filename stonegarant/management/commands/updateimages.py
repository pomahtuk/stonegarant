# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from stonegarant.models import *


class Command(BaseCommand):
    help = 'Migrates old stonegarant data to new one, in this case - images'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    def handle(self, *args, **options):
        all_memorials = Memorial.objects.all()
        for single_memorial in all_memorials:
            # update images
            try:
                current_file = single_memorial.photo1.file
                photo1 = AttachedImage(order=0)
                photo1.save()
                single_memorial.images.add(photo1)
                photo1.photo.save(current_file.name, current_file)
                current_file = single_memorial.photo2.file
                photo2 = AttachedImage(order=0)
                photo2.save()
                single_memorial.images.add(photo2)
                photo2.photo.save(current_file.name, current_file)
            except IOError:
                self.stdout.write('Not an image for memorial %s' % single_memorial.slug)
            finally:
                self.stdout.write('Successfully created photos for memorial %s' % single_memorial.slug)
        self.stdout.write('Successfully executed command')