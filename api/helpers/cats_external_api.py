from django.conf import settings
import requests
import datetime
from PIL import Image
from io import BytesIO

URL = 'https://cataas.com/cat'


def call_external_cats_api(tag=None, count=5):
    paths = []
    for count in range(count):
        response = requests.get(URL, timeout=10, stream=True)
        response.raise_for_status()

        image_name = 'photo-' + str(datetime.datetime.now()) + '.png'
        new_path = settings.MEDIA_ROOT + '/' + image_name

        image = Image.open(BytesIO(response.content))
        image.save(new_path)

        paths.append(new_path)

    return paths
