from rest_framework import serializers
from showtimes.models import Cinema
from movielist.models import Movie


class CinemaSerializer(serializers.ModelSerializer):
    movies = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='movies-detail')

    class Meta:
        model = Cinema
        fields = ("name", "city", "movies")
