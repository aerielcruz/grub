from django.shortcuts import render, redirect

from .forms import CategoryForm, RestaurantForm, DishForm, ReviewForm
from .models import Category, Restaurant, Dish, Review

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

# def create(request):

# def read(request, id):
#     obj = Restaurant.objects.get(pk=id)
#     title = obj.restaurant

#     context = {
#         "title": title,
#         "obj": obj
#     }
#     return render(request, "restaurant/read.html", context)



