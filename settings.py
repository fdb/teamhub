import os
import sys

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (('Frederik De Bleser', 'frederik@pandora.be'),)
MANAGERS = ADMINS

TIME_ZONE = 'Europe/Brussels'
LANGUAGE_CODE = 'en'
SITE_ID = 1
PREPEND_WWW = True

# Default language for the site
DEFAULT_LANGUAGE = 'en-us'

# Root of the site install
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT.
MEDIA_URL = '/media'
ADMIN_MEDIA_PREFIX = MEDIA_URL + '/admin/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'teamhub.util.require_login.RequireLoginMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'teamhub.util.context.site_info_to_context',
)

ROOT_URLCONF = 'teamhub.urls'

TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, 'templates'),)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.admin',
    'django.contrib.markup',
    'typogrify',
    'template_utils',
    'teamhub.apps.dashboard',
    'teamhub.apps.journal',
    'teamhub.util',
    'dmigrations',
)

# Migrations
DMIGRATIONS_DIR = os.path.join(PROJECT_ROOT, 'migrations')
DISABLE_SYNCDB = True

# Add required dependencies
sys.path.append(os.path.join(PROJECT_ROOT, 'vendor'))

# Dependency checker functionality.  Gives our users nice errors when they start
# out, instead of encountering them later on.  Most of the magic for this
# happens in manage.py, not here.
install_help = '''
Please see http://code.google.com/p/reviewboard/wiki/GettingStarted
for help setting up this Django project.
'''
def dependency_error(string):
    sys.stderr.write('%s\n' % string)
    sys.stderr.write(install_help)
    sys.exit(1)

# Load local settings.  This can override anything in here, but at the very
# least it needs to define database connectivity.
try:
    from settings_local import *
except ImportError:
    dependency_error('Unable to read settings_local.py.')
