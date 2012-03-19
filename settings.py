# Django settings for testtinymce project.

import os

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
LIB_PATH = os.path.join(ROOT_PATH,'communitytools', 'sphenecoll')


import sys
sys.path.append(ROOT_PATH)
sys.path.append(LIB_PATH)


CACHE_BACKEND = 'locmem:///'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Joyal Shah', 'joyal.shah@njconsultancy.com'),
)

MANAGERS = ADMINS

#DATABASE_ENGINE = 'postgresql_psycopg2'    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
#DATABASE_ENGINE = 'postgresql'    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
DATABASE_ENGINE = 'mysql'
DATABASE_NAME = 'books1' # Or path to database file if using sqlite3.
#DATABASE_USER = 'postgres'             # Not used with sqlite3.
#DATABASE_USER = 'postgres'             # Not used with sqlite3.
DATABASE_USER = 'root'
#DATABASE_PASSWORD = 'postgres'         # Not used with sqlite3.
#DATABASE_PASSWORD = 'postgres'         # Not used with sqlite3.
DATABASE_PASSWORD = 'root'
#DATABASE_HOST = 'localhost'             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_HOST = 'localhost'             # Set to empty string for localhost. Not used with sqlite3.
#DATABASE_PORT = '5432'             # Set to empty string for default. Not used with sqlite3.
DATABASE_PORT = '3306'             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
# although not all variations may be possible on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

#SPH_SETTINGS = { 'wiki_rss_url' : '/feeds/wiki/',
#                 }

SPH_SETTINGS = { }
SPH_SETTINGS['workaround_select_related_bug'] = True

#SPH_SETTINGS['community_show_languageswitcher'] = True

LANGUAGES = (
    ('de', 'German'),
    ('en', 'English'),
    ('fr', 'French'),
    ('pl', 'Polish'),
    ('ko', 'Korean'),
)


# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en-us'

EMAIL_HOST = '' # GIVE A SMTP HOST NAME EX. - smtp.gmail.com

# Port for sending e-mail.
EMAIL_PORT = 0 # GIVE A PORT NUMBER : 587

# Optional SMTP authentication information for EMAIL_HOST.
EMAIL_HOST_USER = '' # USER NAME EX. - dharmesh.patel.eiffel@gmail.com
EMAIL_HOST_PASSWORD = '' # PASSWORD EX. - 123456
EMAIL_USE_TLS = True # set as a True


SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = "%s/%s/" % (ROOT_PATH, 'media/')

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '7j6o^y6#w@#067^-dr)h_)*^^@b&mgmd@1_y309w+)rk!4p^0!'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'sphene.community.groupaware_templateloader.load_template_source',
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'sphene.sphboard.middleware.PerformanceMiddleware',
    'sphene.community.middleware.PsycoMiddleware',
    'sphene.community.middleware.ThreadLocals',
    'sphene.community.middleware.GroupMiddleware',
    'sphene.community.middleware.MultiHostMiddleware',
    'sphene.community.middleware.StatsMiddleware',
    'sphene.community.middleware.LastModified',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'sphene.community.context_processors.navigation',
)

ROOT_URLCONF = 'dishnine.urls'

SPH_HOST_MIDDLEWARE_URLCONF_MAP = {
    r'^(?P<groupName>\w+).localhost.*$': { 'urlconf': 'urlconfs.community_urls', },
    '.*': { 'urlconf': 'urlconfs.community_urls',
            'params': { 'groupName': 'DishNine' } },
}

TEMPLATE_DIRS = (
    "%s/%s/" % (ROOT_PATH, 'templates'),
	"%s/%s/" % (ROOT_PATH, 'sitetemplates'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.humanize',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
    'tinymce',
    'Publication',
    'Home',
    'Recent_Updates',
    'Paper_Download',
    'Contact_Us',
    'accounts',
    'dishnine',
    'sphene.community',
    'sphene.sphboard',
    'sphene.sphwiki',
    'sphene.sphblog',
)

DJAPIAN_DATABASE_PATH = '/var/cache/sct'

TINYMCE_SPELLCHECKER = True

TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme_advanced_buttons3_add': "|table,spellchecker,paste,searchreplace",
}
