from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('Paper_Download.views',
    url(r'^$', 'paper_download'),
    url(r'^(?P<object_id>\d+)/$', 'get_paper_download'),
    url(r'^Level/(?P<level_id>\d+)/$', 'level_wise_paper_download'),
    url(r'^Subject/(?P<subject_id>\d+)/$|$', 'subject_wise_paper_download'),
)

