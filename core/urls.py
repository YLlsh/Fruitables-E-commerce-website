from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns=[
    path("",index,name="index"),
    path('add_to_cark/<int:id>/', add_to_cark, name="add_to_cark"),
    # path('vege/<int:id>/<path:path>/', vegetable_to_cart, name="vegetable_to_cart"),
    path('shop/', shop_random, name="shop")
]