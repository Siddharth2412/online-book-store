from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from django.views import View
from store.models.contact import Feedback


# Create your views here.

def home(request):
    cart = request.session.get('cart')
    feedback= Feedback.objects.all()
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products_by_categoryid(1)[ :8]
        twale = Product.get_all_products_by_categoryid(2)[ :8]
        elevan= Product.get_all_products_by_categoryid(4)[ :8]
        ten = Product.get_all_products_by_categoryid(6)[ :8]
    
    data = {}
    data['products'] = products
    data['categories'] = categories
    # jay
    data['twale'] = twale
    data['elevan'] = elevan
    data['ten']= ten
    data['feedback']= feedback
    



    print('you are : ', request.session.get('email'))
    return render(request, "home1.html", data)
# return render (request,"home.html")


class Index(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

        # return redirect('homepage')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()

    data = {}
    data['products'] = products
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, "index.html", data)




def product(request,myid):
    product = Product.objects.filter(id=myid)
    categories = Category.get_all_categories()


    return render(request,"Product_Page.html",{'product':product[0],'categories':categories})


def search(request):
    aap=request.GET['pruth']
    if len(aap)>48:
        Products=[]
    else:
        productname = Product.objects.filter(Book_name__icontains=aap)
        productpublisher = Product.objects.filter(Publisher_name__icontains=aap)

        Products = productname.union(productpublisher)
    
    categories = Category.get_all_categories()

    return render(request,"search.html",{'desc':Products,'aap':aap,'categories':categories})


def feedback(request):
    if request.method=="POST":
        message=request.POST.get('message',"")
        line2=request.POST.get('message2',"")
        line3=request.POST.get('message3',"")
        line4=request.POST.get('message4',"")
        f_name=request.POST.get('f_name',"")
        email=request.POST.get('email',"")
        feedback=Feedback(Comment=message,line2=line2,line3=line3,line4=line4, F_Name=f_name,Email=email)
        feedback.save()
        return redirect("home")
    
    # data = {}
    # data['error'] = eror
    # data['values'] = value
    # if (not feedback.Comment)>30:
    #     error = "Only write 30 words in line1 !!"
    return render(request,"feedback.html")