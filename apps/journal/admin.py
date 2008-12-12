from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from models import Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'content')
    search_fields = ('content',)
    
admin.site.register(Entry, EntryAdmin)
