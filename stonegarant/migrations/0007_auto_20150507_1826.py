# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import stonegarant.models.attached_image
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stonegarant', '0006_auto_20150506_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttachedImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField()),
                ('photo', easy_thumbnails.fields.ThumbnailerImageField(upload_to=stonegarant.models.attached_image.upload_path_handler, verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5')),
            ],
        ),
        migrations.RemoveField(
            model_name='memorial',
            name='photo3',
        ),
        migrations.AlterField(
            model_name='order',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 7, 18, 26, 13, 121631), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbe\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AddField(
            model_name='attachedimage',
            name='memorial',
            field=models.ForeignKey(related_name='images', verbose_name=b'\xd0\x9c\xd0\xb5\xd0\xbc\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb0\xd0\xbb', blank=True, to='stonegarant.Memorial', null=True),
        ),
    ]
