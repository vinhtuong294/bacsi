from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import UserModel
from .serializers import UserSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

class UserViewSet(viewsets.ModelViewSet):

    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        print("Received data: %s", request.data)  # Log dữ liệu nhận được
        return super().create(request, *args, **kwargs)
    # permission_classes = [IsAuthenticated]

def login(request):
    return render(request, 'login/login.html')

def password_reset(request):
    return render(request, 'password_reset/password_reset.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        fullname = request.POST['fullname']
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password == password_confirmation:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Đăng ký thành công!')
            return redirect('login')
        else:
            messages.error(request, 'Mật khẩu không khớp!')

    return render(request, 'register/register.html')
