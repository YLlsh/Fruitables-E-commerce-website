from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns=[
    path("",index,name="index"),
    path('fruit/<int:id>/<path:path>/', fruit_to_cart, name="fruit_to_cart"),
    path('vege/<int:id>/<path:path>/', vegetable_to_cart, name="vegetable_to_cart"),
    path('shop/', shop_random, name="shop")
]