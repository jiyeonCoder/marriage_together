from django.contrib import admin
from django.urls import path, include
from users import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.UserView.as_view(),name='user_view'),
    path('signup/', views.signup_view, name= 'signup'),
    # path('signup/', views.UserView.as_view(),name='user_view'),
    path('login/', views.login_view, name='login'),
    # path('login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('login/', views.UserView.as_view(), name='user_view'),
    path('logout/', views.logout_view(), name='logout'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('mock/', views.mockView.as_view(), name='mock_view'),
    path('api/token/', views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('myprofile/',
         views.MyProfileView.as_view(), name='my_profile_view'),
    path('<int:user_id>/profile/', views.ProfileView.as_view(), name='profile_view'),
    path('country/', views.CountryView.as_view()),
    path('city/<int:country_id>/', views.CityView.as_view()),
]
