from django.shortcuts import render
from . models import Category, SubCategory, Products

# Create your views here.
def home(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    print(subcategories.values())
    products = Products.objects.all()
    data = {
        'categories':categories,
        'subcategories':subcategories,
        'products':products,
    }
    return render(request, 'homepage.html', data)