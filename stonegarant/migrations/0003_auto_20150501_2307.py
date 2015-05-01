# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('stonegarant', '0002_auto_20150501_1215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cvetnik',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(null=True, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
                ('size', models.TextField(null=True, verbose_name=b'\xd0\xa0\xd0\xb0\xd0\xb7\xd0\xbc\xd0\xb5\xd1\x80', blank=True)),
                ('added_value', models.BigIntegerField(default=0, null=True, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb4\xd0\xb1\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb0 \xd0\xba \xd0\xb1\xd0\xb0\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xb9 \xd1\x86\xd0\xb5\xd0\xbd\xd0\xb5', blank=True)),
            ],
            options={
                'verbose_name': '\u0412\u0430\u0440\u0438\u0430\u043d\u0442 \u0446\u0432\u0435\u0442\u043d\u0438\u043a\u0430',
                'verbose_name_plural': '\u0412\u0430\u0440\u0438\u0430\u043d\u0442\u044b \u0446\u0432\u0435\u0442\u043d\u0438\u043a\u043e\u0432',
            },
        ),
        migrations.CreateModel(
            name='Polirovka',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(null=True, verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf', blank=True)),
                ('added_value', models.BigIntegerField(default=0, null=True, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb4\xd0\xb1\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb0 \xd0\xba \xd0\xb1\xd0\xb0\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xb9 \xd1\x86\xd0\xb5\xd0\xbd\xd0\xb5', blank=True)),
            ],
            options={
                'verbose_name': '\u0412\u0430\u0440\u0438\u0430\u043d\u0442 \u043f\u043e\u043b\u0438\u0440\u043e\u0432\u043a\u0438',
                'verbose_name_plural': '\u0412\u0430\u0440\u0438\u0430\u043d\u0442\u044b \u043f\u043e\u043b\u0438\u0440\u043e\u0432\u043e\u043a',
            },
        ),
        migrations.CreateModel(
            name='Stella',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(null=True, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
                ('size', models.TextField(null=True, verbose_name=b'\xd0\xa0\xd0\xb0\xd0\xb7\xd0\xbc\xd0\xb5\xd1\x80', blank=True)),
                ('added_value', models.BigIntegerField(default=0, null=True, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb4\xd0\xb1\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb0 \xd0\xba \xd0\xb1\xd0\xb0\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xb9 \xd1\x86\xd0\xb5\xd0\xbd\xd0\xb5', blank=True)),
            ],
            options={
                'verbose_name': '\u0421\u0442\u044d\u043b\u043b\u0430',
                'verbose_name_plural': '\u0421\u0442\u044d\u043b\u043b\u044b',
            },
        ),
        migrations.AddField(
            model_name='memorial',
            name='base_price',
            field=models.BigIntegerField(null=True, verbose_name=b'\xd0\x91\xd0\xb0\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x8f \xd1\x86\xd0\xb5\xd0\xbd\xd0\xb0', blank=True),
        ),
        migrations.AddField(
            model_name='memorial',
            name='discount_percent',
            field=models.BigIntegerField(null=True, verbose_name=b'\xd0\xa1\xd0\xba\xd0\xb8\xd0\xb4\xd0\xba\xd0\xb0(\xd0\xbf\xd1\x80\xd0\xbe\xd1\x86\xd0\xb5\xd0\xbd\xd1\x82)', blank=True),
        ),
        migrations.AddField(
            model_name='memorial',
            name='discount_price',
            field=models.BigIntegerField(null=True, verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xb0 \xd1\x81\xd0\xbe \xd1\x81\xd0\xba\xd0\xb8\xd0\xb4\xd0\xba\xd0\xbe\xd0\xb9', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 1, 23, 7, 48, 836447), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbe\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AddField(
            model_name='memorial',
            name='cvetnik_variants',
            field=models.ManyToManyField(to='stonegarant.Cvetnik', verbose_name=b'\xd0\x92\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb0\xd0\xbd\xd1\x82\xd1\x8b \xd1\x86\xd0\xb2\xd0\xb5\xd1\x82\xd0\xbd\xd0\xb8\xd0\xba\xd0\xb0'),
        ),
        migrations.AddField(
            model_name='memorial',
            name='polirovka_variants',
            field=models.ManyToManyField(to='stonegarant.Polirovka', verbose_name=b'\xd0\x92\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb0\xd0\xbd\xd1\x82\xd1\x8b \xd0\xbf\xd0\xbe\xd0\xbb\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xb8'),
        ),
        migrations.AddField(
            model_name='memorial',
            name='stella_variants',
            field=models.ManyToManyField(to='stonegarant.Stella', verbose_name=b'\xd0\x92\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb0\xd0\xbd\xd1\x82\xd1\x8b \xd1\x81\xd1\x82\xd1\x8d\xd0\xbb\xd0\xbb\xd1\x8b'),
        ),
    ]
