from django.urls import path
from users import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # path('login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('signup/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
