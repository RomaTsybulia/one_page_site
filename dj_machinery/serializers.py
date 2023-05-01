from rest_framework import serializers

from dj_machinery.models import Transport, Product


class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "get_image",
            "get_thumbnail",
        )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "get_image",
            "get_thumbnail",
        )
