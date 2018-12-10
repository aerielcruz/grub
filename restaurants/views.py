from django.shortcuts import render, redirect

from .forms import RestaurantForm, DishForm, ReviewForm
from .models import Restaurant, Dish, Review

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    # Get data from the database
    # Output to html file

    restaurants = Restaurant.objects.all()
    dishes = Dish.objects.all()
    context = {
        "title": "Restaurant List",
        "restaurantlist": restaurants,
        "dishlist": dishes
    }

    return render(request, "restaurants/index.html", context)