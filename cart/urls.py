from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path("", cart, name="cart"),
    path("plus/<int:p>/", cart_modify_plus, name="cart_modify_plus"),
    path("minos/<int:m>/", cart_modify_minos,  name="cart_modify_minos"),
    path("delete/<int:d>/", cart_delete, name="cart_delete")
]