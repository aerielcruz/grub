from django.shortcuts import render, redirect
from .forms import RegisterForm

from django.contrib.auth.models import User

#def logout(request):
 #	user = request.user
 #	logout(request, user)
#
 #	return redirect("/")

def registration(request):
	form = RegisterForm()
	if (request.method=="POST"):
		form = RegisterForm(request.POST)
		if (form.is_valid()):
			username = form.cleaned_data["username"]
			email = form.cleaned_data["email"]
			password = form.cleaned_data["password"]
			User.objects.create_user(username=username, email=email, password=password)

			return redirect("bauth:success")

	context = {
		"title": "Register Here",
		"message": "Create an account today!",
		"form": form,
	}
	return render(request, "registration/register.html", context)

def success(request):
	context = {
		"title": "User Created"
	}
	return render(request, "basicauth/notice/success.html", context)