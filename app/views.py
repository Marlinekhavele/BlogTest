from django.shortcuts import render
from rest_framework import generics
from django_filters import rest_framework as filters
from .serializers import BucketlistSerializer
from .models import Bucketlist
from rest_framework import permissions



class CreateView(generics.ListCreateAPIView):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(owner=self.request.user)

class ListView(generics.ListAPIView):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
