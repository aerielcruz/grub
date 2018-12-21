from django.http import HttpResponse
from django.shortcuts import render

from restaurants.models import Restaurant

def home(request):
	restaurants = Restaurant.objects.all()
	context = {
		"title": "Welcome to home",
		"restaurantlist": restaurants,
	}
	return render(request, "index.html", context)

def about(request):
	context = {
		"title": "About Page",
	}
	return render(request, "pages/about.html", context)

def contact(request):
	context = {
		"title": "Contact Page",
	}
	return render(request, "pages/contact.html", context)