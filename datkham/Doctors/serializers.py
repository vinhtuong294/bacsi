from .models import UserModel, Doctor, Article
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'fullname', 'gender', 'birthday','telephone','role']

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'status', 'author']

class DoctorSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
    class Meta:
        model = Doctor
        fields = ['id', 'position', 'description', 'room_address','service_prices','department','user']