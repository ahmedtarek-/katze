import requests

from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response

from ..serializers import TagSerializer
from ..external_api import catsExternalApi
from django_cache import cache


class CatApiView(GenericAPIView):
    """
    API for retrieving cats

    URL PARAMS:
    ```
    {
        tag: 'string'
    }
    ```

    SUCCESS RESPONSE:
    ```
    {
        cats: [
            img: 'string'
            .
            .
            img: 'string'
        ]
    }
    ```
    """
    serializer_class = TagSerializer

    def get(self, request, *args, **kwargs):
        tag = self._get_valid_tag(kwargs)

        try:
            data = self._get_images_with_tag(tag)
        except requests.exceptions.ConnectionError:
            return Response(
                {'details': 'Connection failed, please try again later'},
                status=status.HTTP_400_BAD_REQUEST
            )
        except requests.exceptions.HTTPError:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(data, status=status.HTTP_200_OK)

    def _get_valid_tag(self, data):
        """Validates tag using TagSerializer"""
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        tag = serializer.validated_data['tag']
        return tag

    def _get_images_with_tag(self, tag):
        """get images from cache or from external api"""
        images_paths = cache.get(tag)
        if not images_paths:
            images = catsExternalApi.call(tag)
            images_paths = cache.set(tag, images)

        images_data = self._construct_data_object(images_paths)

        return images_data

    def _construct_data_object(self, images_paths):
        return [{'img': path} for path in images_paths]
