from django import forms
from .models import Category, Restaurant, Dish, Review

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        # exclude = ()
        fields = [
            "category",
            "is_active"
        ]

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            "name",
            "address",
            "country",
            "phone",
            "category",
            "opening_hours"
        ]

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = [
            "dish",
            "description",
            "price",
            "restaurant",
            "category"
        ]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "rating",
            "comment",
            "restaurant"
        ]