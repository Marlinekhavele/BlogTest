from django.urls import include, path
from app.views import (
    ListView,
    CreateView,
    DetailView,

)

urlpatterns = [
    path('list/',ListView.as_view(),name='list'),
    path('create-bucketlist/',CreateView.as_view(),name='create-bucketlist'),
    path('<int:pk>/',DetailView.as_view(),name='details'),

]
