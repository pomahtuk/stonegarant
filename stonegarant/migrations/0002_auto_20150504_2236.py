# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stonegarant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cvetnik',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, null=True, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
                ('length', models.BigIntegerField(default=0, verbose_name=b'\xd0\x94\xd0\xbb\xd0\xb8\xd0\xbd\xd0\xb0, \xd1\x81\xd0\xbc')),
                ('width', models.BigIntegerField(default=0, verbose_name=b'\xd0\xa8\xd0\xb8\xd1\x80\xd0\xb8\xd0\xbd\xd0\xb0, \xd1\x81\xd0\xbc')),
                ('height', models.BigIntegerField(default=0, verbose_name=b'\xd0\x92\xd1\x8b\xd1\x81\xd0\xbe\xd1\x82\xd0\xb0, \xd1\x81\xd0\xbc')),
                ('added_value', models.BigIntegerField(default=0, null=True, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb4\xd0\xb1\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb0 \xd0\xba \xd0\xb1\xd0\xb0\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xb9 \xd1\x86\xd0\xb5\xd0\xbd\xd0\xb5', blank=True)),
            ],
            options={
                'verbose_name': '\u0412\u0430\u0440\u0438\u0430\u043d\u0442 \u0446\u0432\u0435\u0442\u043d\u0438\u043a\u0430',
                'verbose_name_plural': '\u0412\u0430\u0440\u0438\u0430\u043d\u0442\u044b \u0446\u0432\u0435\u0442\u043d\u0438\u043a\u043e\u0432',
            },
        ),
        migrations.CreateModel(
            name='Podstavka',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, null=True, verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf', blank=True)),
                ('length', models.BigIntegerField(default=0, verbose_name=b'\xd0\x94\xd0\xbb\xd0\xb8\xd0\xbd\xd0\xb0, \xd1\x81\xd0\xbc')),
                ('width', models.BigIntegerField(default=0, verbose_name=b'\xd0\xa8\xd0\xb8\xd1\x80\xd0\xb8\xd0\xbd\xd0\xb0, \xd1\x81\xd0\xbc')),
                ('height', models.BigIntegerField(default=0, verbose_name=b'\xd0\x92\xd1\x8b\xd1\x81\xd0\xbe\xd1\x82\xd0\xb0, \xd1\x81\xd0\xbc')),
                ('added_value', models.BigIntegerField(default=0, null=True, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb4\xd0\xb1\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb0 \xd0\xba \xd0\xb1\xd0\xb0\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xb9 \xd1\x86\xd0\xb5\xd0\xbd\xd0\xb5', blank=True)),
            ],
            options={
                'verbose_name': '\u0412\u0430\u0440\u0438\u0430\u043d\u0442 \u043f\u043e\u0434\u0441\u0442\u0430\u0432\u043a\u0438',
                'verbose_name_plural': '\u0412\u0430\u0440\u0438\u0430\u043d\u0442\u044b \u043f\u043e\u0434\u0441\u0442\u0430\u0432\u043e\u043a',
            },
        ),
        migrations.CreateModel(
            name='Polirovka',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, null=True, verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf', blank=True)),
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
                ('title', models.CharField(max_length=50, null=True, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
                ('length', models.BigIntegerField(default=0, verbose_name=b'\xd0\x94\xd0\xbb\xd0\xb8\xd0\xbd\xd0\xb0, \xd1\x81\xd0\xbc')),
                ('width', models.BigIntegerField(default=0, verbose_name=b'\xd0\xa8\xd0\xb8\xd1\x80\xd0\xb8\xd0\xbd\xd0\xb0, \xd1\x81\xd0\xbc')),
                ('height', models.BigIntegerField(default=0, verbose_name=b'\xd0\x92\xd1\x8b\xd1\x81\xd0\xbe\xd1\x82\xd0\xb0, \xd1\x81\xd0\xbc')),
                ('added_value', models.BigIntegerField(default=0, null=True, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb4\xd0\xb1\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb0 \xd0\xba \xd0\xb1\xd0\xb0\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xb9 \xd1\x86\xd0\xb5\xd0\xbd\xd0\xb5', blank=True)),
            ],
            options={
                'verbose_name': '\u0412\u0430\u0440\u0438\u0430\u043d\u0442 \u0441\u0442\u044d\u043b\u043b\u044b',
                'verbose_name_plural': '\u0412\u0430\u0440\u0438\u0430\u043d\u0442\u044b \u0441\u0442\u044d\u043b\u043b\u044b',
            },
        ),
        migrations.AddField(
            model_name='memorial',
            name='admin_thumb',
            field=easy_thumbnails.fields.ThumbnailerImageField(null=True, upload_to=b'uploads/memorials', blank=True),
        ),
        migrations.AddField(
            model_name='memorial',
            name='base_price',
            field=models.BigIntegerField(null=True, verbose_name=b'\xd0\x91\xd0\xb0\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x8f \xd1\x86\xd0\xb5\xd0\xbd\xd0\xb0', blank=True),
        ),
        migrations.AddField(
            model_name='memorial',
            name='discount',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\xa1\xd0\xbe \xd1\x81\xd0\xba\xd0\xb8\xd0\xb4\xd0\xba\xd0\xbe\xd0\xb9'),
            preserve_default=False,
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
        migrations.AddField(
            model_name='memorial',
            name='popularity',
            field=models.BigIntegerField(default=0, null=True, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbf\xd1\x83\xd0\xbb\xd1\x8f\xd1\x80\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c', blank=True),
        ),
        migrations.AddField(
            model_name='readywork',
            name='admin_thumb',
            field=easy_thumbnails.fields.ThumbnailerImageField(null=True, upload_to=b'uploads/ready', blank=True),
        ),
        migrations.AlterField(
            model_name='memorial',
            name='photo1',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'uploads/memorials', null=True, verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 1', blank=True),
        ),
        migrations.AlterField(
            model_name='memorial',
            name='photo2',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'uploads/memorials', null=True, verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 2', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 4, 22, 36, 36, 162407), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbe\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='readywork',
            name='photo',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'uploads/ready', null=True, verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
        ),
        migrations.AddField(
            model_name='stella',
            name='memorial',
            field=models.ForeignKey(related_name='stella_variants', verbose_name=b'\xd0\x9c\xd0\xb5\xd0\xbc\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb0\xd0\xbb', blank=True, to='stonegarant.Memorial', null=True),
        ),
        migrations.AddField(
            model_name='polirovka',
            name='memorial',
            field=models.ForeignKey(related_name='polirovka_variants', verbose_name=b'\xd0\x9c\xd0\xb5\xd0\xbc\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb0\xd0\xbb', to='stonegarant.Memorial', null=True),
        ),
        migrations.AddField(
            model_name='podstavka',
            name='memorial',
            field=models.ForeignKey(related_name='podstavka_variants', verbose_name=b'\xd0\x9c\xd0\xb5\xd0\xbc\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb0\xd0\xbb', blank=True, to='stonegarant.Memorial', null=True),
        ),
        migrations.AddField(
            model_name='cvetnik',
            name='memorial',
            field=models.ForeignKey(related_name='cvetnik_variants', verbose_name=b'\xd0\x9c\xd0\xb5\xd0\xbc\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb0\xd0\xbb', blank=True, to='stonegarant.Memorial', null=True),
        ),
    ]
