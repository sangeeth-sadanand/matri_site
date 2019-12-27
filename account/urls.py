from django.urls import path, include
from . import views

# from matri_site.config import *
# data = load_config()
# print(data)

urlpatterns = [
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('register/', views.registration_page, name="register"),
    path('ajax/email_availability', views.email_avalability),
    path('view-details',views.edit_details, name = 'edit_details'),
    path('notification-page',views.notification, name = 'notification'),
    path('ajax/notification-count',views.notification_count, name = 'notification_count'),
]
"""
    path('password_change/',views.home),
    path('password_change/done/',views.home),
    path('password_reset/',views.home),
    path('password_reset/done/',views.home),
    
    path('reset/done/',views.home),
"""
