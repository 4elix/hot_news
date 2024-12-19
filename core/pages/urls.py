from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()

router.register('categories', views.CategoryViewSet, basename='category')
router.register('articles', views.ArticleViewSet, basename='articles')

article_router = routers.NestedDefaultRouter(router, 'articles', lookup='articles')
article_router.register('comments', views.CommentViewSet, basename='comments-articles')

urlpatterns = router.urls + article_router.urls
