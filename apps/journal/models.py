from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Entry(models.Model):
    """A Journal keeps track of what everyone is working on."""
    
    user = models.ForeignKey(User)
    content = models.TextField(_('content'))
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)

    class Meta:
        db_table = 'journal_entries'
        verbose_name = 'journal entry'
        verbose_name_plural = 'journal entries'
        ordering = ('-created',)
        
    def __unicode__(self):
        return "%s: %s - %s" % (self.user.get_full_name(), self.content[:50], self.created)
        
    def get_absolute_url(self):
        return "/journal/%s/%s/" % (self.user.username, self.id)