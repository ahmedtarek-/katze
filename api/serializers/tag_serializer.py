from rest_framework import serializers


class TagSerializer(serializers.Serializer):
    tag = serializers.CharField()

    def validate_tag(self, value):
        """Normalizes tag and checks if contains only alphabets"""
        normalized_tag = value.lower()
        if self._invalid_tag(normalized_tag):
            raise serializers.ValidationError(
                "Tag must contain only characters")
        return normalized_tag

    def _invalid_tag(self, tag):
        return not tag.isalpha()
