from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime 

from users.models import User


class Movies(models.Model):
    """Модель фильмов."""

    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Название фильма',
        help_text='Укажите название фильма'
    )
    description = models.TextField(
        verbose_name='О фильме',
        help_text='Напишите описание фильма'
    )    
    producer = models.CharField(
        max_length=150,
        verbose_name='Режиссер',
        help_text='Укажите режиссера',
        blank=True
    )
    years_movi =  models.IntegerField(
        verbose_name='Год выпука',
        help_text='укажите год выпуска фильма',
        validators=[
            MinValueValidator(1895),
            MaxValueValidator(datetime.datetime.now().year)
        ]
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор публикации',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['years_movi']
    
    def __str__(self):
        return self.name


class Favorites(models.Model):
    """Модель избранное."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    movie = models.ForeignKey(
        Movies,
        on_delete=models.CASCADE,
        verbose_name='Фильм'
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
    
    def __str__(self):
        return f'У пользователя {self.user} в избранном {self.movie}'
