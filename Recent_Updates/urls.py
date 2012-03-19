from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('Recent_Updates.views',
    url(r'^$', 'recent_updates'),
    url(r'^(?P<object_id>\d+)/$', 'get_recent_update'),
    url(r'^Level/(?P<level_id>\d+)/$', 'level_wise_recent_updates'),
    url(r'^Subject/(?P<subject_id>\d+)/$|$', 'subject_wise_recent_updates'),
)

