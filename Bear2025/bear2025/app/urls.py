from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Link to the index view
   
]
