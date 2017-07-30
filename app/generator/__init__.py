import os
from datetime import date
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from flask import current_app as app
from tempfile import NamedTemporaryFile


def suffix(d):
    return 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10,
                                                                      'th')


def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))


class Generator(object):

    def __init__(self):
        pass

    def generate(self, name, award):
        pass


class Certificate(Generator):

    def __init__(self):
        pass

    def generate(self, name, award):

        fp = NamedTemporaryFile(suffix='.jpg')

        im = Image.open(os.path.join(app.config['STATIC_FOLDER'], 'images',
                                     'certificate-template.jpg'))

        draw = ImageDraw.Draw(im)

        width = 1308
        font = ImageFont.truetype(
            os.path.join(app.config['FONTS_FOLDER'], "FreeSans.ttf"), 20)

        w, h = draw.textsize(name, font=font)
        draw.text(((width - w) / 2, 470), name, (0, 0, 0), font=font)

        w, h = draw.textsize(award, font=font)
        draw.text(((width - w) / 2, 610), award, (0, 0, 0), font=font)

        today = date.today()

        day = custom_strftime('{S}', today)
        month = today.strftime('%B')
        year = today.strftime('%Y')

        w, h = draw.textsize(day, font=font)
        draw.text((350, 705), day, (0, 0, 0), font=font)

        w, h = draw.textsize(month, font=font)
        draw.text((580, 705), month, (0, 0, 0), font=font)

        w, h = draw.textsize(year, font=font)
        draw.text((870, 705), year, (0, 0, 0), font=font)

        im.save(fp)

        fp.flush()
        fp.seek(0)

        return fp
