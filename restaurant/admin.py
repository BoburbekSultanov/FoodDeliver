from django.contrib import admin

from restaurant.models import Menu, Restaurant


# Register your models here.


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    pass
