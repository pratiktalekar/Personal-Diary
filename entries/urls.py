from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('add_entry/', views.add_entry, name='add_entry'),
]