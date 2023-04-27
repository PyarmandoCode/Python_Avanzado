from rest_framework import serializers
from .models import Movies,Reviewers


class movies_serializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'


class reviewers_serializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewers
        fields = '__all__'        