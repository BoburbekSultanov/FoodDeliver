from rest_framework import routers

from food.views import (FoodViewSet,
                        CategoryViewSet)

router = routers.DefaultRouter()
router.register(r"food", FoodViewSet, basename="food")
router.register(r"category", CategoryViewSet, basename="category")

urlpatterns = [
              ] + router.urls
