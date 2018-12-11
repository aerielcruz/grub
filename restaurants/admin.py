from django.contrib import admin
from .models import Category, Restaurant, Dish, Review

# Register your models here.

admin.site.register(Category)
admin.site.register(Restaurant)
admin.site.register(Dish)
admin.site.register(Review)