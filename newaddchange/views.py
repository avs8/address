from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
import pprint
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib import auth 
from newaddchange.models import MoveType
from userprofile.models import UserProfile
from newaddchange.forms import MoveTypeForm, PersonalInformationForm, AddressOldNewForm
from django.core.context_processors import csrf
from formtools.wizard.views import SessionWizardView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponse


def mymove(request):
	if request.method == "POST":
		form_1 = MoveTypeForm()
		form_2 = PersonalInformationForm()
		form_3 = AddressOldNewForm()
		if form_1.is_valid() and form_2.is_valid() and form_3.is_valid():
			form_1.save() and form_2.save() and form_3.save()
			return HttpResponse("Thanks for submitting your information") 
	else:
		form1 = MoveTypeForm()
		form2 = PersonalInformationForm()
		form3 = AddressOldNewForm()
		args = {}
		args.update(csrf(request))
		args['form1'] = form1
		args['form2'] = form2
		args['form3'] = form3
		return render_to_response('mymove.html', {'form1':form1, 'form2':form2, 
											 'form3':form3})
FORMS = [("move_type", MoveTypeForm),
		("personal_information", PersonalInformationForm),
		("address_oldnew", AddressOldNewForm)]

TEMPLATES = {"move_type": "movetype.html",
			"personal_information": "personalinformation.html",
			"address_oldnew":"addressoldnew.html"}
			
					
def adon(wizard, request):
	cleaned_data = wizard.get_cleaned_data_for_step('address_oldnew') or {'method':'none'}
	return cleaned_data['method'] == 'address_oldnew'	
	
		

class AddressChangeWizard(SessionWizardView):
	def get_template_names(self):
		return [TEMPLATES[self.steps.current]]
	
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(AddressChangeWizard, self).dispatch(*args, **kwargs)
	
					
	def done(self, form_list, **kwargs):
		instance = MoveType()
		for form in form_list:
			for field, value in form.cleaned_data.iteritems():
				setattr(instance, field, value)
		instance.save()
		import hashlib
		form_data = dict(('%s' % (k),v) for form in form_list for k, v in form.cleaned_data.items())
		return render_to_response('done.html', {
            'form_data': form_data
        })
	
@login_required
def moves(request):
	profiles=UserProfile.objects.filter(user=request.user.id)
	moves = MoveType.objects.all()
	return render_to_response('moves.html',
	{'moves':moves, 'profiles':profiles}, context_instance=RequestContext(request))

def move(request, movetype_id=1):
	return render_to_response('move.html',
		{'move':MoveType.objects.get(id=movetype_id)},
		context_instance=RequestContext(request))  


def process_form_data(form_list):
	form_data = [form.cleaned_data for form in form_list]
	send_mail(form_data[0]['move_type'], 
              form_data[2]['personal_information'], form_data[1]['address_oldnew'],
              ['ajitasingh8@gmail.com'], fail_silently=False)
	return form_data


def language(request, language):
	response = HttpResponse("setting language to %s" % language)
	response.set_cookie('lang', language)
	return response