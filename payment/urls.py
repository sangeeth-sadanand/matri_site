from django.urls import path, include
from . import views
#from matri_site.config import *
#data = load_config()
#print(data)

urlpatterns = [
    path('user-payment/',views.user_payment, name = 'user_payment'),
    path('user-upayment/',views.user_upayment, name = 'user_upayment'),
    path('user-payment-page/',views.user_payment_page, name = 'user_payment_page'),
]


