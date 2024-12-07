from djoser.views import UserViewSet
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404 

from users.models import User
from reviews.models import Movies, Favorites
from .serializers import UsersSerializer, MovieSerializer, FavoritesSerializer


class UserCustomViewSet(UserViewSet):
    """Вьюсет для пользователя."""

    queryset = User.objects.all()
    serializer_class = UsersSerializer

    def destroy(self, request, *args, **kwargs):
        """Удаление только своего профиля."""
    
        user = self.get_object()
        if user != request.user:
            return Response({'Вы не можете удалить чужой профиль.'},
                            status=status.HTTP_403_FORBIDDEN)

        self.perform_destroy(user)
        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели фольмов."""

    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

    @action(detail=True, methods=['POST', 'DELETE']) 
    def favorite(self, request, **kwargs):
        """Добавление и удаление фильмов в избранное."""
    
        movie = get_object_or_404(Movies, id=kwargs['pk']) 
        if request.method == 'POST': 
            serializer = FavoritesSerializer( 
                data={'user': request.user.id, 
                      'movie': movie.id}, 
                context={'request': request}, 
            ) 
            serializer.is_valid(raise_exception=True) 
            serializer.save(user=request.user, movie=movie) 
            return Response(serializer.data, 
                            status=status.HTTP_201_CREATED)
        get_object_or_404(Favorites, user=request.user, 
                          movie=movie).delete() 
        return Response({'Фильм удален из избранного'}, status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=False, methods=['GET',],
            url_path='list_favorite')
    def list_favorite(self, request):
        """Отображение списка избранного."""
    
        user = request.user
        favorites = Favorites.objects.filter(user=user)
        serializer = FavoritesSerializer(favorites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
