from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .helpers import call_external_cats_api


class CatApiView(APIView):
    """
    API for retrieving cats
    """

    def get(self, request, format=None):
        tag = request.GET.get('tag', None)
        images_paths = call_external_cats_api()

        data = list(map(lambda x: {'img': x}, images_paths))
        return Response(data, status=status.HTTP_200_OK)
