import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from flask import current_app as app

class Generator(object):

    def __init__(self):
        pass

    def generate(self, name, award):
        pass


class Certificate(Generator):

    def __init__(self):
        pass

    def generate(self, name, award):

        im = Image.open(os.path.join(app.config['STATIC_FOLDER'], 'images',
                                     'certificate-template.jpg'))                     

        draw = ImageDraw.Draw(im)

        width = 1308
        font = ImageFont.truetype(
            os.path.join(app.config['FONTS_FOLDER'], "FreeSans.ttf"), 20)

        w, h = draw.textsize(name, font=font)
        draw.text(((width-w)/2, 470), name, (0,0,0), font=font)

        w, h = draw.textsize(award, font=font)
        draw.text(((width-w)/2, 610), award, (0,0,0), font=font)

        im.save(os.path.join(app.config['STATIC_FOLDER'], 'certificates',
                             'out.jpg'))
