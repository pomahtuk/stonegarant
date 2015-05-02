# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('stonegarant', '0006_auto_20150502_2052'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stella',
            options={'verbose_name': '\u0412\u0430\u0440\u0438\u0430\u043d\u0442 \u0441\u0442\u044d\u043b\u043b\u044b', 'verbose_name_plural': '\u0412\u0430\u0440\u0438\u0430\u043d\u0442\u044b \u0441\u0442\u044d\u043b\u043b\u044b'},
        ),
        migrations.AlterField(
            model_name='cvetnik',
            name='title',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 3, 0, 48, 0, 357435), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbe\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='podstavka',
            name='title',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf', blank=True),
        ),
        migrations.AlterField(
            model_name='polirovka',
            name='title',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf', blank=True),
        ),
    ]
