from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from core.views import *
urlpatterns = [
    path("", product_random, name="product_detail") 

]