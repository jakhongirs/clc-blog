from django.shortcuts import render
from django.http import JsonResponse
from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
@api_view(['GET', 'POST'])
def post_list(request):
    # get all the posts
    # serialize them
    # return json
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse({'posts': serializer.data}, safe=False)

    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
