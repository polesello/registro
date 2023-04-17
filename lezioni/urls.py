from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mostra/targhetta/<targa>/', views.mostra_targa, name='mostra_targa'),
]