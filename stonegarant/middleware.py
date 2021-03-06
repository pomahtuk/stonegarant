__author__ = 'ilovriakov'

from django.http import HttpResponsePermanentRedirect
from django.conf import settings
import sys

def _get_redirect(new_hostname, request):
    new_location = '%s://%s%s' % (
        request.is_secure() and 'https' or 'http',
        new_hostname,
        request.get_full_path()
    )
    return HttpResponsePermanentRedirect(new_location)


class SetRemoteAddrFromForwardedFor(object):
    def process_request(self, request):
        try:
            real_ip = request.META['HTTP_X_FORWARDED_FOR']
        except KeyError:
            pass
        else:
            # HTTP_X_FORWARDED_FOR can be a comma-separated list of IPs.
            # Take just the first one.
            real_ip = real_ip.split(",")[0]
            request.META['REMOTE_ADDR'] = real_ip

class HostnameRedirectMiddleware(object):
    def process_request(self, request):
        try:
            server_name = request.META['HTTP_HOST']
        except KeyError:
            pass
        else:
            server_should_be_prefixed = not (server_name.startswith('www.') or ('stage' in server_name) or (
                'fastvps-server' in server_name
            ) or ('localhost' in server_name))

            if settings.FORCE_WWW and server_should_be_prefixed:
                return _get_redirect('%s.%s' % ('www', server_name), request)

        return None
