from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from models import UserProfile
from forms import UserProfileForm
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from newaddchange.models import MoveType
from address.forms import MyRegistrationForm

	


@login_required
def user_profile(request):
	user = User.objects.get_or_create(pk=request.user.id)
	if request.method == 'POST':
		form = UserProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			form.user = request.user
			return HttpResponseRedirect('/accounts/loggedin')
	else:
		
		form= UserProfileForm(instance=request.user)
	args={}
	args.update(csrf(request))
	args['form'] = form
	return render_to_response('profile.html',args, context_instance=RequestContext(request))

# 
#   # def user_profile(request):
#     success = False
#     user = User.objects.get(pk=request.user.id)
#     if request.method == 'POST':
#         upform = UserProfileForm(request.POST, instance=user.get_profile())
#         if upform.is_valid():
#             up = upform.save(commit=False)
#             up.user = request.user
#             up.save()
#             success = True
#     else:
#         upform = UserProfileForm(instance=request.user)
# 
#     return render_to_response('profile.html',
#         locals(), context_instance=RequestContext(request))

 
#