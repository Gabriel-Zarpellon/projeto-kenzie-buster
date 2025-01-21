from rest_framework import serializers
from .models import Rating, Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    duration = serializers.CharField(required=False, default="")
    rating = serializers.ChoiceField(choices=Rating.choices, default=Rating.G)
    synopsis = serializers.CharField(required=False, default="")

    added_by = serializers.CharField(read_only=True, source="user.email")

    def create(self, validated_data: dict):
        return Movie.objects.create(**validated_data)
