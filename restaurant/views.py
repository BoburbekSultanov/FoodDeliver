from drf_spectacular.utils import extend_schema
from rest_framework import generics, viewsets, views
from rest_framework.permissions import AllowAny

from restaurant.models import Restaurant
from restaurant.serializers import RestaurantModelSerializers


@extend_schema(tags=["restaurant", ])
class RestaurantDetailApiView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantModelSerializers
    permission_classes = [AllowAny]


class Test(views.APIView):
    pass


class Test1(viewsets.ModelViewSet):
    pass
