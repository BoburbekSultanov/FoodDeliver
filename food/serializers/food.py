from rest_framework import serializers

from food.models.food import Food


class FoodModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "id", "name", "price", "description", "bonus_price", "image_url", "category",



