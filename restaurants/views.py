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


def read(request, id):
    obj = Restaurant.objects.get(pk=id)
    title = obj.name
    info = {
        "User": obj.user,
        "Name": obj.name,
        "Address": obj.address,
        "Country": obj.country,
        "Phone": obj.phone,
        "Category": obj.category,
        "Opening hours": obj.opening_hours,
        "Created at": obj.created_at,
		"Updated at": obj.updated_at,
    }
	
    context = {
		"title": title,
		"obj": obj,
		"info": info,
	}
    return render(request, "restaurants/read.html", context)



