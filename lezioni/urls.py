from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),


    path('corsi/', views.corsi, name='corsi'),
    path('corsi/<int:id>/lezioni/', views.lezioni, name='lezioni'),
    path('corsi/lezioni/<int:id>/', views.dettaglio_lezione, name='dettaglio_lezione'),


    path('mostra/targhetta/<targa>/', views.mostra_targa, name='mostra_targa'),
]