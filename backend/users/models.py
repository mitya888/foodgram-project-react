from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель кастомного юзера"""

    email = models.EmailField(
        max_length=200,
        unique=True,
        verbose_name='Почта',
    )
    username = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Логин',
    )
    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя',
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        ordering = ['username']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


class Follow(models.Model):
    """Модель подписок"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор',
    )

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['user', 'author'],
            name='unigue_subscriber',
        )]
        ordering = ['-author']
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return self.author[:10]
