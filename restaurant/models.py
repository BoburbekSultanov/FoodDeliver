from django.db import models


# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=30)
    work_time_start = models.TimeField()
    work_time_end = models.TimeField()
    deliver_fee = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "api_restaurant"


class Menu(models.Model):
    name = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="menus", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "api_menu"
