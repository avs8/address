# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'MoveType.user'
        db.delete_column(u'newaddchange_movetype', 'user_id')


    def backwards(self, orm):
        # Adding field 'MoveType.user'
        db.add_column(u'newaddchange_movetype', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='/', to=orm['auth.User']),
                      keep_default=False)


    models = {
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
            'title': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10'})
        }
    }

    complete_apps = ['newaddchange']