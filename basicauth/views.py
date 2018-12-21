from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UserUpdateForm, UserProfileUpdateForm
from django.contrib import messages

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

			messages.success(request, f'Your account has been created! You may now login.')
			return redirect("bauth:login")

	context = {
		"title": "Register Here",
		"message": "Create an account today!",
		"form": form,
	}
	return render(request, "registration/register.html", context)

@login_required
def profile(request):
	if (request.method=="POST"):
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = UserProfileUpdateForm(request.POST, 
										request.FILES, 
										instance=request.user.userprofile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			# return redirect("bauth:success")
			messages.success(request, f'Your account has been updated!')
			return redirect("bauth:profile")
	else:	
		u_form = UserUpdateForm(instance=request.user)
		p_form = UserProfileUpdateForm(instance=request.user.userprofile)
	
	context = {
		"u_form": u_form,
		"p_form": p_form,
		"profile_page": "active"
	}

	return render(request, 'basicauth/profile.html', context)

def success(request):
	context = {
		"title": "User Created"
	}
	return render(request, "basicauth/notice/success.html", context)