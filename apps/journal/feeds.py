import datetime

from django.contrib.syndication.feeds import Feed
from django.conf import settings

from models import Entry

class JournalEntryFeed(Feed):
    title = "The %s journal entries" % settings.SITE_NAME
    link = settings.SITE_URL
    description = settings.SITE_DESCRIPTION

    def items(self):
        return Entry.objects.all()[:20]

