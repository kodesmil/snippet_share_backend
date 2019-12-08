from django.urls import include, path
from rest_framework import routers
from snippets import views as snippets_views
from reports import views as reports_views
from comments import views as comments_views
from django.contrib import admin
from django.urls import path

router = routers.DefaultRouter()
router.register(r'collections', snippets_views.CollectionViewSet)
router.register(r'snippets', snippets_views.SnippetViewSet)
router.register(r'comments', comments_views.CommentViewSet)
router.register(r'tags', snippets_views.TagViewSet)
router.register(r'users', snippets_views.UserViewSet)
router.register(r'reports', reports_views.ReportViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

