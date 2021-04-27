from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('server.urls') ),
 ]