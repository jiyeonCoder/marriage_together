from django.shortcuts import render
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from users.models import User
from users.serializers import CustomTokenObtainPairSerializer, UserSerializer, UserProfileSerializer

class UserView(APIView):
    #사용자 정보 조회
    def get(self, request):
        return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)

    #회원가입
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message: User created successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
    
    #회원 정보 수정
    def put(self, request):
        return Response("message: User updated successfully")

    #회원 탈퇴
    def delete(self, request):
        return Response("message: User deleted successfully")
        

class TokenObtainPairView(TokenObtainPairView):
    #serializer_class = TokenObtainPairSerializer


class mockView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        print(request.user)
        user = request.user
        user.is_admin = True
        user.save()
        return Response("message: get 요청")


class ProfileView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)