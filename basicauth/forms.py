from django import forms

from django.contrib.auth.models import User
from .models import UserProfile

class RegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username", "email", "password"]
		widgets = {
			"password": forms.PasswordInput() # Cant see pass when typed
		}

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username", "email"]

class UserProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ["image"]