from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    quantity_views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    description = models.TextField(verbose_name='Описание')
    is_published = models.BooleanField(default=True, verbose_name='Опубликованная')
    is_banned = models.BooleanField(default=False, verbose_name='Заблокированная статья')
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создание')
    update_datetime = models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    slug = models.SlugField(max_length=255)

    def first_photo(self):
        try:
            img = self.gallery_article.all().first()
            return img.photo.url
        except Exception as error:
            print(error)
            return '-'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class GalleryArticle(models.Model):
    photo = models.ImageField(upload_to='image/articles/', verbose_name='')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='gallery_article', verbose_name='')


class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='')
    content = models.TextField(verbose_name='')
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name='')
    update_datetime = models.DateTimeField(auto_now=True, verbose_name='')


class FavoriteArticle(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
