from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from posts.models import Post
from posts.serializers import PostSerializer, PostCreateSerializer


class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        if request.user.is_authenticated:
            serializer = PostCreateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)


class PostDetailView(APIView):
    def get(self, request):
        pass
    
    def put(self, request):
        pass

    def delete(self, request):
        pass
