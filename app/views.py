from django.shortcuts import render
from rest_framework import generics
from django_filters import rest_framework as filters
from .serializers import BucketlistSerializer
from .models import Bucketlist


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class ListView(generics.ListAPIView):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer