from django.shortcuts import render_to_response
from django.template.loader import get_template 
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import login as auth_login 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.formtools.wizard.views import SessionWizardView
from newaddchange.forms import ContactForm
from django.core.context_processors import csrf
from forms import MyRegistrationForm
import logging

logr = logging.getLogger(__name__)

def index(request):
	return render_to_response('index.html')
		
def learnmore(request):
	return render_to_response('learnmore.html')
	
def about(request):
	return render_to_response('about.html')	
	
def contact(request):
	return render_to_response('contact.html')	
	

def login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/loggedin/')
	c = {}
	c.update(csrf(request))   
	return render_to_response('login.html', c)
    
	
def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid/')		

def loggedin(request):
	return render_to_response('loggedin.html', 
							 {'full_name':request.user.first_name})	
							 	
							 
def invalid_login(request):
	return render_to_response('invalid_login.html')

@login_required	
def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')

# def register_user(request):
# 	if request.method == 'POST':
# 		form = MyRegistrationForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return HttpResponseRedirect('/accounts/register_success/')
# 			
# 	args = {}
# 	args.update(csrf(request))
# 	args['form'] = MyRegistrationForm()
# 	return render_to_response('register.html', args)

def register_user(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/loggedin/')
 	user_creation_form = MyRegistrationForm(request.POST or None)
	if request.method == 'POST' and user_creation_form.is_valid():
		u_name = user_creation_form.cleaned_data.get('username')
		u_pass = user_creation_form.cleaned_data.get('password2')
		user_creation_form.save()
		u = authenticate(username=u_name,
                            password=u_pass)
		
		u.backend = "django.contrib.auth.backends.ModelBackend"
		auth_login(request, u)
		return HttpResponseRedirect('/newaddchange/addressoldnew/') 
	c = RequestContext(request, {'form': user_creation_form})
	return render_to_response('register.html', c)




def register_success(request):
	return render_to_response('register_success.html', {'first_name':request.user.username})
	
def contact(request):
	if request.method == 'POST':
		form=ContactForm(request.POST)
		if form.is_valid():
			saveit = form.save()
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			email = form.cleaned_data['email']
			cc_myself = form.cleaned_data['cc_myself']
			recipients = ['ajitasing8@gmail.com']
			if cc_myself:
				recipients.append(email)
			from django.core.mail import send_mail
			send_mail(subject, message, email, recipients)	
			return HttpResponse('Thanks for Contacting us!!! We will get back to you ASAP')
	else:
		form = ContactForm()
	args= {}
	args['form'] = form	
	args.update(csrf(request))	
	return render_to_response('contact.html', args)