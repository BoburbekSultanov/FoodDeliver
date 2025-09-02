from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import AllowAny

from food.models import Category, Food
from food.serializers import CategoryModelSerializers, FoodModelSerializer


@extend_schema(tags=("category",))
class CategoryCreateApiView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializers
    permission_classes = [AllowAny]


@extend_schema(tags=("category",))
class CategoryUpdateApiView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializers
    permission_classes = [AllowAny]
    lookup_field = 'pk'


@extend_schema(tags=("category",))
class CategoryDetailApiView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializers
    permission_classes = [AllowAny]
    lookup_field = 'pk'


@extend_schema(tags=("category",))
class CategoryDestroyAPIView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializers
    permission_classes = [AllowAny]
    lookup_field = "pk"


@extend_schema(tags=("food",))
class FoodListCreateApiView(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodModelSerializer
    permission_classes = [AllowAny]


#
#
# @extend_schema(tags=("food",))
# class FoodUpdateApiView(generics.UpdateAPIView):
#     queryset = Food.objects.all()
#     serializer_class = FoodModelSerializer
#     permission_classes = [AllowAny]
#     lookup_field = "pk"
#
#
# @extend_schema(tags=("food",))
# class FoodDeleteApiView(generics.DestroyAPIView):
#     queryset = Food.objects.all()
#     serializer_class = FoodModelSerializer
#     permission_classes = [AllowAny]
#     lookup_field = "pk"


@extend_schema(tags=("food",))
class FoodDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodModelSerializer
    permission_classes = [AllowAny]
    lookup_field = "pk"
