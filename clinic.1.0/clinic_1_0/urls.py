from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from notetaker_1_0.views import (RegistrationView,RegistrationCompleteView)
from django.contrib import admin
from two_factor.urls import urlpatterns as tf_urls
from two_factor.gateways.twilio.urls import urlpatterns as tf_twilio_urls

from two_factor.admin import AdminSiteOTPRequired
from two_factor.views import LoginView

admin.autodiscover()


urlpatterns = patterns('',
	 url(r'^$', 'notetaker_1_0.views.home_page', name='home'),
         url(r'^newnote/$', 'notetaker_1_0.views.newnote_page', name='newnote'),
	 url(r'^addpatient/$', 'notetaker_1_0.views.addpatient_page', name='addpatient'),
         url(r'^viewnote_as_table/$', 'notetaker_1_0.views.viewnote_as_table', name='view_note_as_table'),
         url(regex=r'^account/logout/$',view='django.contrib.auth.views.logout',name='logout',),
         url(regex=r'^account/custom-login/$',view=LoginView.as_view(redirect_field_name='next_page'),name='custom-login',),
         url(regex=r'^account/register/$',view=RegistrationView.as_view(),name='registration',),
         url(regex=r'^account/register/done/$',view=RegistrationCompleteView.as_view(),name='registration_complete',),
         url(r'^accounts/', include('registration.backends.default.urls')),
         url(r'^ckeditor/', include('ckeditor.urls')),
         url(r'', include('two_factor.urls', 'two_factor')),
         url(r'', include('user_sessions.urls', 'user_sessions')),
         url(r'', include(tf_urls + tf_twilio_urls, 'two_factor')),
         url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)