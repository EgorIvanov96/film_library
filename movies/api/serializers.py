from rest_framework import serializers

from users.models import User
from reviews.models import Movies, Favorites


class UsersSerializer(serializers.ModelSerializer):
    """Сериализатор модели пользователя."""


    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name'
        )


class MovieSerializer(serializers.ModelSerializer):
    """Сериализатор модели фильма."""

    class Meta:
        model = Movies
        fields = (
            'name',
            'description',
            'producer',
            'years_movi',
            'author'
        )


class FavoritesSerializer(serializers.ModelSerializer):
    """Сериализатор модели избранного."""

    class Meta:
        model = Favorites
        fields = ('user', 'movie')
        message = 'Фильм добавлен в избранное'
