# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Contact.Email'
        db.delete_column(u'newaddchange_contact', 'Email')

        # Adding field 'Contact.email'
        db.add_column(u'newaddchange_contact', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='/', max_length=75),
                      keep_default=False)

        # Adding field 'MoveType.user'
        db.add_column(u'newaddchange_movetype', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=datetime.datetime(2014, 5, 27, 0, 0), to=orm['auth.User']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Contact.Email'
        db.add_column(u'newaddchange_contact', 'Email',
                      self.gf('django.db.models.fields.EmailField')(default='/', max_length=75),
                      keep_default=False)

        # Deleting field 'Contact.email'
        db.delete_column(u'newaddchange_contact', 'email')

        # Deleting field 'MoveType.user'
        db.delete_column(u'newaddchange_movetype', 'user_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'newaddchange.contact': {
            'Meta': {'object_name': 'Contact'},
            'cc_myself': ('django.db.models.fields.BooleanField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'newaddchange.movetype': {
            'Meta': {'object_name': 'MoveType'},
            'buisnessname': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'exclusive_notification': ('django.db.models.fields.BooleanField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100'}),
            'movingdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'movingstatus': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30'}),
            'movingtype': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100'}),
            'new_apt_suite': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'blank': 'True'}),
            'new_city': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100'}),
            'new_state': ('localflavor.us.models.USStateField', [], {'default': 'None', 'max_length': '2'}),
            'new_street': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100'}),
            'new_zip_code': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '5', 'blank': 'True'}),
            'old_apt_suite': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'blank': 'True'}),
            'old_city': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100'}),
            'old_state': ('localflavor.us.models.USStateField', [], {'default': 'None', 'max_length': '2'}),
            'old_street': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100'}),
            'old_zip_code': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '5', 'blank': 'True'}),
            'own_rent': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '5'}),
            'person_authorization': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'person_validate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '12'}),
            'primary_email': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            'secondary_email': ('django.db.models.fields.EmailField', [], {'max_length': '50', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['newaddchange']