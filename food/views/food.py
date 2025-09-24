from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny

from food.models.food import Food
from food.serializers.food import FoodModelSerializer


@extend_schema(tags=("food",))
class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodModelSerializer
    permission_classes = [AllowAny]
