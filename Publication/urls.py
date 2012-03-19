from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('Publication.views',
    url(r'^$', 'all_books_detail'),
    url(r'^Subject/(?P<subject_id>\d+)/$', 'subject_wise_book_detail'),
    url(r'^Level/(?P<level_id>\d+)/$', 'level_wise_book_detail'),
    url(r'^Book/(?P<book_id>\d+)/$', 'book_detail'),
    url(r'^Book/Author/(?P<author_id>\d+)/$', 'author_detail'),
    url(r'^Book/Publisher/(?P<publisher_id>\d+)/$', 'publisher_detail'),
    url(r'^Book/Distributor/(?P<distributor_id>\d+)/$', 'distributor_detail'),
)

