#app urls

from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name="home"),
    path('blogpost/<int:id>',views.blogpost,name="blogpost"),
]