from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from food.models.category import Category
from food.serializers.food import FoodModelSerializer


class CategoryModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "id", "name",


class CategoryRetrieveSerializers(serializers.ModelSerializer):
    foods = FoodModelSerializer(many=True)

    class Meta:
        model = Category
        fields = "id", "name", "foods",


class CategoryCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "name",

    def validate_name(self, name):
        name = name.strip().title().replace(" ", "")
        if not name.isalpha() or len(name) <= 4:
            raise ValidationError(
                {
                    "status": False,
                    "message": "Only letters and must be more than 4 characters"
                }
            )
        if Category.objects.filter(name=name).exists():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Already yes field"
                }
            )

        return name
