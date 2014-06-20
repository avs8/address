from django.db import models
from django.contrib.auth.models import User

from datetime import datetime
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.models import USStateField


	
class MoveType(models.Model):
	temporary= 'Temporary'
	permanent='Permanent'
	individual='Individual'
	family='Family'
	buisness='Buisness' 
	own= 'Own'
	rent='Rent'
	movingtype_choice=((temporary, 'Temporary'),
						(permanent, 'Permanent'))
	moving_status_choices = (
			(individual, 'Individual'),
			(family, 'Family'),
			(buisness,'Business'))
	
	TITLE_CHOICES = (
    			('MR', 'Mr.'),
   				 ('MRS', 'Mrs.'),
    			('MS', 'Ms.'),)	
    
	place_choices=((own, 'Own'),
						(rent, 'Rent'))				 
	
	
	movingtype=models.CharField(max_length=100, choices=movingtype_choice, default=None)
	movingdate=models.DateField(blank=True, null=True) 
	movingstatus= models.CharField(max_length=30, choices=moving_status_choices, default=None)
	buisnessname=models.CharField(max_length=100, default=None, blank=True, null=True)   
	title=models.CharField(max_length=10, choices=TITLE_CHOICES,default=None)
	first_name= models.CharField(max_length=100, default=None)
	last_name=models.CharField(max_length=100, default=None)
	phone_number= models.CharField(max_length=12,default=None)
	exclusive_notification=models.BooleanField()
	primary_email=models.EmailField(max_length=50)
	secondary_email=models.EmailField(max_length=50, blank=True)
	person_validate=models.BooleanField(default=None)
	person_authorization= models.BooleanField(default=None)						
	own_rent=models.CharField(max_length=5, choices=place_choices, default=None)
	old_street=models.CharField(max_length=100, default=None)
	old_apt_suite=models.CharField(max_length=100,default=None, blank=True)
	old_city=models.CharField(max_length=100, default=None)
	old_state=USStateField(choices = STATE_CHOICES, default=None)
	old_zip_code=models.CharField(max_length=5, default=None, blank=True)
	new_street=models.CharField(max_length=100, default=None)
	new_apt_suite=models.CharField(max_length=100,default=None, blank=True)
	new_city=models.CharField(max_length=100, default=None)
	new_state=USStateField(choices = STATE_CHOICES, default=None)
	new_zip_code=models.CharField(max_length=5, default=None, blank=True)
	
	def __unicode__(self):
		return self.first_name
	
class Contact(models.Model):
	subject = models.CharField(max_length=100)
	message = models.TextField()
	email = models.EmailField()
	cc_myself = models.BooleanField()						
					