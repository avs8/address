from django.db import models
from django.contrib.auth.models import User
from newaddchange.models import MoveType

class UserProfile(models.Model):
	user=models.OneToOneField(User, related_name="profile")
	first_name=models.CharField(max_length=50, blank=True)
	last_name=models.CharField(max_length=50, blank=True)
	email=models.EmailField(max_length=50)
	phone_number= models.CharField(max_length=12,blank=True)
	
	def __unicode__(self):
		return self.first_name
	
		
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])	
