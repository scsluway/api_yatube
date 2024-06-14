from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken.views import obtain_auth_token

from . import views


router = SimpleRouter()
router.register('posts', views.PostViewSet)
router.register('groups', views.GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    views.CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]
