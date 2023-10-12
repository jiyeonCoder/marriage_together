from dataclasses import field
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from users.models import User, Profile

class UserProfileSerializer(serializers.ModelSerializer):
    followings = serializers.StringRelatedField(many=True)
    followers = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ("id", "email", "followings", "followers", "article_set","like_articles")
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        nickname = user.nickname
        user.save()
        return user
    
    def update(self, validated_data):
        user = super().update(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token
    

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
    

class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("image", "fullname", "age", "introduce_me", "job", "religion", "my_character", "purpose_to_join")
