from django.urls import path
from .views import MoviesList,ReviewersList,movie_ser_full


urlpatterns = [
    path('api/listar_movies',MoviesList.as_view()),
    path('api/listar_reviewers',ReviewersList.as_view()),
    path('api/listarmovies',movie_ser_full)
]
