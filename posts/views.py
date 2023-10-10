from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from posts.models import Post
from posts.models import Comment
from posts.serializers import CommentSerializer, PostSerializer, PostCreateSerializer


class PostView(APIView):
    permission_classes = [permissions.IsAuthenticated]
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
            return Response({'error': '권한이 없습니다.'}, status=status.HTTP_401_UNAUTHORIZED)


class PostDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        if request.user == post.user:
            serializer = PostCreateSerializer(post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        if request.user == post.user:
            post.delete()
            return Response({'게시글이 삭제되었습니다.'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        

class CommentView(APIView):
    def get(self, request):
        # author = request.data.get('author')
        # post = request.data.get('post')
        # post = get_object_or_404(Post, id=post_id)
        # comments = post.comment_set.all()
        # serializer = CommentSerializer(comments, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)
        """post의 댓글을 보여줍니다.  =>  PostSerializer에서 CommentSerializaer한 값을 가져옵니다. """ 

    def post(self, request):
        """
        author = request.user
         data = {
             "content": request.POST.get('content', None),
             "author": author.id
         }
        serializer = CommentSerializer(data=data)
        """

        """
        author = User.objects.get(pk=request.user)
        serializer = CommentSerializer(data=request.data, context={"author":author.id})
        """
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        """각 post에 댓글을 생성합니다."""

    def put(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        serializer = CommentSerializer(comment, data=request.data)
        if request.user == comment.user:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)
        """댓글을 수정"""

    def delete(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user == comment.user:
            comment.delete()
            return Response({'게시글이 삭제되었습니다.'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        
        """댓글을 삭제"""