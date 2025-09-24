from django.db import models

from restaurant.models import Menu


class Category(models.Model):
    name = models.CharField(max_length=100)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="categories", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "api_categories"
