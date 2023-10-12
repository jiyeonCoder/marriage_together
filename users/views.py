from django.shortcuts import render
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from users.models import Profile, User
from users.serializers import CustomTokenObtainPairSerializer, UserSerializer, UserProfileSerializer, ProfileSerializer, ProfileCreateSerializer
from cities_light.models import Country, City

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
    

class mockView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        print(request.user)
        user = request.user
        user.is_admin = True
        user.save()
        return Response("message: get 요청")


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    
class MyProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, user_id):
        profile = get_object_or_404(Profile, id=user_id)
        if request.user == profile.user:
            # profile = get_object_or_404(Profile, id=user_id)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': '권한이 없습니다.'}, status=status.HTTP_401_UNAUTHORIZED)
    
    def post(self, request, user_id):
        serializer = ProfileCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, user_id):
        profile = get_object_or_404(Profile, id=user_id)
        if request.user == profile.user:
            serializer = ProfileCreateSerializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)


class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, user_id):
        profile = get_object_or_404(Profile, id=user_id)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CountryView(APIView):
    def get(self, request ):
        countries = Country.objects.all().values_list("id","name")
        return Response(countries)

class CityView(APIView):
    def get(self, request, country_id ):
        cities = City.objects.filter(country_id = country_id).values_list("id","name")
        return Response(cities)   

    
