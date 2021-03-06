# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0003_auto_20160518_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='footerbanner',
            name='link',
            field=models.CharField(default=b'/page-aktsii-i-skidki', max_length=255, verbose_name=b'\xd1\x81\xd1\x81\xd1\x8b\xd0\xbb\xd0\xba\xd0\xb0'),
        ),
        migrations.AddField(
            model_name='footerbanner',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to=b'/catalog/banners/', verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5'),
        ),
        migrations.AddField(
            model_name='footerbanner',
            name='text',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=b'\xd0\x90\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb5\xd1\x80\xd0\xbd\xd0\xb0\xd1\x82\xd0\xb8\xd0\xbd\xd0\xb2\xd1\x8b\xd0\xb9 \xd1\x82\xd0\xb5\xd0\xba\xd1\x81\xd1\x82'),
        ),
    ]
