from django import forms
from newaddchange.models import MoveType, Contact
from django.forms import ModelForm
from localflavor.us.forms import USPhoneNumberField
from localflavor.us.forms import USZipCodeField


# add_introspection_rules([], ["^django_localflavor_us\.models\.USPhoneNumebrField"])


class MoveTypeForm(forms.ModelForm):
    class Meta:
        model = MoveType
        widgets = {
            'movingtype': forms.RadioSelect(),
            'movingdate': forms.DateInput(attrs={'class': 'datepicker'}),
            'movingstatus': forms.RadioSelect(),
        }
        fields = ('movingtype', 'movingdate', 'movingstatus', 'buisnessname')


class PersonalInformationForm(forms.ModelForm):
    class Meta:
        model = MoveType
        fields = ('title', 'first_name', 'last_name', 'phone_number', 'exclusive_notification',
                  'primary_email', 'secondary_email', 'person_validate', 'person_authorization')
        widgets = {
            'title': forms.RadioSelect(),
        }

    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
                                    error_message=(
                                    "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))


class AddressOldNewForm(forms.ModelForm):
    class Meta:
        model = MoveType
        fields = ('own_rent', 'old_street', 'new_street', 'old_apt_suite', 'old_city', 'old_state', 'old_zip_code',
                  'new_street', 'new_street', 'new_apt_suite', 'new_city', 'new_state', 'new_zip_code')
        widgets = {
            'own_rent': forms.RadioSelect(),
        }

    # add_introspection_rules([], ["^django_localflavor_us\.models\.USStateField"])
    # add_introspection_rules([], ["^django_localflavor_us\.models\.USZipCodeField"])
    # add_introspection_rules([], ["^django_localflavor_us\.models\.USPSSelect"])
    old_zip_code = USZipCodeField()
    new_zip_code = USZipCodeField()


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        cc_myself = forms.BooleanField(required=False)

        fields = ('subject', 'message', 'email', 'cc_myself')
