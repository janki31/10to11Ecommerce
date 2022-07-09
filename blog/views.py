from django.shortcuts import render
from .models import Blogpost

# Create your views here.


def index(request):
    allpost=Blogpost.objects.all()
    return render(request,'blog/index.html',{"allpost":allpost})

def blogpost(request,id):
    postdata=Blogpost.objects.get(bid=id)
    return render(request,'blog/blogpost.html',{'postdata':postdata})
