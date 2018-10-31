import requests
from PIL import Image
from io import BytesIO

URL = 'https://cataas.com/cat'


def call_external_cats_api(tag=None, count=5):
    cat_images = []
    for count in range(count):
        response = requests.get(URL, timeout=10, stream=True)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))
        cat_images.append(image)