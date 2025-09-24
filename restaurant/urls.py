from django.urls import path

from restaurant.views import RestaurantDetailApiView

urlpatterns = [
    path("list/", RestaurantDetailApiView.as_view(), name="restaurant_list")
]
