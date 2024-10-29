# views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import UserModel
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]
