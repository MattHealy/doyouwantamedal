import os
import boto3
import uuid
from datetime import date, datetime
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

    def store(self, name, award):

        client = boto3.client(
            'dynamodb', region_name=os.environ.get('AWS_REGION'))

        id = str(uuid.uuid4())

        item = {
            'id': {
                'S': id
            },
            'type': {
                'S': self.type
            },
            'insertdate': {
                'S': datetime.utcnow().isoformat(timespec='seconds')
            },
            'name': {
                'S': name
            },
            'award': {
                'S': award
            }
        }

        client.put_item(
            TableName=app.config['TABLE_NAME'],
            Item=item
        )


class Certificate(Generator):

    def __init__(self):
        self.type = 'certificate'

    def generate(self, name, award):

        fp = NamedTemporaryFile(suffix='.jpg')

        im = Image.open(os.path.join(app.config['STATIC_FOLDER'], 'images',
                                     'certificate-template.jpg'))

        draw = ImageDraw.Draw(im)

        width = 1298
        font = ImageFont.truetype(
            os.path.join(app.config['FONTS_FOLDER'], "FreeSans.ttf"), 20)

        w, h = draw.textsize(name, font=font)
        draw.text(((width - w) / 2, 465), name, (0, 0, 0), font=font)

        w, h = draw.textsize(award, font=font)
        draw.text(((width - w) / 2, 605), award, (0, 0, 0), font=font)

        today = date.today()

        day = custom_strftime('{S}', today)
        month = today.strftime('%B')
        year = today.strftime('%Y')

        w, h = draw.textsize(day, font=font)
        draw.text((350, 700), day, (0, 0, 0), font=font)

        w, h = draw.textsize(month, font=font)
        draw.text((580, 700), month, (0, 0, 0), font=font)

        w, h = draw.textsize(year, font=font)
        draw.text((870, 700), year, (0, 0, 0), font=font)

        im.save(fp)

        fp.flush()
        fp.seek(0)

        return fp
