from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<str:lobby>', views.index, name='room'),
    path('<str:room>/', views.index, name='room'),
    path('send/', views.index),
]