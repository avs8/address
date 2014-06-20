# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MoveType'
        db.create_table(u'newaddchange_movetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movingtype', self.gf('django.db.models.fields.CharField')(default=None, max_length=100)),
            ('movingdate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('movingstatus', self.gf('django.db.models.fields.CharField')(default=None, max_length=30)),
            ('buisnessname', self.gf('django.db.models.fields.CharField')(default=None, max_length=100, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default=None, max_length=10)),
            ('first_name', self.gf('django.db.models.fields.CharField')(default=None, max_length=100)),
            ('last_name', self.gf('django.db.models.fields.CharField')(default=None, max_length=100)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(default=None, max_length=12)),
            ('exclusive_notification', self.gf('django.db.models.fields.BooleanField')()),
            ('primary_email', self.gf('django.db.models.fields.EmailField')(max_length=50)),
            ('secondary_email', self.gf('django.db.models.fields.EmailField')(max_length=50, blank=True)),
            ('person_validate', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('person_authorization', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('own_rent', self.gf('django.db.models.fields.CharField')(default=None, max_length=5)),
            ('old_street', self.gf('django.db.models.fields.CharField')(default=None, max_length=100)),
            ('old_apt_suite', self.gf('django.db.models.fields.CharField')(default=None, max_length=100, blank=True)),
            ('old_city', self.gf('django.db.models.fields.CharField')(default=None, max_length=100)),
            ('old_state', self.gf('localflavor.us.models.USStateField')(default=None, max_length=2)),
            ('old_zip_code', self.gf('django.db.models.fields.CharField')(default=None, max_length=5, blank=True)),
            ('new_street', self.gf('django.db.models.fields.CharField')(default=None, max_length=100)),
            ('new_apt_suite', self.gf('django.db.models.fields.CharField')(default=None, max_length=100, blank=True)),
            ('new_city', self.gf('django.db.models.fields.CharField')(default=None, max_length=100)),
            ('new_state', self.gf('localflavor.us.models.USStateField')(default=None, max_length=2)),
            ('new_zip_code', self.gf('django.db.models.fields.CharField')(default=None, max_length=5, blank=True)),
        ))
        db.send_create_signal(u'newaddchange', ['MoveType'])


    def backwards(self, orm):
        # Deleting model 'MoveType'
        db.delete_table(u'newaddchange_movetype')


    models = {
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