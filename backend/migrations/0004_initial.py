# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Persona'
        db.create_table(u'backend_persona', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('contact', self.gf('django.db.models.fields.TextField')()),
            ('skills', self.gf('django.db.models.fields.TextField')()),
            ('cv', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('site_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'backend', ['Persona'])

        # Adding model 'Project'
        db.create_table(u'backend_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('main_image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('css_class', self.gf('django.db.models.fields.TextField')(max_length=20)),
            ('status', self.gf('django.db.models.fields.IntegerField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.Persona'])),
        ))
        db.send_create_signal(u'backend', ['Project'])

        # Adding model 'ProjectDetail'
        db.create_table(u'backend_projectdetail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend.Project'])),
            ('caption', self.gf('django.db.models.fields.TextField')()),
            ('main_image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'backend', ['ProjectDetail'])

        # Adding model 'CarouselItem'
        db.create_table(u'backend_carouselitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('subtitle', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'backend', ['CarouselItem'])

        # Adding model 'Metadata'
        db.create_table(u'backend_metadata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'backend', ['Metadata'])


    def backwards(self, orm):
        # Deleting model 'Persona'
        db.delete_table(u'backend_persona')

        # Deleting model 'Project'
        db.delete_table(u'backend_project')

        # Deleting model 'ProjectDetail'
        db.delete_table(u'backend_projectdetail')

        # Deleting model 'CarouselItem'
        db.delete_table(u'backend_carouselitem')

        # Deleting model 'Metadata'
        db.delete_table(u'backend_metadata')


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
            'caption': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['backend.Project']"})
        }
    }

    complete_apps = ['backend']