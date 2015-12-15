__author__ = 'ilovriakov'

from django.http import HttpResponsePermanentRedirect
from django.conf import settings

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
            print(server_name)
        except KeyError:
            pass
        else:
            if getattr(settings, 'REMOVE_WWW', None) and server_name.startswith('www.'):
                return _get_redirect(server_name[4:], request)

        return None
