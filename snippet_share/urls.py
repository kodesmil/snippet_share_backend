from django.urls import include, path
from rest_framework import routers
from snippets import views
from django.contrib import admin
from django.urls import path

router = routers.DefaultRouter()
router.register(r'collections', views.CollectionViewSet)
router.register(r'snippets', views.SnippetViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'users', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

