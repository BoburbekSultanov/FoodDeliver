from drf_spectacular.utils import extend_schema
from rest_framework import mixins, status
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from food.models import Category
from food.serializers.category import (CategoryModelSerializers,
                                       CategoryCreateSerializers,
                                       CategoryRetrieveSerializers)


@extend_schema(tags=("category",))
class CategoryViewSet(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializers
    permission_classes = [AllowAny]

    def get_serializer_class(self, *args, **kwargs):
        action = self.action
        print(action)
        if self.action in ["create", "partial_update"]:
            return CategoryCreateSerializers
        if self.action in ["retrieve"]:
            return CategoryRetrieveSerializers
        return self.serializer_class

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            "message": f"Category '{instance.name}' deleted successfully"
        },
            status=status.HTTP_204_NO_CONTENT,
        )
