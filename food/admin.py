from django.contrib import admin

from food.models.category import Category

from food.models.food import Food, BonusFood


# Register your models here.

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(BonusFood)
class BonusFoodAdmin(admin.ModelAdmin):
    pass
