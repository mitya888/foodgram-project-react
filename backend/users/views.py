from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count
from drf_yasg.utils import swagger_auto_schema


from .models import Follow
from .pagination import BasePageNumberPagination
from . import serializers


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
        return Response({'&&&'}, status=status.HTTP_201_CREATED)

    def delete(self, request, pk: int):
        author = self.get_object()
        request.user.following.remove(author)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListFollowView(generics.ListAPIView):
    serializer_class = serializers.ListFollowingSerializer
    pagination_class = BasePageNumberPagination

    def get_queryset(self):
        user = self.request.user
        return user.following.all().annotate(recipes_count=Count('recipes'))

    @swagger_auto_schema(query_serializer=serializers.RecipeLimitSerializer)
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
        # return super().get(request, *args, **kwargs)