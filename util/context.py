from django.conf import settings

def site_info_to_context(request):
    """Load information about the site in the template context."""
    return {
        'SITE_NAME': settings.SITE_NAME,
        'SITE_URL': settings.SITE_URL,
        'SITE_DESCRIPTION': settings.SITE_DESCRIPTION}