from django import forms
from .models import Restaurant, Dish, Review

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            "user",
            "restaurant_name",
            "street",
            "zip_code",
            "state_or_province",
            "country",
            "telephone"
        ]

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = [
            "user",
            "dish_name",
            "description",
            "price",
            "restaurant"
        ]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "user",
            "rating",
            "comment"
        ]