from django.http import HttpResponse
from django.shortcuts import render

from restaurants.models import Restaurant

def home(request):
	restaurants = Restaurant.objects.all()
	context = {
		"title": "Welcome to Grub",
		"restaurantlist": restaurants,
		"home_page": "active"
	}
	return render(request, "index.html", context)

def about(request):
	context = {
		"title": "About",
		"about_page": "active"
	}
	return render(request, "pages/about.html", context)

def contact(request):
	context = {
		"title": "Contact",
		"contact_page": "active"
	}
	return render(request, "pages/contact.html", context)