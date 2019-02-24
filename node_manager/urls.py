from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:node_pk>/', views.upload, name='upload'),
]
