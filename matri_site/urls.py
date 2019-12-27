from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from account.views import home
# from matri_site.config import *
# data = load_config()
# print(data)

urlpatterns = [   path('admin/', admin.site.urls),
                  path('',home, name='home'),
                  path('home/',home),
                  path('accounts/', include('account.urls')),
                  path('my-profile/', include('my_profile.urls')),
                  path('payment/',include('payment.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
