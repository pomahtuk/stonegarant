from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe
from django.conf import settings
import os
from PIL import Image
from django.forms.widgets import ClearableFileInput
from easy_thumbnails.files import get_thumbnailer


class SafeImageClearableFileInput(ClearableFileInput):
    template_with_initial = (
        u'%(clear_template)s<br />'
        u'%(input_text)s: %(input)s'
    )
    template_with_thumbnail = (
        u'%(template)s<br />'
        u'<a href="%(source_url)s" target="_blank">%(thumb)s</a>'
    )

    def __init__(self, thumbnail_options=None, attrs=None):
        thumbnail_options = thumbnail_options or {}
        thumbnail_options = thumbnail_options.copy()
        if 'size' not in thumbnail_options:
            thumbnail_options['size'] = (80, 80)
        self.thumbnail_options = thumbnail_options.copy()
        super(SafeImageClearableFileInput, self).__init__(attrs)

    def thumbnail_id(self, name):
        return '%s_thumb_id' % name

    def get_thumbnail(self, value):
        try:
            Image.open(value)
            thumbnailer = get_thumbnailer(value, value.name)
            thumbnailer.source_storage = value.storage
            if hasattr(value, 'thumbnail_storage'):
                thumbnailer.thumbnail_storage = value.thumbnail_storage
            return thumbnailer.get_thumbnail(self.thumbnail_options)
        except IOError:  # not image
            return False

    def render(self, name, value, attrs=None):
        output = super(SafeImageClearableFileInput, self).render(
            name, value, attrs)
        if not value or not hasattr(value, 'storage'):
            return output
        thumb = self.get_thumbnail(value)
        if thumb is False:
            return output
        else:
            substitution = {
                'template': output,
                'thumb': thumb.tag(id=self.thumbnail_id(name)),
                'source_url': value.storage.url(value.name),
            }
            return mark_safe(self.template_with_thumbnail % substitution)



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
            try:  # an image
                Image.open(os.path.join(settings.MEDIA_ROOT, file_name))
                output.append('<a target="_blank" href="%s">%s</a>' % (file_path,
                                                                       thumbnail(file_name)
                                                                       )
                              )
            except IOError:  # not image
                output.append('')

        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))
