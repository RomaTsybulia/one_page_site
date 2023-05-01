from rest_framework.response import Response
from rest_framework.views import APIView

from dj_machinery.serializers import ProductSerializer, TransportSerializer
from dj_machinery.models import Product, Transport


class ProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class TransportList(APIView):
    def get(self, request, format=None):
        products = Transport.objects.all()
        serializer = TransportSerializer(products, many=True)
        return Response(serializer.data)

