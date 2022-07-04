#app urls

from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('productview/<int:id>',views.productview,name="productview"),
    path('placeorder/',views.placeorder,name="placeorder"),
    path('search/',views.search,name="search"),
]