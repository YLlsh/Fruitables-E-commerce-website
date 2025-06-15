from django.urls import path
from account.views import *

urlpatterns =[
    path('sign_in/',sign_in,name="sign_in"),
    path('sign_up/',sign_up, name="sign_up"),
    path('log_out/',log_out,name="log_out"),
]