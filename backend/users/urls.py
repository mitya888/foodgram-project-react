from django.urls import include, path

from .views import ListFollowView

urlpatterns = [
    path('users/subscriptions/', ListFollowView.as_view(), name='following_list'),
]
