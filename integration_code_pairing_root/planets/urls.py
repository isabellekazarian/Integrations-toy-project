from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>/', views.get_by_id),
    path('population/<int:population>/', views.get_planets_by_population)
]