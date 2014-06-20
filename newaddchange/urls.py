from django.conf.urls import patterns, url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from newaddchange import views
from newaddchange.views import AddressChangeWizard
from newaddchange.models import MoveType
from newaddchange.forms import MoveTypeForm, PersonalInformationForm, AddressOldNewForm


FORMS = [("move_type", MoveTypeForm),
		("personal_information", PersonalInformationForm),
		("address_oldnew", AddressOldNewForm)]



urlpatterns = patterns('',
				 url(r'^all/$', 'newaddchange.views.moves'),
    			url(r'^get/(?P<movetype_id>\d+)/$', 'newaddchange.views.move'),
				url(r'^admin/', include(admin.site.urls)),
				 url(r'^mymove/$', 'newaddchange.views.mymove'),
				 url(r'^move/$', 'newaddchange.views.move'),
				 url(r'^addressoldnew/$', AddressChangeWizard.as_view(FORMS)),
				 
)				 