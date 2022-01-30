from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count


from .models import Follow
from .serializers import FollowSerializer, ListFollowingSerializer
from .pagination import BasePageNumberPagination


User = get_user_model()


class FollowApiView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return User.objects.all()

    def post(self, request, pk: int):
        author = self.get_object()
        request.user.following.add(author)

        # data = {'user': request.user.id, 'author': pk}
        # serializer = FollowSerializer(data=data, context={'request': request})
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        return Response({''}, status=status.HTTP_201_CREATED)

    def delete(self, request, pk: int):
        author = self.get_object()
        request.user.following.remove(author)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListFollowView(generics.ListAPIView):
    serializer_class = ListFollowingSerializer
    pagination_class = BasePageNumberPagination

    def get_queryset(self):
        user = self.request.user
        return user.following.all().annotate(recipes_count=Count('recipes'))
