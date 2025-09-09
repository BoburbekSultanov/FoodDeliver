from django.db import models
from django.db.models import CASCADE


# Create your models here.
# Crud food
# -name
# -price
# -category
# -status (boolen)
# -photos
# -description
# -bonus_price
# -rate
# -bonus_section

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "api_categories"


class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=True)
    description = models.TextField()
    bonus_price = models.PositiveIntegerField(default=0)
    rate = models.PositiveSmallIntegerField(default=0)
    bonus_section = models.CharField(max_length=5, null=True, blank=True) # 6 / 1

    category = models.ForeignKey(Category, on_delete=CASCADE, related_name="category", default=1)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "api_foods"


class Image(models.Model):
    image_url = models.TextField()
    food = models.ForeignKey(Food, on_delete=CASCADE, related_name="images")

    class Meta:
        db_table = "api_images"
