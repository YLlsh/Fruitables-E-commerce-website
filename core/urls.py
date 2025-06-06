from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns=[
    path("",index,name="index"),
    path('fruit/<id>/', fruit_to_cart, name="fruit_to_cart"),
    path('vege/<id>/', vegetable_to_cart, name="vegetable_to_cart")
]