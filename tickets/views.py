from tickets.models import Movie
from tickets.serializers import MovieSerializer
from rest_framework import generics


class SurveyDetailView(generics.RetrieveAPIView):
    """API view to handle retrieving a specific Survey by its ID."""

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'
