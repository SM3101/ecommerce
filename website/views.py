from django.shortcuts import render
from . models import Category, SubCategory, Products

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

def subcategory_display(request):
    categories = Category.objects.all()
    subcategory_show = SubCategory.objects.all()
    #print(subcategories.values())
    #temp_sub = SubCategory.objects.get(id=select)
    products = Products.objects.all()
    data = {
        'categories':categories,
        'subcategories':subcategory_show,
        'products':products,
        #'temp':temp_sub,
    }
    return render(request, 'subpage.html', data)
