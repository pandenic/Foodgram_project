"""Describe custom mixins for the users app."""
from rest_framework import mixins, viewsets


class ListCreateViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """Describe a custom ViewSet for List and Create methods."""

    pass
