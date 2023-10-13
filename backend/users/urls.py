from django.contrib import admin
from django.urls import path, include
from users import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.UserView.as_view(),name='user_view'),
    path('signup/', views.UserView.as_view(),name='user_view'),
    path('login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('login/', views.UserView.as_view(), name='user_view'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('mock/', views.mockView.as_view(),name='mock_view'),
    path('api/token/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('myprofile/', views.MyProfileView.as_view(), name='my_profile_view'),
    # path('<int:user_id>/profile/', views.ProfileView.as_view(), name='profile_view'),
    path('<int:user_id>/profile/', views.MyProfileView.as_view(), name='profile_view'),
    path('<int:profile_id>/like/', views.LikeView.as_view(), name='like_view'),
]
