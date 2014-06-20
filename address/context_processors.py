from forms import MyRegistrationForm

def registration_form(request):
	return {
     'registration_form' : MyRegistrationForm()
}