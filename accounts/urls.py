from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('accounts.views',
    url(r'^$', 'account_logout'),

)

