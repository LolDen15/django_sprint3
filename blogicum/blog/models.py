from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    title = models.CharField('Название', max_length=256, blank=False)
    text = models.TextField('Текст', blank=False)
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text='Если установить дату и время в будущем '
                  '— можно делать отложенные публикации.'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор публикации',
        blank=False
    )
    location = models.ForeignKey(
        'Location',
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Местоположение',
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Категория',
        null=True,
        blank=False
    )
    is_published = models.BooleanField(
        verbose_name='Опубликовано',
        default=True,
        help_text='Снимите галочку, чтобы скрыть публикацию.',
        blank=False
    )
    created_at = models.DateTimeField(
        'Добавлено',
        auto_now_add=True, blank=False)

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField('Заголовок', max_length=256, blank=False)
    description = models.TextField('Описание', blank=False)
    slug = models.SlugField(
        'Идентификатор',
        unique=True,
        help_text='Идентификатор страницы для URL; '
                  'разрешены символы латиницы, цифры, дефис и подчёркивание.'
    )
    is_published = models.BooleanField(
        verbose_name='Опубликовано',
        default=True,
        help_text='Снимите галочку, чтобы скрыть публикацию.',
        blank=False
    )
    created_at = models.DateTimeField(
        'Добавлено',
        auto_now_add=True,
        blank=False
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Location (models.Model):
    name = models.CharField('Название места', max_length=256, blank=False)
    is_published = models.BooleanField(
        verbose_name='Опубликовано',
        default=True,
        blank=False
    )
    created_at = models.DateTimeField(
        'Добавлено',
        auto_now_add=True,
        blank=False
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name
