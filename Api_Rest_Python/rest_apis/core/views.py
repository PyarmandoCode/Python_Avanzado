from django.shortcuts import render
from rest_framework import generics,status
from .models import Movies,Reviewers
from .serializers import movies_serializer,reviewers_serializer

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.parsers import JSONParser


class MoviesList(generics.ListAPIView):
    #Select * from Movies
    queryset=Movies.objects.all()
    serializer_class=movies_serializer


class ReviewersList(generics.ListAPIView):
    #Select * from Movies
    queryset=Reviewers.objects.all()
    serializer_class=reviewers_serializer


@api_view(['GET','POST','DELETE'])
def movie_ser_full(request):
    if request.method=='GET':
        movies=Movies.objects.all()
    elif request.method == 'POST':
        #Informacion que se le pasa desde el Body y luego es Parseada
        movie_data=JSONParser().parse(request) 
        #Serializando la nueva data
        mov_serializer=movies_serializer(data=movie_data)   
        #Validando y Guardando el Nuevo Registro
        if mov_serializer.is_valid():
            mov_serializer.save()
            return JsonResponse(mov_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(movie_serializer.errors,status.HTTP_400_BAD_REQUEST)
    movie_serializer= movies_serializer(movies,many=True) 
    return JsonResponse(movie_serializer.data,safe=False)

