from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from . import views

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('password-reset/',views.password_reset, name="password_reset"),
    path('register/login/', views.login, name="register_login"),
]
