# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ProjectDetail.description'
        db.add_column(u'backend_projectdetail', 'description',
                      self.gf('django.db.models.fields.TextField')(max_length=500, null=True),
                      keep_default=False)


        # Changing field 'ProjectDetail.caption'
        db.alter_column(u'backend_projectdetail', 'caption', self.gf('django.db.models.fields.TextField')(max_length=200))

    def backwards(self, orm):
        # Deleting field 'ProjectDetail.description'
        db.delete_column(u'backend_projectdetail', 'description')


        # Changing field 'ProjectDetail.caption'
        db.alter_column(u'backend_projectdetail', 'caption', self.gf('django.db.models.fields.TextField')())

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
            'css_class': ('django.db.models.fields.TextField', [], {'max_length': '20'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'status': ('django.db.models.fields.IntegerField', [], {})
        },
        u'backend.projectdetail': {
            'Meta': {'object_name': 'ProjectDetail'},
            'caption': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backend.Project']"})
        }
    }

    complete_apps = ['backend']