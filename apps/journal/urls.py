from django.conf.urls.defaults import *
from models import Entry

urlpatterns = patterns('teamhub.apps.journal.views',
    (r'^$', 'list_all'),
    (r'^add_entry/$', 'add_entry'),
    (r'^(?P<user>\w+)/$', 'list_user'),
    (r'^(?P<user>\w+)/(?P<id>[0-9]+)/$', 'detail_user'),
)