from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = "bauth"
urlpatterns = [
	#path("login/", views.login, name="login")
	path("login/", LoginView.as_view(), name="login"),
	path("logout/", LogoutView.as_view(), name="logout"),
	#path("logout/", views.logout, name="logout"),
	path("register/", views.registration, name="register"),

	path("success/", views.success, name="success")
]