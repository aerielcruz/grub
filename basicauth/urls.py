from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "bauth"
urlpatterns = [
	#path("login/", views.login, name="login")
	path("login/", LoginView.as_view(), name="login"),
	path("logout/", LogoutView.as_view(), name="logout"),
	#path("logout/", views.logout, name="logout"),
	path("register/", views.registration, name="register"),
	path("profile/", views.profile, name="profile"),

	path("success/", views.success, name="success")
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)