from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL for the homepage
    path('residential_solar/', views.residential_solar, name='residential_solar'),  # URL for the Residential Solar page
    path('commercial_solar/', views.commercial_solar, name='commercial_solar'),  # URL for the Commercial Solar page
]