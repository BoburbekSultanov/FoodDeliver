from django.urls import path

from food.views import (CategoryCreateApiView,
                        CategoryUpdateApiView,
                        CategoryDestroyAPIView,
                        FoodListCreateApiView,
                        FoodDApiView, CategoryDetailApiView)

urlpatterns = [
    path("category/", CategoryCreateApiView.as_view(), name="category_create_list"),
    path("category/update/<int:pk>", CategoryUpdateApiView.as_view(), name="category_update"),
    path("category/delete/<int:pk>", CategoryDestroyAPIView.as_view(), name="category_delete"),
    path("category/detail/<int:pk>", CategoryDetailApiView.as_view(), name="category_detail"),
]

urlpatterns += [
    path("create/list/", FoodListCreateApiView.as_view(), name="food_create_list"),
    path("<int:pk>", FoodDApiView.as_view(), name="food"),
]
