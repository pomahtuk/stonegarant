# -*- coding: utf-8 -*-
from easy_thumbnails.files import get_thumbnailer
from PIL import Image


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