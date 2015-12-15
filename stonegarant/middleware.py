__author__ = 'ilovriakov'

from django.http import HttpResponsePermanentRedirect
from django.conf import settings
from django.contrib.sites.models import Site

def _get_redirect(new_hostname, request):
    new_location = '%s://%s%s' % (
        request.is_secure() and 'https' or 'http',
        new_hostname,
        request.get_full_path()
    )
    return HttpResponsePermanentRedirect(new_location)

class HostnameRedirectMiddleware(object):
    def process_request(self, request):
        server_name = request.META['SERVER_NAME']

        if getattr(settings, 'REMOVE_WWW', None) and server_name.startswith('www.'):
            return _get_redirect(server_name[4:], request)

        catchall = getattr(settings, 'CATCHALL_REDIRECT_HOSTNAME', None)
        # if catchall hostname is set, verify that the current
        # hostname is valid, and redirect if not
        if catchall:
            # cache all site domains in one query
            if not hasattr(self, '_sites'):
                self._sites = Site.objects.values_list('domain', flat=True)
            if server_name not in self._sites:
                return _get_redirect(catchall, request)

        return None
