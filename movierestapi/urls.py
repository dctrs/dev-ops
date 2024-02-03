from django.contrib import admin
from django.urls import path, include
from movieapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('movieapp.urls')),
]
