from rest_framework import serializers
from basic_app.models import Movie_detail

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_detail
        fields = '__all__'
