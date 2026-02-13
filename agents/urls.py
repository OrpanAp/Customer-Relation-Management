from django.urls import path
from . import views



app_name = 'agents'

urlpatterns = [
    path('agents/', views.AgentListView.as_view(), name="agents"),
    path('agents/add/', views.AgentCreateView.as_view(), name="agent_create"),
    path('agents/details/<int:pk>/', views.AgentDetailView.as_view(), name="agent_details"),
    path('agents/update/<int:pk>/', views.AgentUpdateView.as_view(), name="agent_update"),
    path('agents/delete/<int:pk>/', views.AgentDeleteView.as_view(), name="agent_delete"),
]
    