from rest_framework import serializers

from food.serializers import CategoryModelSerializers
from restaurant.models import Menu, Restaurant


class MenuModelSerializers(serializers.ModelSerializer):
    categories = CategoryModelSerializers(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = ("name", "restaurant", "categories")


class RestaurantModelSerializers(serializers.ModelSerializer):
    menus = MenuModelSerializers(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ("id",
                  "name",
                  "address",
                  "phone_number",
                  "work_time_start",
                  "work_time_end",
                  "deliver_fee",
                  "menus",
                  )
