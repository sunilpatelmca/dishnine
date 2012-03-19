from django.conf import settings
from django.conf.urls.defaults import *
from sphene.sphwiki.sitemaps import WikiSnipSitemap
from sphene.sphboard.sitemaps import ThreadsSitemap
from sphene.sphwiki.feeds import LatestWikiChanges
from sphene.sphwiki import urls as sphwiki_urls
from sphene.community.models import Group

defaultdict = { 'groupName': None,
                'urlPrefix': '', }

sitemaps = {
    'wiki': WikiSnipSitemap,
    'board': ThreadsSitemap,
    }

feeds = {
    'wiki': LatestWikiChanges,
    }

# newforms admin magic

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', include('Home.urls')),
	url(r'^Publication/', include('Publication.urls')),
	url(r'^Recent_Updates/', include('Recent_Updates.urls')),
	url(r'^Paper_Download/', include('Paper_Download.urls')),
	url(r'^Contact_us/', include('Contact_Us.urls')),
	url(r'^tinymce/', include('tinymce.urls')),
	url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:],'django.views.static.serve', {"document_root": settings.MEDIA_ROOT}),
	url(r'^Community_Board/$', 'sphene.community.views.groupaware_redirect_to', { 'url': '/board/show/0/', 'groupName': None }),
	url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', { 'sitemaps': sitemaps }),
	url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
	url(r'^community/', include('sphene.community.urls'), defaultdict),
	url(r'^board/', include('sphene.sphboard.urls'), defaultdict),
	url(r'^wiki/',  include('sphene.sphwiki.urls'), defaultdict),
	url(r'^blog/',  include('sphene.sphblog.urls'), defaultdict),
	#(r'^block/', include('sphene.sphblockframework.urls'), defaultdict),
	#url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
	url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
	#url(r'^accounts/logout/$', include('accounts.urls')),
	url(r'^accounts/logout/$', 'sphene.community.views.accounts_logout', {'group':Group.objects.get( name = 'DishNine' ), 'logged_out_template_name': 'logout.html'}),
	url(r'accounts/forgot/$', 'sphene.community.views.accounts_forgot',{'forgot_template_name': 'forgot.html', 'forgot_sent_template_name': 'forgot_sent.html'}),
	url(r'^accounts/register/$', 'sphene.community.views.register', {'group': Group.objects.get( name = 'DishNine' ), 'frm': 'main_site', 'register_template_name': 'register.html', 'email_sent_template_name':'register_emailsent.html'}, name = 'sph_register'),
	url(r'^accounts/register/(?P<emailHash>[a-zA-Z/\+0-9=]+)/$', 'sphene.community.views.register_hash',{'register_hash_template_name': 'register_hash.html', 'register_hash_success_template_name': 'register_hash_success.html'}, name = 'sph_register_hash'),
	#(r'^accounts/register/$', 'sphene.community.views.register', defaultdict),
	#(r'^accounts/register/(?P<emailHash>[a-zA-Z/\+0-9=]+)/$', 'sphene.community.views.register_hash', defaultdict),
	#url(r'^accounts/profile/$', 'sphene.community.views.profile', {'group': Group.objects.get( name = 'DishNine' ), 'profile_template_name':'profile.html', 'frm': 'main_site'}),
	url(r'^accounts/profile/(?P<user_id>\d+)/$', 'sphene.community.views.profile', {'group': Group.objects.get( name = 'DishNine' ), 'profile_template_name':'profile.html', 'frm': 'main_site'}),
	url(r'^accounts/profile/edit/$', 'sphene.community.views.profile_edit_mine', {'group': Group.objects.get( name = 'DishNine' ), 'profile_edit_template_name': 'profile_edit.html', 'frm':'main_site'}),
	url(r'^accounts/profile/edit/(?P<user_id>\d+)/$', 'sphene.community.views.profile_edit', {'group': Group.objects.get( name = 'DishNine' ), 'profile_edit_template_name': 'profile_edit.html', 'frm':'main_site'}),
	url(r'^accounts/profile/(?P<user_id>\d+)/reveal_address/$', 'sphene.community.views.reveal_emailaddress', name = 'sph_reveal_emailaddress'), 
	url(r'^accounts/terms/$', 'accounts.views.get_terms'),
	url(r'^admin/(.*)', admin.site.root),
	## for development only ...
	url(r'^static/sphene/(.*)$', 'django.views.static.serve', {'document_root': settings.ROOT_PATH + '/communitytools/media/sphene' }),
	url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.ROOT_PATH + '/media' }),
	url(r'^i18n/', include('django.conf.urls.i18n')),
)
