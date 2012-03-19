from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

"""
feeds = {
    'latestpages': LatestPages,
}

sitemaps = {
    'wiki': Wiki,
}
"""

urlpatterns = patterns('',
    url(r'^$', include('Home.urls')),
    url(r'^Publication/', include('Publication.urls')),
    url(r'^Recent_Updates/', include('Recent_Updates.urls')),
    url(r'^Paper_Download/', include('Paper_Download.urls')),
    url(r'^Contact_Us/', include('Contact_Us.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/(.*)', admin.site.root),
    url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 
        'django.views.static.serve', {"document_root": settings.MEDIA_ROOT}),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', include('accounts.urls')),
    url(r'^accounts/register/$', 'sphene.community.views.register', name = 'sph_register'),
    (r'^board/', include('sphene.sphboard.urls')),
    (r'^(?P<urlPrefix>test/(?P<groupName>\w+))/board/', include('sphene.sphboard.urls')),
    (r'^(?P<urlPrefix>test/(?P<groupName>\w+))/wiki/',  include('sphene.sphwiki.urls')),
    (r'^wiki/',  include('sphene.sphwiki.urls'), { 'urlPrefix': 'wiki', 'groupName': 'Sphene' }),
    (r'^static/sphene/(.*)$', 'django.views.static.serve', {'document_root': settings.ROOT_PATH + '/communitytools/static/sphene' }),
    (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.ROOT_PATH + '/static' }),
    (r'^site_media/(.*)$', 'django.views.static.serve', {'document_root': '/home/kahless/dev/python/diamanda/media'}), 
    (r'^accounts/register/(?P<emailHash>[a-zA-Z/\+0-9=]+)/$', 'sphene.community.views.register_hash'),
)

