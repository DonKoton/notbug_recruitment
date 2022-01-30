from django.urls import path

from pokedex import views

app_name = "pokedex"

urlpatterns = [
    path('', views.index, name='index'),
    path('pokemon/<int:poke_id>/', views.details, name='details'),
]
