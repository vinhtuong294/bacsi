from .models import UserModel
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'fullname', 'gender', 'birthday','telephone','role']