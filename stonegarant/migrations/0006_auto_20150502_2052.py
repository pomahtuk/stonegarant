# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('stonegarant', '0005_auto_20150502_0120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Podstavka',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(null=True, verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf', blank=True)),
                ('width', models.BigIntegerField(default=0, verbose_name=b'\xd0\xa8\xd0\xb8\xd1\x80\xd0\xb8\xd0\xbd\xd0\xb0, \xd1\x81\xd0\xbc')),
                ('height', models.BigIntegerField(default=0, verbose_name=b'\xd0\x92\xd1\x8b\xd1\x81\xd0\xbe\xd1\x82\xd0\xb0, \xd1\x81\xd0\xbc')),
                ('length', models.BigIntegerField(default=0, verbose_name=b'\xd0\x94\xd0\xbb\xd0\xb8\xd0\xbd\xd0\xb0, \xd1\x81\xd0\xbc')),
                ('added_value', models.BigIntegerField(default=0, null=True, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb4\xd0\xb1\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb0 \xd0\xba \xd0\xb1\xd0\xb0\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xb9 \xd1\x86\xd0\xb5\xd0\xbd\xd0\xb5', blank=True)),
            ],
            options={
                'verbose_name': '\u0412\u0430\u0440\u0438\u0430\u043d\u0442 \u043f\u043e\u0434\u0441\u0442\u0430\u0432\u043a\u0438',
                'verbose_name_plural': '\u0412\u0430\u0440\u0438\u0430\u043d\u0442\u044b \u043f\u043e\u0434\u0441\u0442\u0430\u0432\u043e\u043a',
            },
        ),
        migrations.RemoveField(
            model_name='cvetnik',
            name='size',
        ),
        migrations.RemoveField(
            model_name='memorial',
            name='cvetnik_variants',
        ),
        migrations.RemoveField(
            model_name='memorial',
            name='polirovka_variants',
        ),
        migrations.AddField(
            model_name='cvetnik',
            name='height',
            field=models.BigIntegerField(default=0, verbose_name=b'\xd0\x92\xd1\x8b\xd1\x81\xd0\xbe\xd1\x82\xd0\xb0, \xd1\x81\xd0\xbc'),
        ),
        migrations.AddField(
            model_name='cvetnik',
            name='length',
            field=models.BigIntegerField(default=0, verbose_name=b'\xd0\x94\xd0\xbb\xd0\xb8\xd0\xbd\xd0\xb0, \xd1\x81\xd0\xbc'),
        ),
        migrations.AddField(
            model_name='cvetnik',
            name='memorial',
            field=models.ForeignKey(related_name='cvetnik_variants', verbose_name=b'\xd0\x9c\xd0\xb5\xd0\xbc\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb0\xd0\xbb', blank=True, to='stonegarant.Memorial', null=True),
        ),
        migrations.AddField(
            model_name='cvetnik',
            name='width',
            field=models.BigIntegerField(default=0, verbose_name=b'\xd0\xa8\xd0\xb8\xd1\x80\xd0\xb8\xd0\xbd\xd0\xb0, \xd1\x81\xd0\xbc'),
        ),
        migrations.AddField(
            model_name='memorial',
            name='popularity',
            field=models.BigIntegerField(default=0, null=True, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbf\xd1\x83\xd0\xbb\xd1\x8f\xd1\x80\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c', blank=True),
        ),
        migrations.AddField(
            model_name='polirovka',
            name='memorial',
            field=models.ForeignKey(related_name='polirovka_variants', verbose_name=b'\xd0\x9c\xd0\xb5\xd0\xbc\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb0\xd0\xbb', to='stonegarant.Memorial', null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 2, 20, 52, 23, 913447), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbe\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='stella',
            name='height',
            field=models.BigIntegerField(default=0, verbose_name=b'\xd0\x92\xd1\x8b\xd1\x81\xd0\xbe\xd1\x82\xd0\xb0, \xd1\x81\xd0\xbc'),
        ),
        migrations.AlterField(
            model_name='stella',
            name='length',
            field=models.BigIntegerField(default=0, verbose_name=b'\xd0\x94\xd0\xbb\xd0\xb8\xd0\xbd\xd0\xb0, \xd1\x81\xd0\xbc'),
        ),
        migrations.AlterField(
            model_name='stella',
            name='width',
            field=models.BigIntegerField(default=0, verbose_name=b'\xd0\xa8\xd0\xb8\xd1\x80\xd0\xb8\xd0\xbd\xd0\xb0, \xd1\x81\xd0\xbc'),
        ),
        migrations.AddField(
            model_name='podstavka',
            name='memorial',
            field=models.ForeignKey(related_name='podstavka_variants', verbose_name=b'\xd0\x9c\xd0\xb5\xd0\xbc\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb0\xd0\xbb', blank=True, to='stonegarant.Memorial', null=True),
        ),
    ]
