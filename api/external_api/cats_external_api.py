from django.core.files.images import ImageFile
import requests
from io import BytesIO


class CatsExternalApi:
    """
    Communicates with the outside world

    Point of interaction:

    CatsExternalApi.call(tag)

    returns array of paths
    ex.
    [
        "localhost:3000/api/media/img1.png",
        "localhost:3000/api/media/img2.png"
    ]
    """

    BASE_URL = 'https://cataas.com/cat/'
    DEFUALT_COUNT = 5

    def call(self, tag):
        """main interface for the external api"""
        images = []
        for count in range(self.DEFUALT_COUNT):
            response = self._get_response(tag)
            new_image = self._get_image(response)
            images.append(new_image)

        return images

    def _get_response(self, tag):
        """returns response and raises errors"""
        response = requests.get(
            self._get_tag_url(tag), timeout=10, stream=True
        )
        response.raise_for_status()

        return response

    def _get_image(self, response):
        """gets image and returns it"""
        image = ImageFile.open(BytesIO(response.content))

        return image

    def _get_tag_url(self, tag):
        return self.BASE_URL + tag
