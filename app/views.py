from django.shortcuts import render
from rest_framework import generics,permissions
from .permissions import IsOwner
from django_filters import rest_framework as filters
from .serializers import BucketlistSerializer, UserSerializer
from .models import Bucketlist
from django.contrib.auth.models import User



class CreateView(generics.ListCreateAPIView):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated,IsOwner)

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(owner=self.request.user)

class ListView(generics.ListAPIView):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated,IsOwner)

class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


