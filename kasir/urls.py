from django.contrib import admin
from django.urls import path, include
from kasir.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('bout', about, name='about'),
    path('barang/', include('barang.urls')),
]