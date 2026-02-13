from django.urls import path
from . import views

app_name = 'leads'

""" urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('leads/', views.lead_list, name="lead_list"),
    path('leads/details/<int:pk>/', views.lead_details, name="lead_details"),
    path('leads/add/', views.lead_create, name="lead_create"),
    path('leads/update/<int:pk>/', views.lead_update, name="lead_update"),
    path('leads/delete/<int:pk>/', views.lead_delete, name="lead_delete"),
] """


urlpatterns = [
    path('', views.HomeView.as_view(), name="home_page"),
    path('leads/', views.LeadListView.as_view(), name="lead_list"),
    path('leads/details/<int:pk>/', views.LeadDetailView.as_view(), name="lead_details"),
    path('leads/add/', views.LeadCreateView.as_view(), name="lead_create"),
    path('leads/update/<int:pk>/', views.LeadUpdateView.as_view(), name="lead_update"),
    path('leads/delete/<int:pk>/', views.LeadDeleteView.as_view(), name="lead_delete"),
    path('leads/assign_agent/<int:pk>/', views.AgentAssignView.as_view(), name="assign_agent"),
    path('leads/categories/', views.CategoryListView.as_view(), name="categories"),
    path('leads/categories/details/<int:pk>/', views.CategoryDetailView.as_view(), name="category_details"),
    path('leads/categories/update/<int:pk>/', views.LeadCategoryUpdateView.as_view(), name="category_update"),
]



    