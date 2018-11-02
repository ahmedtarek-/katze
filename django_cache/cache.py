from django.core.files.storage import FileSystemStorage
from django.core.cache import cache


class Cache:
    """
    Uses File based caching using django filesytemstorage
    +
    Uses django database cache (key/value) to store tag (key) and images
    paths (values)
    """
    DEFAULT_IMG_EXTENSION = 'png'

    def get(self, key):
        return cache.get(key)

    def set(self, key, images):
        paths = self._store_images(key, images)
        cache.set(key, paths)

        return paths

    def _store_images(self, key, images):
        """stores images and returns paths"""

        paths = []
        for i, image in enumerate(images):
            image_name = self._construct_image_name(key, i)
            image_path = self._save_image(image, image_name)
            paths.append(image_path)

        return paths

    def _save_image(self, image, image_name):
        """saves a signle image into filesystem"""
        fs = FileSystemStorage()

        fs.save(image_name, image)
        path = fs.url(image_name)

        return path

    def _construct_image_name(self, tag, number):
        """
        Constructs the unique image name with extension
        ex. 'funny_3.png'
        """
        return f"{tag}_{number}.{self.DEFAULT_IMG_EXTENSION}"
