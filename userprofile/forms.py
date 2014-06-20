from django import forms
from models import UserProfile
from newaddchange.models import MoveType
from address.forms import MyRegistrationForm

class UserProfileForm(forms.ModelForm):

	class Meta:
		model = UserProfile	
		
		fields=('first_name','last_name','email', 'phone_number')
		
	