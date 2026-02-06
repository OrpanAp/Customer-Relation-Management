from django.urls import path
from . import views

app_name = 'leads'

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('leads/', views.lead_list, name="lead_list"),
    path('leads/details/<int:pk>/', views.lead_details, name="lead_details"),
]
