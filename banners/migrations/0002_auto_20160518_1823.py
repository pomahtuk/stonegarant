# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogbanner',
            name='active',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\x90\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd1\x8b\xd0\xb9'),
        ),
        migrations.AlterField(
            model_name='catalogbanner',
            name='contents',
            field=models.TextField(blank=True, null=True, verbose_name=b'\xd0\xa1\xd0\xbe\xd0\xb4\xd0\xb5\xd1\x80\xd0\xb6\xd0\xb8\xd0\xbc\xd0\xbe\xd0\xb5'),
        ),
        migrations.AlterField(
            model_name='footerbanner',
            name='active',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\x90\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd1\x8b\xd0\xb9'),
        ),
        migrations.AlterField(
            model_name='footerbanner',
            name='contents',
            field=models.TextField(blank=True, null=True, verbose_name=b'\xd0\xa1\xd0\xbe\xd0\xb4\xd0\xb5\xd1\x80\xd0\xb6\xd0\xb8\xd0\xbc\xd0\xbe\xd0\xb5'),
        ),
    ]
