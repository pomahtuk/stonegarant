from django.conf import settings # import the settings file


def jivosite(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {
        'JIVOSITE_ID': settings.JIVOSITE_ID,
        'STATIC_URL': settings.STATIC_URL
    }