# -*- coding: utf-8 -*-
from easy_thumbnails.files import get_thumbnailer
from PIL import Image
from django.core.urlresolvers import reverse
import requests
from StringIO import StringIO
from mimetypes import MimeTypes


class InlineEditLinkMixin(object):
    readonly_fields = ['edit_details']
    edit_label = u'Редактировать'

    def edit_details(self, obj):
        if obj.id:
            opts = self.model._meta
            return "<a href='%s' target='_blank'>%s</a>" % (reverse(
                'admin:%s_%s_change' % (opts.app_label, opts.object_name.lower()),
                args=[obj.id]
            ), self.edit_label)
        else:
            return u'(сохрани для возможности редактировать)'
    edit_details.allow_tags = True


def simple_admin_thumb(obj, photo):
    output = [
        u'<style>',
        u'.field-admin_thumbnail a{display: block; text-align: center}',
        u'.field-admin_thumbnail a img{display: inline-block;}',
        u'</style>',
    ]
    if obj.admin_thumb:
        output.append(u'<img src="%s" />' % obj.admin_thumb)
        return u''.join(output)
    else:
        if photo:
            try:  # an image
                Image.open(photo)
                thumbnailer = get_thumbnailer(photo)
                thumbnailer_options = ({'size': (100, 100), 'crop': False})
                thumb_file = thumbnailer.get_thumbnail(thumbnailer_options)
                obj.admin_thumb = thumb_file.url
                obj.save()
                output.append(u'<img src="%s" />' % thumb_file.url)
                return u''.join(output)
            except IOError:  # not image
                return 'not an image'

        else:
            return 'нет изображения'


def admin_thumb(obj, photo):
    output = [
        u'<style>',
        u'.field-admin_thumbnail a{display: block; text-align: center}',
        u'.field-admin_thumbnail a img{display: inline-block;}',
        u'</style>',
    ]
    if obj.admin_thumb:
        output.append(u'<img src="%s" />' % obj.admin_thumb.url)
        return u''.join(output)
    else:
        if photo:
            try:  # an image
                Image.open(photo)
                thumbnailer = get_thumbnailer(photo)
                thumbnailer_options = ({'size': (100, 100), 'crop': False})
                thumb_file = thumbnailer.get_thumbnail(thumbnailer_options)
                # save resulting thumb to admin thumb
                # self.admin_thumb = thumb_file
                obj.admin_thumb.save(thumb_file.name, thumb_file)
                obj.save()
                output.append(u'<img src="%s" />' % thumb_file.url)
                return u''.join(output)
            except IOError:  # not image
                return 'not an image'

        else:
            return 'нет изображения'


def email_thumb(photo):
    Image.open(photo)
    thumbnailer = get_thumbnailer(photo)
    thumbnailer_options = ({'size': (230, 250), 'crop': False, 'autocrop': True})
    thumb_file = thumbnailer.get_thumbnail(thumbnailer_options)
    return thumb_file.url


def get_base64_image(url):
    template_image = ''
    mime = MimeTypes()
    mime_type = mime.guess_type(url)[0]
    # Steam the image from the url
    request = requests.get(url)
    image_buffer = StringIO(request.content)

    if image_buffer:
        template_image = image_buffer.getvalue().encode('base64')
        template_image = u'data:%s;base64,%s' % (mime_type, template_image)

    return template_image
