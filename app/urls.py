from django.urls import include, path
from app.views import (
    ListView,
    CreateView,
    DetailView,

)
from rest_framework.authtoken import views


urlpatterns = [
    path('list/',ListView.as_view(),name='list'),
    path('create-bucketlist/',CreateView.as_view(),name='create-bucketlist'),
    path('<int:pk>/',DetailView.as_view(),name='details'),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    path('api-token-auth/', views.obtain_auth_token)


]
