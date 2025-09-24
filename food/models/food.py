from django.db import models

from food.models.category import Category


class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=True)
    description = models.TextField()
    bonus_price = models.PositiveIntegerField(default=0)
    rate = models.PositiveSmallIntegerField(default=0)
    image_url = models.URLField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="foods")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "api_foods"


class BonusFood(models.Model):
    buy_count = models.PositiveIntegerField(default=0)
    add = models.PositiveIntegerField(default=0)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="bonus")

    def __str__(self):
        return "Bonus Food"

    class Meta:
        db_table = "api_bonus"
