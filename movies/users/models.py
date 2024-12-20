from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя."""

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'first_name', 'last_name')
    email = models.EmailField(
        max_length=150,
        unique=True,
        verbose_name='e-mail',
        help_text='Укажите свой e-mail'
    )
    username = models.CharField(
        max_length=150,
        verbose_name='Никнейм пользователя',
        help_text='Кажите свой никнейм'
    )
    first_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Имя пользователя',
        help_text='Укажите свое имя'
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия пользователя',
        blank=True,
        help_text='Укажите свою фамилию'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ['username']
    
    def __str__(self):
        return self.username
