from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('Contact_Us.views',
    url(r'^$', 'contact_us'),
)
