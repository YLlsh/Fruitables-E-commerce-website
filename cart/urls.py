from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path("", cart, name="cart"),
    path("plus/<int:p>/", cart_modify_plus),
    path("minos/<int:m>/", cart_modify_minos),
]