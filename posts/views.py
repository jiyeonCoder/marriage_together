from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class Comment(APIView):
    def get(self, request):
        """post의 댓글을 보여줍니다."""

    def post(self, request):
        """각 post에 댓글을 생성합니다."""

    def put(self, request):
        """댓글을 수정"""

    def delete(self, request):
        """댓글을 삭제"""