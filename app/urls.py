from django.urls import include, path
from app.views import (
    ListView,
    CreateView, 
)

urlpatterns = [
    path('list/',ListView.as_view(),name='list'),
    path('create-bucketlist/',CreateView.as_view(),name='create-bucketlist'),
]
