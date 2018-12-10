from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	context = {
		"title": "Welcome to home",
	}
	return render(request, "index.html", context)

# def about(request):
# 	context = {
# 		"title": "About Page",
# 	}
# 	return render(request, "pages/about.html", context)

# def contact(request):
# 	context = {
# 		"title": "Contact Page",
# 	}
# 	return render(request, "pages/contact.html", context)