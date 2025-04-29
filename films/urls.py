from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_film, name='add_film'),
    path('list/', views.film_list, name='film_list'),
]
