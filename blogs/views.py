from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from blogs import models, serializers



class BlogAPIViewpr(CreateModelMixin,
                   RetrieveModelMixin,
                   ListModelMixin,
                   GenericViewSet):
    queryset=models.Product.objects.all()
    serializer_class = serializers.Productserializers

class BlogAPIViewca(ModelViewSet):
    queryset=models.Category.objects.all()
    serializer_class = serializers.Categoryserializers