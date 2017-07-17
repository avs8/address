from django.conf.urls import patterns, include, url
from newaddchange import views
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
     url(r'^newaddchange/', include('newaddchange.urls')),
     url(r'^accounts/', include('userprofile.urls')),
    url(r'^$', 'address.views.index', name='home'),
    url(r'^learnmore/$', 'address.views.learnmore'),
    url(r'^about/$', 'address.views.about'),
    url(r'^contact/$', 'address.views.contact'),   
    url(r'^accounts/login/$', 'address.views.login'),
    url(r'^accounts/auth/$', 'address.views.auth_view'),
    url(r'^accounts/logout/$', 'address.views.logout'),
    url(r'^accounts/loggedin/$', 'address.views.loggedin'),
    url(r'^accounts/invalid/$', 'address.views.invalid_login'),
    url(r'^accounts/register/$', 'address.views.register_user'),
    url(r'^accounts/register_success/$', 'address.views.register_success'),
    # url('', include('social.apps.django_app.urls', namespace='social'))
    
    
)

