from django import forms

from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ["username", "email", "password"]
		widgets = {
			"password": forms.PasswordInput() # Cant see pass when typed
		}