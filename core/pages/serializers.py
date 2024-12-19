from rest_framework import serializers

from .models import Category, Article, Comments, GalleryArticle


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryArticle
        fields = ['pk', 'photo']


class ArticleSerializer(serializers.ModelSerializer):
    gallery = GallerySerializer(many=True, source='gallery_article')

    class Meta:
        model = Article
        fields = '__all__'


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['pk', 'author', 'content', 'create_datetime', 'update_datetime']

    def create(self, validated_data):
        article_id = self.context['article_id']
        return Comments.objects.create(article_id=article_id, **validated_data)
