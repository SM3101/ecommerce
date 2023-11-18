from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('subcategory/<id>', views.subcategory_display, name="subpage"),
    path('add_to_cart/<id>', views.add_to_cart, name = "add_to_cart"),
    path('cart', views.cart, name="cart"),
    path('delete_cart_item/<id>', views.delete_cart_item, name="delete_cart_item"),
]