"""
URL configuration for e_commerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from core.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from cart.views import *
from account.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('core.urls')),
    path("account/",include('account.urls')),
    path("product_detail/", include('products.urls')),
    path("cart/",include('cart.urls')),
    path('search_result/<int:id>/',search_result, name="search_result"),
    path("contact/",TemplateView.as_view(template_name="core/contact.html"),name="contect"),
    path("testimonial/",TemplateView.as_view(template_name="core/testimonial.html"),name="testimonial"),
    path('verify_otp/', verify_otp, name='verify_otp'),
    path('suggest/', suggest_products, name='suggest'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
