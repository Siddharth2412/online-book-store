from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from store.models.category import Category
from django.views import  View
from store.models.product import  Product

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)

        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        prod = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            prod = Product.get_all_products_by_categoryid(categoryID)
        else:
            prod = Product.get_all_products()

        data = {}
        data['prod'] = prod
        data['categories'] = categories
        data['products'] = products

        print('you are : ', request.session.get('email'))

        return render(request , 'cart.html' , data )

