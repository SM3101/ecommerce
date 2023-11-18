from django.shortcuts import render, redirect
from . models import Category, SubCategory, Products, OrderItem

# Create your views here.
def home(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    #print(subcategories.values())
    products = Products.objects.all()
    data = {
        'categories':categories,
        'subcategories':subcategories,
        'products':products,
    }
    return render(request, 'homepage.html', data)

def subcategory_display(request, id):
    categories = Category.objects.all()
    subcategory_show = SubCategory.objects.all()
    #print(subcategories.values())
    temp_sub = SubCategory.objects.get(id=id)
    products = Products.objects.filter(subcategory=temp_sub)
    data = {
        'categories':categories,
        'subcategories':subcategory_show,
        'products':products,
        'temp':temp_sub,
    }
    return render(request, 'subpage.html', data)

def add_to_cart(request, id):
    product_item = Products.objects.get(id=id)
    order_item = OrderItem.objects.create(product=product_item)
    order_item.save()
    return redirect(home)

def cart(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    order_items = OrderItem.objects.all()
    data = {
        'order_items':order_items,
        'categories':categories,
        'subcategories':subcategories,
    }
    return render(request, 'cart.html', data)

def delete_cart_item(request, id):
    order_item = OrderItem.objects.get(id=id)
    order_item.delete()
    return redirect(cart)