from django.contrib import admin
from django.urls import path 
from CovidMap import views

urlpatterns = [
   # path("", views.index , name ="CovidMap"),
    path("",views.index,name = "index"),
    path("about", views.about , name ="about"),
    path("contact",views.contact , name = "contact"),
    

]