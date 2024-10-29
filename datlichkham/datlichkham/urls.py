# urls.py của ứng dụng chính
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from doctors.views import UserViewSet

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('doctors.urls')),
]
