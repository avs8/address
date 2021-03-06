from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MyRegistrationForm(UserCreationForm):
		first_name = forms.CharField(required=False, label="First Name")
		last_name = forms.CharField(required=False, label="Last Name")
		email = forms.EmailField(required=True)


class Meta:
		model = User
		fields = ('username', 'password1', 'password2', 'first_name', 'last_name')


def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.set_password(self.cleaned_data['password1'])

		if commit:
				user.save()

		return user
