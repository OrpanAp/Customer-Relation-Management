from django.urls import path
from . import views

app_name = 'leads'

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('leads/', views.lead_list, name="lead_list"),
    path('leads/details/<int:pk>/', views.lead_details, name="lead_details"),
    path('leads/add/', views.lead_create, name="lead_create"),
    path('leads/update/<int:pk>/', views.lead_update, name="lead_update"),
    path('leads/delete/<int:pk>/', views.lead_delete, name="lead_delete"),
]
