from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "resto"
urlpatterns = [
    path("", views.index, name="index"),
	path('create/<str:category>', views.create, name="create"),
	path('read/<str:category>/<int:id>', views.read, name="read"), #<int:id> placeholder, id is variable
	path('update/<str:category>/<int:id>', views.update, name="update"),
	path('delete/<str:category>/<int:id>', views.delete, name="delete"),

	path('success/', views.success, name="success"),
	path('deleted/', views.deleted, name="deleted"),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)