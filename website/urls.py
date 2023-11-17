from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('subcategory', views.subcategory_display, name="subpage")
]