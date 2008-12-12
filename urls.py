from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib.sitemaps import FlatPageSitemap
from django.contrib import admin

from teamhub.apps.journal.feeds import JournalEntryFeed

admin.autodiscover()

feeds = {
    'journal': JournalEntryFeed,
}

sitemaps = {
    'flatpages': FlatPageSitemap,
}

urlpatterns = patterns('',
    (r'^$', 'teamhub.apps.dashboard.views.index'),
    (r'^journal/', include('teamhub.apps.journal.urls')),
#    (r'^forum/', include('projecthub.apps.forum.urls')),
#    (r'^accounts/', include('projecthub.apps.accounts.urls')),
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name':'accounts/login.html'}),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page':'/'}),
    (r'^admin/(.*)', admin.site.root),
    (r'^rss/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
