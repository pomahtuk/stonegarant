# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('stonegarant', '0002_auto_20150504_2236'),
    ]

    operations = [
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
        migrations.AlterField(
            model_name='memorial',
            name='discount_percent',
            field=models.BigIntegerField(null=True, verbose_name=b'\xd0\xa1\xd0\xba\xd0\xb8\xd0\xb4\xd0\xba\xd0\xb0 (\xd0\xbf\xd1\x80\xd0\xbe\xd1\x86\xd0\xb5\xd0\xbd\xd1\x82)', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 5, 0, 20, 30, 915377), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbe\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AddField(
            model_name='memorial',
            name='granit',
            field=models.ForeignKey(verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf \xd0\xb3\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x82\xd0\xb0', to='stonegarant.Granit', null=True),
        ),
    ]
