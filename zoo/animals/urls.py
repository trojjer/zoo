from django.urls import path

from . import views


urlpatterns = [
    path('population/', views.AnimalPopulationView.as_view(), name='population'),
    path('animal/', views.AnimalView.as_view(), name='animal'),
]
