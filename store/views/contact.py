from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.contact import Contact
from django.contrib import messages
from store.models.category import Category






def contact(request):
         if request.method=="POST":
                  name=request.POST.get('name','')
                  phone=request.POST.get('phone','') 
                  email=request.POST.get('email','')
                  message=request.POST.get('message','')
                  contact=Contact(Name=name,Phone=phone,Email=email,Message=message)
                  # messages.info(request,'Your message sent successfully')
                  contact.save()
                  messages.info(request,'Your message sent successfully')
                  return redirect('home')    
    
         categories = Category.get_all_categories()
         data={}
         data['categories'] = categories

         return render(request,"contact.html",data)


def about(request):
         categories = Category.get_all_categories()
         data={}
         data['categories'] = categories

         return render(request,"About_us.html",data)