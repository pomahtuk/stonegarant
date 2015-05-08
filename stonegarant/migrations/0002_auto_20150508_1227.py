# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import stonegarant.models.attached_image
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stonegarant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttachedImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x80\xd1\x8f\xd0\xb4\xd0\xbe\xd0\xba')),
                ('photo', easy_thumbnails.fields.ThumbnailerImageField(upload_to=stonegarant.models.attached_image.upload_path_handler, verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5')),
            ],
            options={
                'verbose_name': '\u041f\u0440\u0438\u043a\u0440\u0435\u043f\u043b\u0435\u043d\u043d\u043e\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u041f\u0440\u0438\u043a\u0440\u0435\u043f\u043b\u0435\u043d\u043d\u044b\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f',
            },
        ),
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
            name='Granit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, null=True, verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf', blank=True)),
            ],
            options={
                'verbose_name': '\u0422\u0438\u043f \u0433\u0440\u0430\u043d\u0438\u0442\u0430',
                'verbose_name_plural': '\u0422\u0438\u043f\u044b \u0433\u0440\u0430\u043d\u0438\u0442\u0430',
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
            field=models.BigIntegerField(null=True, verbose_name=b'\xd0\xa1\xd0\xba\xd0\xb8\xd0\xb4\xd0\xba\xd0\xb0 (\xd0\xbf\xd1\x80\xd0\xbe\xd1\x86\xd0\xb5\xd0\xbd\xd1\x82)', blank=True),
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
            model_name='order',
            name='notes',
            field=models.TextField(null=True, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xbc\xd0\xb5\xd1\x87\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f', blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.CharField(default=1, unique=True, max_length=150, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xb7\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='order_pin',
            field=models.CharField(default=1, max_length=150, verbose_name=b'\xd0\x9f\xd0\x98\xd0\x9d-\xd0\xba\xd0\xbe\xd0\xb4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.BigIntegerField(default=1, verbose_name=b'\xd0\x98\xd1\x82\xd0\xbe\xd0\xb3\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x8f \xd1\x86\xd0\xb5\xd0\xbd\xd0\xb0 \xd0\xb7\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='user_email',
            field=models.CharField(max_length=150, null=True, verbose_name=b'Email', blank=True),
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
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 8, 12, 27, 19, 209163), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbe\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default=b'N', max_length=1, choices=[(b'N', b'\xd0\x9d\xd0\xbe\xd0\xb2\xd1\x8b\xd0\xb9'), (b'S', b'\xd0\x9e\xd1\x82\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd'), (b'D', b'\xd0\x94\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xb2\xd0\xbd\xd0\xb5\xd1\x81\xd0\xb5\xd0\xbd\xd1\x8b'), (b'P', b'\xd0\x9f\xd1\x80\xd0\xbe\xd0\xb8\xd0\xb7\xd0\xb2\xd0\xbe\xd0\xb4\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe'), (b'C', b'\xd0\x97\xd0\xb0\xd0\xb2\xd0\xb5\xd1\x80\xd0\xb5\xd1\x88\xd0\xb5\xd0\xbd'), (b'R', b'\xd0\x94\xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd')]),
        ),
        migrations.AlterField(
            model_name='order',
            name='user_comment',
            field=models.TextField(max_length=150, null=True, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbc\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb9 \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8f', blank=True),
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
            name='stella',
            field=models.ForeignKey(verbose_name=b'\xd0\xa1\xd1\x82\xd1\x8d\xd0\xbb\xd0\xbb\xd0\xb0', blank=True, to='stonegarant.Stella', null=True),
        ),
        migrations.AddField(
            model_name='podstavka',
            name='stella',
            field=models.ForeignKey(verbose_name=b'\xd0\xa1\xd1\x82\xd1\x8d\xd0\xbb\xd0\xbb\xd0\xb0', to='stonegarant.Stella', null=True),
        ),
        migrations.AddField(
            model_name='cvetnik',
            name='stella',
            field=models.ForeignKey(verbose_name=b'\xd0\xa1\xd1\x82\xd1\x8d\xd0\xbb\xd0\xbb\xd0\xb0', to='stonegarant.Stella', null=True),
        ),
        migrations.AddField(
            model_name='attachedimage',
            name='memorial',
            field=models.ForeignKey(related_name='images', verbose_name=b'\xd0\x9c\xd0\xb5\xd0\xbc\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb0\xd0\xbb', blank=True, to='stonegarant.Memorial', null=True),
        ),
        migrations.AddField(
            model_name='memorial',
            name='granit',
            field=models.ForeignKey(verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf \xd0\xb3\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x82\xd0\xb0', blank=True, to='stonegarant.Granit', null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='cvetnik',
            field=models.ForeignKey(default=1, verbose_name=b'\xd0\xa6\xd0\xb2\xd0\xb5\xd1\x82\xd0\xbd\xd0\xb8\xd0\xba', to='stonegarant.Cvetnik'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='podstavka',
            field=models.ForeignKey(default=1, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xb4\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb0', to='stonegarant.Podstavka'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='polirovka',
            field=models.ForeignKey(default=1, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xb0', to='stonegarant.Polirovka'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='stella',
            field=models.ForeignKey(default=1, verbose_name=b'\xd0\xa1\xd1\x82\xd1\x8d\xd0\xbb\xd0\xbb\xd0\xb0', to='stonegarant.Stella'),
            preserve_default=False,
        ),
    ]
