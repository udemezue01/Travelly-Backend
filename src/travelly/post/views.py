from django.shortcuts import render



from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import PostSerializer

from .models import Post


class PostListView(APIView):

	def get(self, request, format=None):

		posts  	= Post.objects.all()
		serializer = PostSerializer(posts, many=True)
		return Response(serializer.data)




