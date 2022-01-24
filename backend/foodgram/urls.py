from django.contrib import admin
from django.urls import include, path
from djoser.views import TokenCreateView, TokenDestroyView

api_patterns = [
    path('', include('users.urls')),
    path('auth/token/login/', TokenCreateView.as_view(), name='login'),
    path('auth/token/logout/', TokenDestroyView.as_view(), name='logout'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_patterns)),

]
