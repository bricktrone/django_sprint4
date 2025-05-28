"""imports."""
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Category(models.Model):
    """Category model."""

    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(verbose_name='Идентификатор',
                            help_text='Идентификатор страницы для URL;\
 разрешены символы латиницы, цифры, дефис и подчёркивание.',
                            unique=True)
    is_published = models.BooleanField(
        default=True, verbose_name='Опубликовано', help_text='Снимите галочку\
, чтобы скрыть публикацию.')
    created_at = models.DateTimeField(
        verbose_name='Добавлено', auto_now_add=True)

    class Meta:
        """Meta class."""

        verbose_name = ("категория")
        verbose_name_plural = ("Категории")

    def __str__(self):
        """Name of model."""
        return self.title


class Location(models.Model):
    """Location model."""

    name = models.CharField(max_length=256, verbose_name='Название места')
    is_published = models.BooleanField(
        default=True, verbose_name='Опубликовано', help_text='Снимите галочку\
, чтобы скрыть публикацию.')
    created_at = models.DateTimeField(
        verbose_name='Добавлено', auto_now_add=True)

    class Meta:
        """Meta class."""

        verbose_name = ("местоположение")
        verbose_name_plural = ("Местоположения")

    def __str__(self):
        """Name of model."""
        return self.name


class Post(models.Model):
    """Post model."""

    title = models.CharField(max_length=256, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(verbose_name='Дата и время публикации',
                                    help_text='Если установить дату и время в\
 будущем — можно делать отложенные публикации.')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Местоположение'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория'
    )
    is_published = models.BooleanField(
        default=True, verbose_name='Опубликовано', help_text='Снимите галочку,\
 чтобы скрыть публикацию.')
    created_at = models.DateTimeField(
        verbose_name='Добавлено', auto_now_add=True)
    image = models.ImageField('Фото', upload_to='posts_images', blank=True)

    @property
    def username(self):
        return self.author.username

    class Meta:
        """Meta class."""

        verbose_name = ("публикация")
        verbose_name_plural = ("Публикации")

    def __str__(self):
        """Name of model."""
        return self.title


class Comment(models.Model):
    """Comment model"""

    text = models.TextField(verbose_name='Текст')
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='Пост'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор комментария'
    )
    created_at = models.DateTimeField(verbose_name='Добавлено',
                                      auto_now_add=True)

    class Meta:
        """Meta class"""

        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        """Text of comment"""
        return self.text
