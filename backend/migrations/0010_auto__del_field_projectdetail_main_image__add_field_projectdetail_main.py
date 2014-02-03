# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ProjectDetail.main_image'
        db.delete_column(u'backend_projectdetail', 'main_image')

        # Adding field 'ProjectDetail.main_image_url'
        db.add_column(u'backend_projectdetail', 'main_image_url',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=200, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'ProjectDetail.main_image'
        db.add_column(u'backend_projectdetail', 'main_image',
                      self.gf('django.db.models.fields.files.FileField')(default=None, max_length=100),
                      keep_default=False)

        # Deleting field 'ProjectDetail.main_image_url'
        db.delete_column(u'backend_projectdetail', 'main_image_url')


    models = {
        u'backend.carouselitem': {
            'Meta': {'ordering': "['position']", 'object_name': 'CarouselItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'backend.metadata': {
            'Meta': {'object_name': 'Metadata'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'backend.persona': {
            'Meta': {'object_name': 'Persona'},
            'contact': ('django.db.models.fields.TextField', [], {}),
            'cv': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'site_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'skills': ('django.db.models.fields.TextField', [], {})
        },
        u'backend.project': {
            'Meta': {'object_name': 'Project'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backend.Persona']"}),
            'css_class': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '20', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_image_url': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'status': ('django.db.models.fields.IntegerField', [], {})
        },
        u'backend.projectdetail': {
            'Meta': {'object_name': 'ProjectDetail'},
            'caption': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.TextField', [], {'default': 'None', 'max_length': '500', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_image_url': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backend.Project']"})
        }
    }

    complete_apps = ['backend']