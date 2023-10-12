from django.urls import path
from posts import views

urlpatterns = [
    path('', views.PostView.as_view(), name='post_view'),
    path('<int:post_id>/comment/', views.CommentView.as_view(), name='comment_create'),
    path('comment/<int:comment_id>/', views.CommentView.as_view(), name='comment_edit'),
    path('<int:post_id>/', views.PostDetailView.as_view(), name='post_detail_view'),
]