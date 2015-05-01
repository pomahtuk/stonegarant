# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=150, verbose_name=b'Email')),
                ('calc_result', models.TextField(null=True, verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xb7\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb0\xd1\x82 \xd1\x80\xd0\xb0\xd1\x81\xd1\x81\xd1\x87\xd1\x91\xd1\x82\xd0\xbe\xd0\xb2', blank=True)),
                ('user_phone', models.CharField(max_length=150, null=True, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd', blank=True)),
                ('user_name', models.CharField(max_length=150, null=True, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f, \xd0\xb8\xd0\xbc\xd1\x8f', blank=True)),
                ('user_comment', models.TextField(max_length=150, null=True, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbc\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb9', blank=True)),
                ('status', models.CharField(default=b'S', max_length=1, choices=[(b'S', b'\xd0\x9e\xd1\x82\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd'), (b'D', b'\xd0\x94\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xb2\xd0\xbd\xd0\xb5\xd1\x81\xd0\xb5\xd0\xbd\xd1\x8b'), (b'P', b'\xd0\x9f\xd1\x80\xd0\xbe\xd0\xb8\xd0\xb7\xd0\xb2\xd0\xbe\xd0\xb4\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe'), (b'C', b'\xd0\x97\xd0\xb0\xd0\xb2\xd0\xb5\xd1\x80\xd0\xb5\xd1\x88\xd0\xb5\xd0\xbd')])),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2015, 5, 1, 12, 15, 29, 50960), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbe\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
            ],
            options={
                'verbose_name': '\u0417\u0430\u043a\u0430\u0437\u0430',
                'verbose_name_plural': '\u0417\u0430\u043a\u0430\u0437\u044b',
            },
        ),
        migrations.CreateModel(
            name='ReadyWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('photo', models.ImageField(upload_to=b'uploads/ready', null=True, verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
                ('description', models.TextField(null=True, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82', blank=True)),
                ('pub_date', models.DateTimeField()),
            ],
            options={
                'verbose_name': '\u0413\u043e\u0442\u043e\u0432\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430',
                'verbose_name_plural': '\u0413\u043e\u0442\u043e\u0432\u044b\u0435 \u0440\u0430\u0431\u043e\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reply', models.TextField(null=True, verbose_name=b'\xd0\x9e\xd1\x82\xd0\xb7\xd1\x8b\xd0\xb2', blank=True)),
                ('person', models.CharField(max_length=50, null=True, verbose_name=b'\xd0\xa7\xd0\xb5\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xb5\xd0\xba', blank=True)),
            ],
            options={
                'verbose_name': '\u041e\u0442\u0437\u044b\u0432',
                'verbose_name_plural': '\u041e\u0442\u0437\u044b\u0432\u044b',
            },
        ),
        migrations.CreateModel(
            name='SeoArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('description', models.TextField(null=True, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82', blank=True)),
            ],
            options={
                'verbose_name': 'SEO \u0441\u0442\u0430\u0442\u044c\u044f',
                'verbose_name_plural': 'SEO \u0441\u0442\u0430\u0442\u044c\u0438',
            },
        ),
        migrations.CreateModel(
            name='SeoEmpoweredModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seo_keywords', models.CharField(max_length=300, null=True, verbose_name=b'\xd0\x9a\xd0\xbb\xd1\x8e\xd1\x87\xd0\xb5\xd0\xb2\xd1\x8b\xd0\xb5 \xd1\x81\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xb0', blank=True)),
                ('seo_description', models.CharField(max_length=300, null=True, verbose_name=b'SEO-\xd0\xbe\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
                ('meta_title', models.CharField(max_length=300, null=True, verbose_name=b'META title', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('seoempoweredmodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='stonegarant.SeoEmpoweredModel')),
                ('title', models.CharField(unique=True, max_length=50, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('slug', models.CharField(max_length=255, verbose_name=b'URL')),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0430\u0440\u0430\u044f \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u0421\u0442\u0430\u0440\u044b\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
            bases=('stonegarant.seoempoweredmodel',),
        ),
        migrations.CreateModel(
            name='Memorial',
            fields=[
                ('seoempoweredmodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='stonegarant.SeoEmpoweredModel')),
                ('photo1', models.ImageField(upload_to=b'uploads/memorials', null=True, verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 1', blank=True)),
                ('photo2', models.ImageField(upload_to=b'uploads/memorials', null=True, verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 2', blank=True)),
                ('number', models.BigIntegerField(unique=True, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80')),
                ('title', models.CharField(max_length=50, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb3\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xba')),
                ('slug', models.CharField(max_length=255, verbose_name=b'URL')),
                ('description', models.TextField(null=True, verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
                ('stella', models.CharField(max_length=50, verbose_name=b'\xd0\xa1\xd1\x82\xd0\xb5\xd0\xbb\xd0\xbb\xd0\xb0')),
                ('podstavka', models.CharField(max_length=50, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xb4\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xba\xd0\xb0')),
                ('cvetnik', models.CharField(max_length=50, verbose_name=b'\xd0\xa6\xd0\xb2\xd0\xb5\xd1\x82\xd0\xbd\xd0\xb8\xd0\xba')),
                ('price_face', models.BigIntegerField(verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xb0 \xd0\xb7\xd0\xb0 \xd0\xbb\xd0\xb8\xd1\x86\xd0\xb5\xd0\xb2\xd1\x83\xd1\x8e \xd0\xbf\xd0\xbe\xd0\xbb\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd1\x83')),
                ('price_circle', models.BigIntegerField(verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xb0 \xd0\xb7\xd0\xb0 \xd0\xba\xd1\x80\xd1\x83\xd0\xb3\xd0\xbe\xd0\xb2\xd1\x83\xd1\x8e \xd0\xbf\xd0\xbe\xd0\xbb\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd1\x83')),
                ('categories', models.ManyToManyField(to='stonegarant.Category', verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb8')),
            ],
            options={
                'verbose_name': '\u041f\u0430\u043c\u044f\u0442\u043d\u0438\u043a',
                'verbose_name_plural': '\u041f\u0430\u043c\u044f\u0442\u043d\u0438\u043a\u0438',
            },
            bases=('stonegarant.seoempoweredmodel',),
        ),
        migrations.CreateModel(
            name='ServicePage',
            fields=[
                ('seoempoweredmodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='stonegarant.SeoEmpoweredModel')),
                ('title', models.CharField(max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('description', models.TextField(null=True, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82', blank=True)),
            ],
            options={
                'verbose_name': '\u0421\u043b\u0443\u0436\u0435\u0431\u043d\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430',
                'verbose_name_plural': '\u0421\u043b\u0443\u0436\u0435\u0431\u043d\u044b\u0435 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b',
            },
            bases=('stonegarant.seoempoweredmodel',),
        ),
        migrations.CreateModel(
            name='StaticPage',
            fields=[
                ('seoempoweredmodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='stonegarant.SeoEmpoweredModel')),
                ('title', models.CharField(max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('slug', models.CharField(max_length=255, verbose_name=b'URL')),
                ('short', models.TextField(null=True, verbose_name=b'\xd0\x9a\xd0\xbe\xd1\x80\xd0\xbe\xd1\x82\xd0\xba\xd0\xbe\xd0\xb5 \xd0\xbf\xd0\xbe\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
                ('description', models.TextField(null=True, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82', blank=True)),
                ('show_in_list', models.BooleanField(default=False, verbose_name=b'\xd0\xa1\xd1\x82\xd0\xb0\xd1\x82\xd1\x8c\xd1\x8f?')),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430',
                'verbose_name_plural': '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u044b',
            },
            bases=('stonegarant.seoempoweredmodel',),
        ),
        migrations.AddField(
            model_name='seoarticle',
            name='category',
            field=models.ForeignKey(verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', blank=True, to='stonegarant.Category', null=True),
        ),
        migrations.AddField(
            model_name='seoarticle',
            name='memorial',
            field=models.ForeignKey(verbose_name=b'\xd0\x9c\xd0\xb5\xd0\xbc\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb0\xd0\xbb', blank=True, to='stonegarant.Memorial', null=True),
        ),
        migrations.AddField(
            model_name='readywork',
            name='memorial',
            field=models.ForeignKey(verbose_name=b'\xd0\x9c\xd0\xb5\xd0\xbc\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb0\xd0\xbb', blank=True, to='stonegarant.Memorial', null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='memorial',
            field=models.ForeignKey(verbose_name=b'\xd0\x9c\xd0\xb5\xd0\xbc\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb0\xd0\xbb', to='stonegarant.Memorial'),
        ),
    ]
