# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('stonegarant_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('stonegarant', ['Category'])

        # Adding model 'Memorial'
        db.create_table('stonegarant_memorial', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photo1', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('photo2', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('number', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('stella', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('podstavka', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cvetnik', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stonegarant.Category'], null=True, blank=True)),
        ))
        db.send_create_signal('stonegarant', ['Memorial'])

        # Adding model 'SeoArticle'
        db.create_table('stonegarant_seoarticle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('memorial', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stonegarant.Memorial'], null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stonegarant.Category'], null=True, blank=True)),
        ))
        db.send_create_signal('stonegarant', ['SeoArticle'])

        # Adding model 'ReadyWork'
        db.create_table('stonegarant_readywork', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('memorial', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stonegarant.Memorial'], null=True, blank=True)),
        ))
        db.send_create_signal('stonegarant', ['ReadyWork'])

        # Adding model 'StaticPage'
        db.create_table('stonegarant_staticpage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('stonegarant', ['StaticPage'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('stonegarant_category')

        # Deleting model 'Memorial'
        db.delete_table('stonegarant_memorial')

        # Deleting model 'SeoArticle'
        db.delete_table('stonegarant_seoarticle')

        # Deleting model 'ReadyWork'
        db.delete_table('stonegarant_readywork')

        # Deleting model 'StaticPage'
        db.delete_table('stonegarant_staticpage')


    models = {
        'stonegarant.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'stonegarant.memorial': {
            'Meta': {'object_name': 'Memorial'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stonegarant.Category']", 'null': 'True', 'blank': 'True'}),
            'cvetnik': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'photo1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'podstavka': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'stella': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'stonegarant.readywork': {
            'Meta': {'object_name': 'ReadyWork'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'memorial': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stonegarant.Memorial']", 'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'stonegarant.seoarticle': {
            'Meta': {'object_name': 'SeoArticle'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stonegarant.Category']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'memorial': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stonegarant.Memorial']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'stonegarant.staticpage': {
            'Meta': {'object_name': 'StaticPage'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['stonegarant']