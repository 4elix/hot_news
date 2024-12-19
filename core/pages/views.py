from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Category, Article, Comments
from .serializers import CategorySerializer, ArticleSerializer, CommentSerializers
from .pagination_settings import ClassicPagination, MiniPagination


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['pk']
    pagination_class = MiniPagination

    def get_serializer_context(self):
        return {'request': self.request}


class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['pk', 'quantity_views']
    pagination_class = ClassicPagination

    def get_serializer_context(self):
        return {'request': self.request}


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializers

    def get_queryset(self):
        return Comments.objects.filter(article_id=self.kwargs['articles_pk'])

    def get_serializer_context(self):
        return {'article_id': self.kwargs['articles_pk']}
