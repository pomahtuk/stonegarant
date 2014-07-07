from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from django import forms
from django.db import models
from django.conf import settings
import os
from PIL import Image

try:
    from easy_thumbnails.files import get_thumbnailer
    def thumbnail(image_path):
        thumbnailer = get_thumbnailer(image_path)
        thumbnail_options = {'crop': True, 'size': (100, 100), 'detail': True, 'upscale':True }
        t=thumbnailer.get_thumbnail(thumbnail_options)
        media_url = settings.MEDIA_URL
        return u'<img src="%s%s%s" alt="%s" width="100" height="100"/>' % (media_url, settings.AWS_STORAGE_BUCKET_NAME, t, image_path)
except ImportError:
    def thumbnail(image_path):
        absolute_url = os.path.join(settings.MEDIA_ROOT, image_path)
        return u'<img src="%s" alt="%s" />' % (absolute_url, image_path)

class AdminImageWidget(AdminFileWidget):
    """
    A FileField Widget that displays an image instead of a file path
    if the current file is an image.
    """
    def render(self, name, value, attrs=None):
        output = []
        file_name = str(value)
        if file_name:
            file_path = '%s%s' % (settings.MEDIA_URL, file_name)
            try:            # is image
                Image.open(os.path.join(settings.MEDIA_ROOT, file_name))
                output.append('<a target="_blank" href="%s">%s</a>' % \
                    (file_path, thumbnail(file_name)))
            except IOError: # not image
                output.append('')

        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))
