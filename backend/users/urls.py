from django.urls import include, path

from .views import ListFollowView, FollowApiView

urlpatterns = [
    path('users/subscriptions/', ListFollowView.as_view(), name='following_list'),
    path('users/<pk>/subscribe/', FollowApiView.as_view(), name='subscribe_list'),
]
