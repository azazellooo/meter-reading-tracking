from django.contrib.auth.views import LoginView
from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from .views import MeterViewSet, api_root, MeterDetail
# router = routers.DefaultRouter()
# router.register(r'meters', views.MeterViewSet)
# app_name = 'api'

urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('meters/', MeterViewSet.as_view({'get': 'list', 'post': 'create'}), name='meters'),
    path(r'meters/<uuid:pk>', MeterDetail.as_view(), name='meter-detail'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
])

# urlpatterns = format_suffix_patterns([
#     path('posts/',
#          views.PostList.as_view(),
#          name='post-list'),
#     path('posts/<int:pk>/',
#          views.PostDetail.as_view(),
#          name='post-detail'),
#     path('users/',
#          views.UserList.as_view(),
#          name='user-list'),
#     path('users/<int:pk>/',
#          views.UserDetail.as_view(),
#          name='user-detail')
# ])