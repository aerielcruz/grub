from django import forms
from .models import Category, Restaurant, Dish, Review

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        # exclude = ()
        fields = [
            "name",
            "is_active"
        ]

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            "user",
            "name",
            "address",
            "country",
            "phone_number",
            "category",
            "opening_hours"
        ]

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = [
            "name",
            "description",
            "price",
            "restaurant",
            "category"
        ]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "user",
            "rating",
            "comment",
            "restaurant"
        ]