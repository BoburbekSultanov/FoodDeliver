from rest_framework import serializers

from food.models import Food, Category, Image


class CategoryModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "id", "name",
        read_only_fields = "id",


class FoodModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "id", "name", "price", "description", "bonus_price", "category",
        read_only_fields = "id",


class ImageCreateModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "image_url",
        read_only_fields = "food",
