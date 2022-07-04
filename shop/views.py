from django.shortcuts import render
from .models import Product,Contact,Order
from math import *

# Create your views here.

def index(request):
    '''products=Product.objects.all()
    print("Allk products :- ",products)
    n=len(products)

    noofslides=ceil(n/4)
    print("total noofslide :- ", noofslides)
    allprods=[[products,range(1,noofslides),noofslides],[products,range(1,noofslides),noofslides]]'''
    allprods=[]
    catproducts=Product.objects.values('category','pid')

    categorys={i['category']for i in catproducts}
    #print("categorys :- ", categorys)
    for c in categorys:
        products = Product.objects.filter(category=c)
        #print("products :- ", products)
        n = len(products)
        noofslides = ceil(n / 4)
        allprods.append([products,range(1,noofslides),noofslides])


    return render(request,'shop/index.html',{'allprods':allprods})

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        emailid=request.POST.get('emailid','')
        mobileno=request.POST.get('mobileno','')
        feedback=request.POST.get('feedback','')

        con=Contact(name=name,emailid=emailid,mobileno=mobileno,feedback=feedback)
        con.save()

    return render(request,'shop/contact.html')

def productview(request,id):
    product=Product.objects.get(pid=id)
    return render(request,'shop/productview.html',{'product':product})

def placeorder(request):

    flag=False
    ver=False
    if request.method=="POST":
        cartitems=request.POST.get("cartitems","")
        firstname=request.POST.get("firstname","")
        lastname=request.POST.get("lastname","")
        email=request.POST.get("emailid","")
        address=request.POST.get("address","")
        mobileno=request.POST.get("mobno","")
        city=request.POST.get("city","")
        state=request.POST.get("state","")
        zipcode=request.POST.get("zipcode","")
        totalprice=request.POST.get("totalprice","")
        if(cartitems=="" or firstname=="" or lastname=="" or email=="" or address=="" or mobileno=="" or city=="" or state=="" or zipcode=="" or totalprice==""):
            ver=True

        else:
            order1=Order(items=cartitems,firstname=firstname,lastname=lastname,email=email,address=address,mobileno=mobileno,city=city,state=state,zipcode=zipcode,totalprice=totalprice)
            order1.save()
            flag=True

        return render(request,'shop/placeorder.html',{'flag':flag,'ver':ver})

    return render(request,'shop/placeorder.html')

def searchmatch(stext,item):
    if stext.lower() in item.product_name.lower() or stext.lower() in item.category.lower() or stext.lower() in item.product_desc.lower():
        return True
    else:
        return False

def search(request):
    stext=request.GET.get("searchtext","")
    allprods = []
    catproducts = Product.objects.values('category', 'pid')

    categorys = {i['category'] for i in catproducts}
    # print("categorys :- ", categorys)
    for c in categorys:
        products = Product.objects.filter(category=c)
        sprod=[item for item in products if searchmatch(stext,item)]
        # print("products :- ", products)
        n = len(sprod)
        noofslides = ceil(n / 4)
        if(n!=0):
            allprods.append([sprod, range(1, noofslides), noofslides])
        params={"allprods":allprods,"msg":""}
        if(len(allprods)==0):
            params={"msg":"please enter proper search detail"}

    return render(request,'shop/search.html',params)

