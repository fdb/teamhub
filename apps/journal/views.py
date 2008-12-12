from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import list_detail

from models import Entry

def list_all(request):
    latest_entries_by_user = []
    for user in User.objects.all():
        for entry in Entry.objects.filter(user=user)[:3]:
            latest_entries_by_user.append({'user':user, 'entry':entry})
    return list_detail.object_list(request, Entry.objects.all(), template_object_name='entry', extra_context={'latest_entries_by_user':latest_entries_by_user})
    
def list_user(request, user):
    pass

def detail_user(request, user, id):
    pass
    
def add_entry(request):
    if request.method == 'POST':
        entry = Entry(user=request.user, content=request.POST['content'])
        entry.save()
    return HttpResponseRedirect('/journal/')
add_entry = login_required(add_entry)
