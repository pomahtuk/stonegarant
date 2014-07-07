# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SeoEmpoweredModel'
        db.create_table('stonegarant_seoempoweredmodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seo_keywords', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('seo_description', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('meta_title', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('stonegarant', ['SeoEmpoweredModel'])

        # Deleting field 'Category.id'
        db.delete_column('stonegarant_category', 'id')

        # Adding field 'Category.seoempoweredmodel_ptr'
        db.add_column('stonegarant_category', 'seoempoweredmodel_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['stonegarant.SeoEmpoweredModel'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'Memorial.id'
        db.delete_column('stonegarant_memorial', 'id')

        # Adding field 'Memorial.seoempoweredmodel_ptr'
        db.add_column('stonegarant_memorial', 'seoempoweredmodel_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['stonegarant.SeoEmpoweredModel'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'StaticPage.id'
        db.delete_column('stonegarant_staticpage', 'id')

        # Adding field 'StaticPage.seoempoweredmodel_ptr'
        db.add_column('stonegarant_staticpage', 'seoempoweredmodel_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['stonegarant.SeoEmpoweredModel'], unique=True, primary_key=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'SeoEmpoweredModel'
        db.delete_table('stonegarant_seoempoweredmodel')

        # Adding field 'Category.id'
        db.add_column('stonegarant_category', 'id',
                      self.gf('django.db.models.fields.AutoField')(default='', primary_key=True),
                      keep_default=False)

        # Deleting field 'Category.seoempoweredmodel_ptr'
        db.delete_column('stonegarant_category', 'seoempoweredmodel_ptr_id')

        # Adding field 'Memorial.id'
        db.add_column('stonegarant_memorial', 'id',
                      self.gf('django.db.models.fields.AutoField')(default=1, primary_key=True),
                      keep_default=False)

        # Deleting field 'Memorial.seoempoweredmodel_ptr'
        db.delete_column('stonegarant_memorial', 'seoempoweredmodel_ptr_id')

        # Adding field 'StaticPage.id'
        db.add_column('stonegarant_staticpage', 'id',
                      self.gf('django.db.models.fields.AutoField')(default=1, primary_key=True),
                      keep_default=False)

        # Deleting field 'StaticPage.seoempoweredmodel_ptr'
        db.delete_column('stonegarant_staticpage', 'seoempoweredmodel_ptr_id')


    models = {
        'stonegarant.category': {
            'Meta': {'object_name': 'Category', '_ormbases': ['stonegarant.SeoEmpoweredModel']},
            'seoempoweredmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['stonegarant.SeoEmpoweredModel']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'stonegarant.memorial': {
            'Meta': {'object_name': 'Memorial', '_ormbases': ['stonegarant.SeoEmpoweredModel']},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stonegarant.Category']", 'null': 'True', 'blank': 'True'}),
            'cvetnik': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'photo1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'podstavka': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'seoempoweredmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['stonegarant.SeoEmpoweredModel']", 'unique': 'True', 'primary_key': 'True'}),
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
        'stonegarant.seoempoweredmodel': {
            'Meta': {'object_name': 'SeoEmpoweredModel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'seo_description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'seo_keywords': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'stonegarant.staticpage': {
            'Meta': {'object_name': 'StaticPage', '_ormbases': ['stonegarant.SeoEmpoweredModel']},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'seoempoweredmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['stonegarant.SeoEmpoweredModel']", 'unique': 'True', 'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['stonegarant']