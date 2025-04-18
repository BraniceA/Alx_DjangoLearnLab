from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Like
from notifications.utils import create_notification  # utility we'll create

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        return Response({'detail': 'Already liked'}, status=status.HTTP_400_BAD_REQUEST)
    
    if post.author != request.user:
        create_notification(
            recipient=post.author,
            actor=request.user,
            verb='liked your post',
            target=post
        )
    return Response({'detail': 'Post liked'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    try:
        like = Like.objects.get(user=request.user, post__pk=pk)
        like.delete()
        return Response({'detail': 'Post unliked'})
    except Like.DoesNotExist:
        return Response({'detail': 'Like does not exist'}, status=status.HTTP_400_BAD_REQUEST)


from .models import Notification
from .serializers import NotificationSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_notifications(request):
    notifications = Notification.objects.filter(recipient=request.user)
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)
